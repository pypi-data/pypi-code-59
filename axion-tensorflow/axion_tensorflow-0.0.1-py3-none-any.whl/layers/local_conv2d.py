import numpy as np
import tensorflow as tf
from tensorflow import nn
from tensorflow.keras import layers
from tensorflow.python.keras import initializers
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.utils import conv_utils
from axion_tensorflow import fake_quant

@tf.keras.utils.register_keras_serializable(package="Axion")
class LocalConv2D(layers.Layer):
    """ Quantization aware Local Conv2D. """

    def __init__(
        self,
        filters,
        kernel_size,
        spatial_groups,
        groups=1,
        strides=1,
        kernel_bits=4,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        data_format="channels_last",
        **kwargs,
    ):
        super().__init__(**kwargs)
        if data_format not in ["channels_first"]:
            raise ValueError("data_format currently supports only channels_first.")
        if spatial_groups not in [(1, 2), (1, 4)]:
            raise ValueError("spatial_groups only supports (1, 2) or (1, 4).")
        self.filters = filters
        self.kernel_size = kernel_size
        self.kernel_bits = kernel_bits
        self.spatial_groups = spatial_groups
        self.groups = groups
        self.strides = strides
        self.kernel_initializer = initializers.get(kernel_initializer)
        self.bias_initializer = initializers.get(bias_initializer)

    def build(self, input_shape):
        spatial_h, spatial_w = self.spatial_groups
        unused_N, C, H, W = input_shape
        h_interval = (H + 2) // spatial_h
        w_interval = (W + 2) // spatial_w
        out_H = conv_utils.conv_output_length(H, self.kernel_size,
                                               "VALID", self.strides)
        out_W = conv_utils.conv_output_length(W, self.kernel_size,
                                               "VALID", self.strides)
        kernel_shape = (
            spatial_h,
            spatial_w,
            self.kernel_size * self.kernel_size * (C // self.groups),
            self.filters,
        )

        self.kernel = self.add_weight(
            name="kernel", shape=kernel_shape, initializer=self.kernel_initializer,
        )
        self.bias = self.add_weight(
            name="bias", shape=(self.filters,), initializer=self.bias_initializer
        )

    def call(self, inputs):
        q_kernel, unused_scale = fake_quant.fake_quant_weights(
            self.kernel, num_bits=self.kernel_bits
        )
        x = tf.pad(inputs, [[0, 0], [0, 0], [1, 1], [1, 1]])
        # x = nn.conv2d(
        #     x, q_kernel, self.strides, padding="VALID", data_format="NCHW"
        # )
        x = K.local_conv(inputs, self.kernel, self.kernel_size, self.strides,
                            (self.output_row, self.output_col),
                            data_format="NCHW")
        x = nn.bias_add(x, self.bias, data_format="NCHW")
        return x

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "filters": self.filters,
                "kernel_size": self.kernel_size,
                "strides": self.strides,
                "groups": self.groups,
                "kernel_bits": self.kernel_bits,
                "kernel_initializer": initializers.serialize(self.kernel_initializer),
                "bias_initializer": initializers.serialize(self.bias_initializer),
                "data_format": "channels_first",
            }
        )
        return config

    def get_bitmeta(self):
        q_kernel, scale = fake_quant.fake_quant_weights(
            self.kernel, num_bits=self.kernel_bits
        )
        q_kernel = q_kernel / scale
        # bitmeta shape is (oc, ic, 3, 3), while tensorflow shape is (3, 3, ic, oc).
        q_kernel = tf.transpose(q_kernel, perm=(3, 2, 0, 1))
        # special treatment for the current converter.
        q_kernel, scale =  q_kernel / 2, scale * 2
        return {
            "name": self.name,
            "type": "conv",
            "if_bit": None,
            "w_bit": self.kernel_bits,
            "of_bit": 0,
            "input": [],
            "groups": self.groups,
            "affine_k": np.zeros((self.filters,)) + scale.numpy(),
            "affine_b": self.bias.numpy(),
            "weight": q_kernel.numpy(),
            "stride": self.strides,
            "pooling": None,
            "compnode": "npu",
            # TODO: Remove data ratio.
            "data_ratio": 255,
        }
