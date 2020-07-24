# -*- coding: UTF-8 -*-
import os
import glob
from abc import abstractmethod
from copy import deepcopy

import numpy as np
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit

__all__ = ["TRTInference", "TRTClassifier", "EntropyCalibrator", "CaffeModelBuilder", "OnnxModelBuilder", "save_engine"]

from hxlxalgos.utils.common import AlgorithmHelper, Const

_TRT_LOGGER = trt.Logger(trt.Logger.ERROR)

# We first load all custom plugins shipped with TensorRT,
# some of them will be needed during inference
trt.init_libnvinfer_plugins(_TRT_LOGGER, '')
_TRT_RUNTIME = trt.Runtime(_TRT_LOGGER)
_EXPLICIT_BATCH = 1 << (int)(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)


# Simple helper data class that's a little nicer to use than a 2-tuple.
class HostDeviceMem(object):
    def __init__(self, host_mem, device_mem):
        self.host = host_mem
        self.device = device_mem

    def __str__(self):
        return "Host:\n" + str(self.host) + "\nDevice:\n" + str(self.device)

    def __repr__(self):
        return self.__str__()


# Allocates all buffers required for an engine, i.e. host/device inputs/outputs.
def allocate_buffers(engine):
    inputs = []
    outputs = []
    bindings = []
    stream = cuda.Stream()
    for binding in engine:
        size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
        dtype = trt.nptype(engine.get_binding_dtype(binding))
        # Allocate host and device buffers
        host_mem = cuda.pagelocked_empty(size, dtype)
        device_mem = cuda.mem_alloc(host_mem.nbytes)
        # Append the device buffer to device bindings.
        bindings.append(int(device_mem))
        # Append to the appropriate list.
        if engine.binding_is_input(binding):
            inputs.append(HostDeviceMem(host_mem, device_mem))
        else:
            outputs.append(HostDeviceMem(host_mem, device_mem))
    return inputs, outputs, bindings, stream


# This function is generalized for multiple inputs/outputs.
# inputs and outputs are expected to be lists of HostDeviceMem objects.
def do_inference(context, bindings, inputs, outputs, stream, batch_size=1):
    # Transfer input data to the GPU.
    [cuda.memcpy_htod_async(inp.device, inp.host, stream) for inp in inputs]
    # Run inference.
    context.execute_async(batch_size=batch_size, bindings=bindings, stream_handle=stream.handle)
    # Transfer predictions back from the GPU.
    [cuda.memcpy_dtoh_async(out.host, out.device, stream) for out in outputs]
    # Synchronize the stream
    stream.synchronize()
    # Return only the host outputs.
    return [out.host for out in outputs]


# This function is generalized for multiple inputs/outputs for full dimension networks.
# inputs and outputs are expected to be lists of HostDeviceMem objects.
def do_inference_v2(context, bindings, inputs, outputs, stream):
    # Transfer input data to the GPU.
    [cuda.memcpy_htod_async(inp.device, inp.host, stream) for inp in inputs]
    # Run inference.
    context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)
    # Transfer predictions back from the GPU.
    [cuda.memcpy_dtoh_async(out.host, out.device, stream) for out in outputs]
    # Synchronize the stream
    stream.synchronize()
    # Return only the host outputs.
    return [out.host for out in outputs]


def GiB(val):
    return val * 1 << 30


def save_engine(engine, engine_dest_path):
    dir_path = os.path.split(engine_dest_path)[0]
    if not dir_path:
        dir_path = "./"
    os.makedirs(dir_path, exist_ok=True)
    buf = engine.serialize()
    with open(engine_dest_path, 'wb') as f:
        f.write(buf)


def load_engine(trt_runtime, engine_path):
    assert os.path.exists(engine_path), "Trt model file %s not exist!" % engine_path
    with open(engine_path, 'rb') as f:
        engine_data = f.read()
    engine = trt_runtime.deserialize_cuda_engine(engine_data)
    return engine


class TRTInference(Const):
    """Manages TensorRT objects for model inference."""
    model_name = ""

    def __init__(self, engine_path: str, *args, **kwargs):
        super(TRTInference, self).__init__(*args, **kwargs)
        """Initializes TensorRT objects needed for model inference.

        Args:
            engine_path (str): path where TensorRT engine should be stored
        """

        # If we get here, the file with engine exists, so we can load it
        self._trt_engine = load_engine(_TRT_RUNTIME, engine_path)

        # Display requested engine settings to stdout
        print("=> TensorRT-{} inference engine settings:".format(self.model_name))
        print("  * Serialized engine path = {}".format(engine_path))
        print("  * Max batch size = {}\n".format(self._trt_engine.max_batch_size))

        # This allocates memory for network inputs/outputs on both CPU and GPU
        self._inputs, self._outputs, self._bindings, self._stream = allocate_buffers(self._trt_engine)

        # Execution context is needed for inference
        self._context = self._trt_engine.create_execution_context()

        self.input_res = None
        self.input_w, self.input_h = None, None
        self.mean = None
        self.std = None
        self.num_classes = None
        self.class_names = None
        self.thresh = None
        self.output_shapes = None
        self.transform = None
        self.helper = AlgorithmHelper(self.model_name, with_lock=True)

    def _pre_process(self, image: np.ndarray):
        """
        A abstractmethod, which need to be overridden in subclasses.
        """
        if self.transform is not None:
            return self.transform(image)
        else:
            raise NotImplementedError

    @abstractmethod
    def _post_process(self, outputs: list(), meta: dict = None):
        """
        A abstractmethod, which need to be overridden in subclasses.
        """
        raise NotImplementedError

    def predict(self, image: np.ndarray):
        """Infers model on given image.
        Args:
            image (np.ndarray): image to run model on
        """
        with self.helper.pre_stage:
            meta = self._pre_process(image)
        with self.helper.exec_stage:
            outputs = self._forward(meta["image"])
            outputs = [i.reshape(self.output_shapes[index]) for index, i in enumerate(outputs)]
        with self.helper.post_stage:
            results = self._post_process(outputs, meta)
        return results

    __call__ = predict

    def _forward(self, image):
        # Copy it into appropriate place into memory
        # (self.inputs was returned earlier by allocate_buffers())
        np.copyto(self._inputs[0].host, image.ravel())

        # When infering on single image, we measure inference
        # time to output it to the user
        # Fetch output from the model
        outputs = do_inference(
            self._context, bindings=self._bindings, inputs=self._inputs,
            outputs=self._outputs, stream=self._stream)
        return [np.array(output, dtype=np.float32) for output in outputs]


class TRTClassifier(TRTInference):
    res_template = {"cls_name": '', "confidence": -1, 'scores': [], 'label': -1}

    def _post_process(self, outputs: list(), meta: dict = None):
        obj = deepcopy(self.res_template)
        probs = np.squeeze(outputs)
        indies = np.argsort(probs)[::-1]
        ap = probs[indies] > np.array(self.thresh)[indies]
        if np.all(ap == False):
            obj.update(cls_name=self.class_names[-1], scores=probs.tolist(), label=len(self.class_names) - 1)
        else:
            label = indies[np.where(ap == True)][0]
            obj.update(cls_name=self.class_names[label], confidence=probs[label], scores=probs.tolist(), label=label)
        return obj


class EntropyCalibrator(trt.IInt8EntropyCalibrator2):

    def __init__(self, args):
        trt.IInt8EntropyCalibrator2.__init__(self)

        self.cache_file = args.saveCalib
        self.batch_size = args.maxBatch
        self.channel = args.channel
        self.height = args.height
        self.width = args.width
        self.image_paths = glob.glob(os.path.join(args.inputs_dir, "*.npy"))
        assert len(self.image_paths) > 0, print(
            "=> Found empty input data with path=%s which is used to calibrate." % args.inputs_dir)
        self.batch_idx = 0
        self.max_batch_idx = len(self.image_paths) // self.batch_size
        self.data_size = trt.volume([self.batch_size, self.channel, self.height, self.width]) * trt.float32.itemsize
        self.device_input = cuda.mem_alloc(self.data_size)

    def next_batch(self):
        if self.batch_idx < self.max_batch_idx:
            batch_files = self.image_paths[self.batch_idx * self.batch_size:(self.batch_idx + 1) * self.batch_size]
            batch_imgs = np.zeros((self.batch_size, self.channel, self.height, self.width), dtype=np.float32)
            for index, file_path in enumerate(batch_files):
                input_img = np.load(file_path)
                assert (input_img.nbytes == self.data_size / self.batch_size), \
                    "=> Invalid input data %s, expect input bytes=%d, but got input bytes=%d!" % \
                    (file_path, self.data_size / self.batch_size, input_img.nbytes)
                batch_imgs[index] = input_img
            self.batch_idx += 1
            print("\r=> Batch:[{}/{}]".format(self.batch_idx, self.max_batch_idx), end="")
            return np.ascontiguousarray(batch_imgs)
        else:
            return np.array([])

    def get_batch_size(self):
        return self.batch_size

    def get_batch(self, names, p_str=None):
        try:
            batch_imgs = self.next_batch()
            if batch_imgs.size == 0 or batch_imgs.size != self.batch_size * self.channel * self.height * self.width:
                return None
            cuda.memcpy_htod(self.device_input, batch_imgs.astype(np.float32))
            return [int(self.device_input)]
        except Exception as e:
            print("=> Unexpected error: {}".format(e))
            return None

    def read_calibration_cache(self):
        # If there is a cache, use it instead of calibrating again. Otherwise, implicitly return None.
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "rb") as f:
                return f.read()

    def write_calibration_cache(self, cache):
        with open(self.cache_file, "wb") as f:
            f.write(cache)


def _create_network(builder, explicit_batch=None):
    if explicit_batch:
        return builder.create_network(explicit_batch)
    else:
        return builder.create_network()


class CaffeModelBuilder(object):
    def __init__(self, args, calib=None):
        self.deploy_file = args.deploy
        self.model_file = args.model
        self.output_names = args.output
        self.max_batch_size = args.maxBatch
        self.explicit_batch = _EXPLICIT_BATCH if args.explicitBatch else None
        self.mode = args.mode
        self.dtype = args.inputIOFormats
        self.calib = calib
        self.workspace = GiB(args.workspace)
        assert args.mode.lower() in ('fp32', 'fp16', 'int8'), "=> Mode should be in ('fp32', 'fp16', 'int8')"

    def build_engine(self):
        with trt.Builder(_TRT_LOGGER) as builder, _create_network(builder, self.explicit_batch) as network, \
                trt.CaffeParser() as parser:
            builder.max_batch_size = self.max_batch_size
            builder.max_workspace_size = self.workspace
            if self.mode.lower() == 'int8':
                assert (builder.platform_has_fast_int8 == True), "=> Current platform not support int8"
                builder.int8_mode = True
                builder.int8_calibrator = self.calib
            elif self.mode.lower() == 'fp16':
                assert (builder.platform_has_fast_fp16 == True), "=> Current platform not support fp16"
                builder.fp16_mode = True

            model_tensors = parser.parse(deploy=self.deploy_file, model=self.model_file,
                                         network=network, dtype=self.dtype)
            if model_tensors is None:
                print("=> Parser network error, maybe some layers not support in tensorRT,"
                      "you can check this with using trtexec bin file!")
                for error in range(parser.num_errors):
                    print("=> Parser error: {}".format(parser.get_error(error)))
                return None
            for name in self.output_names:
                network.mark_output(model_tensors.find(name))

            # Build engine
            return builder.build_cuda_engine(network)


class OnnxModelBuilder(object):

    def __init__(self, args, calib=None):
        self.onnx = args.onnx
        self.max_batch_size = args.maxBatch
        self.explicit_batch = _EXPLICIT_BATCH if args.explicitBatch else None
        self.mode = args.mode
        self.calib = calib
        self.workspace = GiB(args.workspace)
        assert args.mode.lower() in ('fp32', 'fp16', 'int8'), "mode should be in ('fp32', 'fp16', 'int8')"

    def build_engine(self):
        with trt.Builder(_TRT_LOGGER) as builder, _create_network(builder, self.explicit_batch) as network, \
                trt.OnnxParser(network, _TRT_LOGGER) as parser:
            builder.max_batch_size = self.max_batch_size
            builder.max_workspace_size = self.workspace
            if self.mode.lower() == 'int8':
                assert (builder.platform_has_fast_int8 == True), "=> Current platform not support int8"
                builder.int8_mode = True
                builder.int8_calibrator = self.calib
            elif self.mode.lower() == 'fp16':
                assert (builder.platform_has_fast_fp16 == True), "=> Current platform not support fp16"
                builder.fp16_mode = True
            # Parse Onnx model
            with open(self.onnx, 'rb') as model:
                if not parser.parse(model.read()):
                    print("=> Parser network error, maybe some layers not support in tensorRT,"
                          "you can check this with using trtexec bin file!")
                    for error in range(parser.num_errors):
                        print(parser.get_error(error))
                    return None
            return builder.build_cuda_engine(network)
