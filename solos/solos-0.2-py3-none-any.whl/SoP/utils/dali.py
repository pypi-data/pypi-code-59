try:
    from nvidia.dali.pipeline import Pipeline
    import nvidia.dali.ops as ops
    import nvidia.dali.types as types
    from nvidia.dali.plugin.pytorch import DALIGenericIterator
except:
    raise ImportError('No nvidia DALI found')
from ..config.deep_config import *
import torch

from .dataset import BSSDataset

"""
The aim of this file is using Nvidia's DALI.
At the moment this is a prototype
"""

__all__ = ['PostProcessor', 'get_dali_pipeline']


def reformat_trace(trace, idx):
    indices = [x['indices'][idx] for x in trace]
    kwargs = [x['kwargs'][idx] for x in trace]
    return zip(indices, kwargs)


class AudioVisualPipe(Pipeline):
    def __init__(self, batch_size: int, num_threads: int, device_id: int, dataset: BSSDataset, seed: int):
        super(AudioVisualPipe, self).__init__(batch_size, num_threads, device_id, seed=seed,
                                              prefetch_queue_depth=PREFETCH_QUEUE_DEPTH,
                                              exec_pipelined=EXEC_PIPELINED)
        self.dataset = dataset

        self.input = ops.VideoReaderResize(device="gpu", file_list=DALI_VIDEO_DATASET_PATH,
                                           sequence_length=N_VIDEO_FRAMES,
                                           shard_id=0, num_shards=1, file_list_frame_num=True,
                                           random_shuffle=False, skip_vfr_check=True,
                                           resize_x=224, resize_y=224)
        self.normalize = ops.Normalize(device='gpu')
        if STFT_WINDOW.__name__ == 'hann_window':
            window_fn = []
        else:
            window_fn = STFT_WINDOW(N_FFT).tolist()
        self.spectrogram = ops.Spectrogram(device="gpu",
                                           nfft=N_FFT,
                                           window_length=N_FFT,
                                           window_step=HOP_LENGTH,
                                           window_fn=window_fn)
        self.audio_main_data = ops.ExternalSource()
        self.audio_slave_data = ops.ExternalSource()
        self.skeleton_data = ops.ExternalSource()
        self.traces = self.dataset.prepare_data_for_dali(DALI_VIDEO_DATASET_PATH, 40)
        # Divide the list in chunks of size=batch_size
        self.idx = 0
        self.traces = [self.traces[i * batch_size:(i + 1) * batch_size] for i in
                       range((len(self.traces) + batch_size - 1) // batch_size)]

    def define_graph(self):
        video = self.input(name='video')
        video = self.normalize(video[0])
        self.audio_main = self.audio_main_data(name='audio_main').gpu()
        self.audio_slave = self.audio_slave_data(name='audio_slave').gpu()
        sp_main = self.spectrogram(self.audio_main)
        sp_slave = self.spectrogram(self.audio_slave)
        sp_mix = self.spectrogram(self.audio_main + self.audio_slave)
        self.skeleton = self.skeleton_data(name='skeleton')

        # Expected output by pytorch ['sp1', 'sp2', 'spm', 'sk', 'vd']
        return sp_main, sp_slave, sp_mix, self.skeleton, video

    def iter_setup(self):
        trace_main = reformat_trace(self.traces[self.idx], 0)
        trace_slave = reformat_trace(self.traces[self.idx], 1)
        audio_main, skeleton = self.dataset.getitem(trace_main, 2, ['audio', 'skeleton_npy'])
        audio_slave = self.dataset.getitem(trace_slave, 2, ['audio'])
        self.feed_input(self.audio_main, audio_main)
        self.feed_input(self.skeleton, skeleton)
        self.feed_input(self.audio_slave, audio_slave[0])
        self.idx += 1


class PostProcessor:
    # Expected output by pytorch ['sp1', 'sp2', 'spm', 'sk', 'vd']
    def __init__(self, dataset: BSSDataset, device, debug: bool):
        self.main_device = device
        self.dataset = dataset
        self.debug = debug

    def __call__(self, dali_dataloader):
        for (data) in dali_dataloader:
            data = data[0]
            sp = torch.stack([data['sp1'], data['sp2']], dim=1)
            gt = []
            spm = []
            for sp_i, spm_i in zip(sp, data['spm']):
                spm_o, gt_o = self.dataset.binary_mask_dali(sp_i, spm_i, self.debug)
                spm.append(spm_o)
                gt.append(gt_o)
            spm = torch.stack(spm)
            gt = torch.stack(gt)

            yield self.dataset.postprocessor(spm, gt=gt,sk=data['sk'], vd=data['vd'], dali=True)


def get_dali_pipeline(batch_size, num_threads, device_id, dataset, seed):
    return AudioVisualPipe(batch_size, num_threads, device_id, dataset, seed)
