from typing import *

import keras
from keras.models import Model
import keras.layers as KL
from keras.applications import *

import numpy as np

'''
Pretrained models on ImageNet available in Keras:
  Xception
  VGG16
  VGG19
  ResNet
  ResNetV2
  InceptionV3
  InceptionResNetV2
  MobileNet
  MobileNetV2
  DenseNet
  NASNet
'''

class CustomBackbone:
  '''
  Define a custom CNN backbone (all except FC layers).
  Stores input's shape and layers.

  Args:
    layers: List of Keras/custom layers.
    input_shape: (height, width, channels).
  '''

  def __init__(
    self,
    layers: List[KL.Layer],
    input_shape: Optional[Tuple[int, int, int]],
  ) -> None:
    self.input_shape = input_shape
    self.layers = layers

  def get_backbone(
    self,
    input_shape: Optional[Tuple[int, int, int]] = None,
  ) -> Model:
    '''
    Compute the backbone into a Keras Model.

    Args:
      input_shape: (height, width, channels) or the default.

    Returns:
      A visual feature extractor as Keras Model.
    '''

    if input_shape is None:
      input_shape = self.input_shape

    model_input = Input(shape=self.input_shape)

    x = model_input
    for layer in self.layers:
      x = layer(x)

    model_output = x

    return Model(model_input, model_output)

    
class CustomCNN:
  '''
  Define a customized Convolutional Neural Network.
  Possibility to use transfer learning.
  Define CNN weigths, hyperparameters and final FC layer.

  Args:
    base_model: CustomBackbone object or from [
      'Xception',
      'VGG16',
      'VGG19',
      'ResNet50',
      'ResNet101',
      'ResNet152',
      'ResNet50V2',
      'ResNet101V2',
      'ResNet152V2',
      'InceptionV3',
      'InceptionResNetV2',
      'MobileNet',
      'MobileNetV2',
      'DenseNet121',
      'DenseNet169',
      'DenseNet201',
      'NASNetMobile',
      'NASNetLarge',
    ]
    weights: 'imagenet' is the only currently available value for transfer
      learning.
    input_shape: (height, width, channels) or None for default.
    last_layer: 'flatten', 'global_max', 'global_avg'.
    nb_layers_to_freeze:
      'all' to freeze the backbone.
      int to freeze the n first layers.
    nb_outputs: Number of neurons in the last Dense layer.
    **kwargs: Parameters for the last Dense layer.
  '''

  def __init__(
    self,
    base_model: Union[CustomBackbone, str] = 'VGG16', # TODO
    weights: Optional[str] = 'imagenet', # TODO: MyTypes.str('imagenet')
    input_shape: Optional[Tuple[int, int, int]] = None,
    last_layer: str = 'flatten', # TODO
    nb_layers_to_freeze: Union[int, str] = 'all', # TODO
    nb_outputs: int = 1,
    **kwargs
  ):
    dict_models = {
      'Xception': (xception, xception.Xception),
      'VGG16': (vgg16, vgg16.VGG16),
      'VGG19': (vgg19, vgg19.VGG19),
      'ResNet50': (resnet, resnet.ResNet50),
      'ResNet101': (resnet, resnet.ResNet101),
      'ResNet152': (resnet, resnet.ResNet152),
      'ResNet50V2': (resnet_v2, resnet_v2.ResNet50V2),
      'ResNet101V2': (resnet_v2, resnet_v2.ResNet101V2),
      'ResNet152V2': (resnet_v2, resnet_v2.ResNet152V2),
      'InceptionV3': (inception_v3, inception_v3.InceptionV3),
      'InceptionResNetV2': (inception_resnet_v2, inception_resnet_v2.InceptionResNetV2),
      'MobileNet': (mobilenet, mobilenet.MobileNet),
      'MobileNetV2': (mobilenet_v2, mobilenet_v2.MobileNetV2),
      'DenseNet121': (densenet, densenet.DenseNet121),
      'DenseNet169': (densenet, densenet.DenseNet169),
      'DenseNet201': (densenet, densenet.DenseNet201),
      'NASNetMobile': (nasnet, nasnet.NASNetMobile),
      'NASNetLarge': (nasnet, nasnet.NASNetLarge),
    }

    dict_last_layer = {
      'flatten': KL.Flatten,
      'global_max': KL.GlobalMaxPooling2D,
      'global_avg': KL.GlobalAveragePooling2D,
    }

    self.input_shape = input_shape

    # Existing backbone
    if isinstance(base_model, str):
      self.base_model_module, self.base_model = dict_models[base_model]

      feature_extractor = self.base_model(
        weights=weights,
        include_top=False,
        input_shape=self.input_shape,
      )
    # CustomBackbone
    else:
      self.base_model = base_model
      feature_extractor = self.base_model.get_backbone(
        input_shape=self.input_shape,
      )
      self.base_model_module = None
      
    # Set layers untrainable
    if nb_layers_to_freeze == 'all':
      for layer in feature_extractor.layers:
        layer.trainable = False
    else:
      i = 0
      for layer in feature_extractor.layers:
        if i >= nb_layers_to_freeze:
          break
        if len(layer.get_weights()) > 0:
          i += 1
        layer.trainable = False

    # New layers
    x = feature_extractor.output
    x = dict_last_layer[last_layer]()(x)
    x = KL.Dense(nb_outputs, **kwargs)(x)
    self.model = Model(feature_extractor.input, x)
    
  def print_frozen(self) -> None:
    '''
    Pretty print layers and states (frozen or not).
    '''

    max_len = max([len(layer.name) for layer in self.model.layers])
    for layer in self.model.layers:
      text = ('Trainable' if layer.trainable else 'Frozen')\
        if len(layer.get_weights()) > 0 else 'No weights'
      print(layer.name, '.' * (max_len + 2 - len(layer.name)), text)