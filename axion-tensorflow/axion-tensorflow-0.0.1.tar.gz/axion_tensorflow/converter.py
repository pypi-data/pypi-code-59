import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from axion_tensorflow import layers as qlayers

__all__ = ["Converter"]


class Converter:
    def __init__(self):
        pass

    def convert_keras(self, keras_model, example):
        if isinstance(keras_model, models.Sequential):
            metas = self._convert_keras_sequential(keras_model)
        elif isinstance(keras_model, models.Model):
            metas = self._convert_keras_functional(keras_model)
        else:
            raise ValueError("Unsupported model type: {}".format(type(keras_model)))
        if "compnode" in metas[-1] and metas[-1]["compnode"] == "npu":
            metas[-1]["compnode"] = "cpu"
        self.fill_output(metas, example)
        return metas

    def fill_output(self, metas, example):
        md = {l["name"]: l for l in metas}
        inputs = [l["output_tensor"] for l in metas if l["type"] == "data"]
        if len(inputs) != 1:
            raise ValueError("Unsupported number of inputs: {}.".format(len(inputs)))
        outputs = {l["name"]: l["output_tensor"] for l in metas}
        f = tf.keras.backend.function(inputs=inputs, outputs=outputs)
        output_values = f(example)
        for k, v in output_values.items():
            md[k]["output"] = v
        for l in metas:
            l.pop("output_tensor")

    def _convert_keras_sequential(self, sequential_model):
        metas = []
        last_layer = None
        last_meta = None

        default_input = "input"

        metas.append(
            {
                "name": default_input,
                "type": "data",
                # input is in [0; 1], set data_ratio to 255 to scale to [0; 255].
                "data_ratio": 255,
                "of_bit": 8,
                "output_tensor": sequential_model.input,
            }
        )

        for l in sequential_model.layers:
            if hasattr(l, "get_bitmeta"):
                m = l.get_bitmeta()
                m["output_tensor"] = l.output
                if last_layer is not None:
                    # layer_name, is_unpool
                    m["input"].append((last_layer.name, False))
                else:
                    m["input"].append((default_input, False))
                metas.append(m)
                last_layer = l
                last_meta = m
            elif isinstance(l, layers.InputLayer):
                raise ValueError("InputLayer is not supported in sequential model.")
            else:
                fuse_meta(last_meta, l)

        last_bits = None
        for m in metas:
            m["if_bit"] = last_bits
            last_bits = m["of_bit"]
        return metas

    def _convert_keras_functional(self, functional_model):
        metas = {}

        for l in functional_model.layers:
            if hasattr(l, "get_bitmeta"):
                m = l.get_bitmeta()
                m["output_tensor"] = l.output
                metas[m["name"]] = m
            elif isinstance(l, layers.InputLayer):
                m = {
                    "name": l.name,
                    "type": "data",
                    # input is in [0; 1], set data_ratio to 255 to scale to [0; 255].
                    "data_ratio": 255,
                    "of_bit": 8,
                    "output_tensor": l.output,
                }
                metas[m["name"]] = m

        # This is needed for nested concatenate.
        # l is axion layer or Concat
        def fill_input(metas, l, input, if_bit):
            if isinstance(l, layers.Concatenate):
                if l.axis != 1:
                    raise ValueError(
                        "Unsupported concatenate axis: {}, should be 1.".format(l.axis)
                    )
                for n in l.outbound_nodes:
                    fill_input(metas, n.outbound_layer, input, if_bit)
            else:
                m = metas.get(l.name)
                if m is None:
                    raise ValueError(
                        "Invalid network: {} should be a axion layer.".format(l.name)
                    )
                m["input"].append(input)
                if m["if_bit"] is None:
                    m["if_bit"] = if_bit
                elif m["if_bit"] != if_bit:
                    raise ValueError("if_bit mismatch for {}".format(l.name))

        def try_fuse(metas, current_meta, current_layer):
            num_outs = len(current_layer.outbound_nodes)
            if num_outs == 0:
                return
            if num_outs > 1:
                for n in current_layer.outbound_nodes:
                    fill_input(
                        metas,
                        n.outbound_layer,
                        (current_meta["name"], False),
                        current_meta["of_bit"],
                    )
                return
            outbound_layer = current_layer.outbound_nodes[0].outbound_layer
            if isinstance(outbound_layer, layers.Concatenate) or (
                metas.get(outbound_layer.name) is not None
            ):
                fill_input(
                    metas,
                    outbound_layer,
                    (current_meta["name"], False),
                    current_meta["of_bit"],
                )
                return
            # outbound_layer is not axion layer nor Concat
            fuse_meta(current_meta, outbound_layer)
            try_fuse(metas, current_meta, outbound_layer)

        for name, meta in metas.items():
            l = functional_model.get_layer(name)
            try_fuse(metas, meta, l)

        metas = list(metas.values())
        return metas


def fuse_meta(meta, l: layers.Layer):
    if isinstance(l, qlayers.Activation):
        meta["of_bit"] = l.activation_bits
        # y = multiplier * (gamma * x + beta)
        # => y = multiplier * (gamma * (k * x + b) + beta)
        # => k' = k * gamma * multiplier, b' = b * multiplier * gamma + beta * multiplier
        meta["affine_k"] *= l.gamma.numpy() * l.multiplier
        meta["affine_b"] = meta["affine_b"] * l.gamma.numpy() * l.multiplier + l.beta.numpy() * l.multiplier
    elif isinstance(l, layers.BatchNormalization) or str(type(l)) == "<class 'tensorflow.python.keras.layers.normalization.BatchNormalization'>":
        # y = (x - mean) * tf.rsqrt(variance + eps)
        # => y = (k * x + b - mean) * tf.rsqrt(variance + eps)
        # => k' = k * tf.rsqrt(variance + eps), b' = (b - mean) * tf.rsqrt(variance + eps)
        inv_stddev = tf.math.rsqrt(l.moving_variance + l.epsilon).numpy()
        meta["affine_k"] *= inv_stddev
        meta["affine_b"] = (meta["affine_b"] - l.moving_mean.numpy()) *  inv_stddev
        if l.center or l.scale:
            raise ValueError("BatchNormalization should not enable center or scale.")
    elif isinstance(l, layers.MaxPooling2D):
        if meta is None or meta["type"] != "conv":
            raise ValueError(
                "MaxPooling2D is only supported when immediately after a Conv2D layer."
            )
        ph, pw = l.pool_size
        if ph != pw:
            raise ValueError(
                "MaxPooling2D must have the same pool_size on both dimensions."
            )
        if l.pool_size != l.strides:
            raise ValueError("MaxPooling2D must have the same pool_size and strides.")
        meta["pooling"] = ph
    elif isinstance(l, layers.Flatten):
        return
    else:
        raise ValueError("Unsupported layer: {}".format(l.name))
    # Update output tensor.
    meta["output_tensor"] = l.output
