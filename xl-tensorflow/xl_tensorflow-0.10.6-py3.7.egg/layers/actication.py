#!usr/bin/env python3
# -*- coding: UTF-8 -*-
import tensorflow as tf
from tensorflow.keras import layers, backend
from tensorflow.python.keras.utils import tf_utils
import math


@tf.keras.utils.register_keras_serializable(package='Text')
class HSwish(layers.Layer):
    def __init__(self, **kwargs):
        super(HSwish, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        # alpha is used for leaky relu slope in activations instead of
        # negative_slope.
        return tf.multiply(backend.sigmoid(inputs), tf.nn.relu6(inputs + 3) / 6)

    def get_config(self):
        base_config = super(HSwish, self).get_config()
        return base_config

    @tf_utils.shape_type_conversion
    def compute_output_shape(self, input_shape):
        return input_shape


@tf.keras.utils.register_keras_serializable(package='Text')
class Swish(layers.Layer):
    def __init__(self, **kwargs):
        super(Swish, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        # alpha is used for leaky relu slope in activations instead of
        # negative_slope.
        # return tf.multiply(backend.sigmoid(inputs), inputs)
        return tf.nn.swish(inputs)

    def get_config(self):
        base_config = super(Swish, self).get_config()
        return base_config

    @tf_utils.shape_type_conversion
    def compute_output_shape(self, input_shape):
        return input_shape


@tf.keras.utils.register_keras_serializable(package='Text')
class Mish(layers.Layer):
    def __init__(self, **kwargs):
        super(Mish, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        # alpha is used for leaky relu slope in activations instead of
        # negative_slope.
        return tf.multiply(backend.tanh(backend.softplus(inputs)), inputs)

    def get_config(self):
        base_config = super(Mish, self).get_config()
        return base_config

    @tf_utils.shape_type_conversion
    def compute_output_shape(self, input_shape):
        return input_shape


def get_swish(**kwargs):
    def swish(x):
        """Swish activation function: x * sigmoid(x).
        Reference: [Searching for Activation Functions](https://arxiv.org/abs/1710.05941)
        """
        return tf.nn.swish(x)

    return swish


def get_mish():
    def mish(inputs):
        return tf.multiply(backend.tanh(backend.softplus(inputs)), inputs)

    return mish


@tf.keras.utils.register_keras_serializable(package='Text')
def gelu(x):
    """Gaussian Error Linear Unit.

    This is a smoother version of the RELU.
    Original paper: https://arxiv.org/abs/1606.08415
    Args:
      x: float Tensor to perform activation.

    Returns:
      `x` with the GELU activation applied.
    """
    cdf = 0.5 * (1.0 + tf.tanh(
        (math.sqrt(2 / math.pi) * (x + 0.044715 * tf.pow(x, 3)))))
    return x * cdf


@tf.keras.utils.register_keras_serializable(package='Text')
def simple_swish(features):
    """Computes the Swish activation function.

    The tf.nn.swish operation uses a custom gradient to reduce memory usage.
    Since saving custom gradients in SavedModel is currently not supported, and
    one would not be able to use an exported TF-Hub module for fine-tuning, we
    provide this wrapper that can allow to select whether to use the native
    TensorFlow swish operation, or whether to use a customized operation that
    has uses default TensorFlow gradient computation.

    Args:
      features: A `Tensor` representing preactivation values.

    Returns:
      The activation value.
    """
    features = tf.convert_to_tensor(features)
    return features * tf.nn.sigmoid(features)


@tf.keras.utils.register_keras_serializable(package='Text')
def hard_swish(features):
    """Computes a hard version of the swish function.

    This operation can be used to reduce computational cost and improve
    quantization for edge devices.

    Args:
      features: A `Tensor` representing preactivation values.

    Returns:
      The activation value.
    """
    features = tf.convert_to_tensor(features)
    return features * tf.nn.relu6(features + tf.constant(3.)) * (1. / 6.)


@tf.keras.utils.register_keras_serializable(package='Text')
def identity(features):
    """Computes the identity function.

    Useful for helping in quantization.

    Args:
      features: A `Tensor` representing preactivation values.

    Returns:
      The activation value.
    """
    features = tf.convert_to_tensor(features)
    return tf.identity(features)


@tf.keras.utils.register_keras_serializable(package='Text')
def get_relu6():
    def relu6(x):
        """Swish activation function: x * sigmoid(x).
        Reference: [Searching for Activation Functions](https://arxiv.org/abs/1710.05941)
        """
        return tf.nn.relu6(x)

    return relu6
