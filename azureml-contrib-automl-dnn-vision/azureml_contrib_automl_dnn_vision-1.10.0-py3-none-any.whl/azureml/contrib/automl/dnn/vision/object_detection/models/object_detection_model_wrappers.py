# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Helper functions to build model wrappers."""
import logging

import torch
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

from .base_model_wrapper import BaseObjectDetectionModelWrapper
from .customrcnn import CustomRCNNWrapper, CustomRCNNSpecifications
from ..common.constants import ModelNames, RCNNBackbones
from ...common.pretrained_model_utilities import PretrainedModelFactory

DEFAULT_MODEL = ModelNames.FASTER_RCNN_RESNET50_FPN

logger = logging.getLogger(__name__)


class FasterRCNNResnet50FPNWrapper(BaseObjectDetectionModelWrapper):
    """Model wrapper for Faster RCNN with Resnet50 FPN backbone."""

    def __init__(self, number_of_classes=None, **kwargs):
        """
        :param number_of_classes: Number of object classes
        :type number_of_classes: Int
        :param kwargs: Optional keyword arguments to define model specifications
        :type kwargs: dict
        """

        model = self._create_model(number_of_classes, **kwargs)

        self._gen_rcnn_transform = model.transform
        logger.debug("{} model transform exposed".format(self.__class__.__name__))

        super().__init__(model=model, number_of_classes=number_of_classes)

    def _create_model(self, number_of_classes, specs=None, **kwargs):
        model = PretrainedModelFactory.fasterrcnn_resnet50_fpn(pretrained=True, **kwargs)

        if number_of_classes is not None:
            input_features = model.roi_heads.box_predictor.cls_score.in_features
            model.roi_heads.box_predictor = FastRCNNPredictor(input_features,
                                                              number_of_classes)

        return model

    def disable_model_transform(self):
        """Disable resize and normalize from the model.

        :return:
        """

        self.model.transform.resize = self.identity_resize
        self.model.transform.normalize = self.identity_normalize

    @staticmethod
    def identity_normalize(image):
        """A NOP normalization method.

        :param image: image to normalize
        :return: same image
        """
        return image

    @staticmethod
    def identity_resize(image, target_index):
        """A NOP resize method.

        :param image: image to resize.
        :param target_index: target index to resize.
        :return: tuple with same image and target_index.
        """
        return image, target_index

    def transform(self, is_train, image, boxes):
        """Exposes model specific transformations.

        :param is_train: True if the transformations are for training, False otherwise.
        :param image: image tensor, 3 dimensions
        :param boxes: boxes tensor
        :return: a tuple with new image, boxes, height and width
        """

        self._gen_rcnn_transform.training = is_train
        new_image, new_boxes = self._gen_rcnn_transform(torch.unsqueeze(image, 0),  # transform expects a batch
                                                        [{"boxes": boxes}])
        # remove the batch dimension
        new_image = torch.squeeze(new_image.tensors, 0)
        # the first element of the list contains the boxes for the image,
        # as the batch only has one entry
        new_boxes = new_boxes[0]["boxes"]

        new_height = new_image.shape[1]
        new_width = new_image.shape[2]

        return new_image, new_boxes, new_height, new_width


class FasterRCNNResnet18FPNWrapper(CustomRCNNWrapper):
    """Model wrapper for Faster RCNN with Resnet 18 FPN backbone."""

    _specifications = CustomRCNNSpecifications(
        backbone=RCNNBackbones.RESNET_18_FPN_BACKBONE)

    def __init__(self, number_of_classes, **kwargs):
        """
        :param number_of_classes: Number of object classes
        :type number_of_classes: Int
        :param kwargs: Optional keyword arguments to define model specifications
        :type kwargs: dict
        """

        super().__init__(number_of_classes, self._specifications, **kwargs)


class FasterRCNNMobilenetV2Wrapper(CustomRCNNWrapper):
    """Model wrapper for Faster RCNN with MobileNet v2 w/o FPN backbone."""

    _specifications = CustomRCNNSpecifications(
        backbone=RCNNBackbones.MOBILENET_V2_BACKBONE)

    def __init__(self, number_of_classes, **kwargs):
        """
        :param number_of_classes: Number of object classes
        :type number_of_classes: Int
        :param kwargs: Optional keyword arguments to define model specifications
        :type kwargs: dict
        """

        super().__init__(number_of_classes, self._specifications, **kwargs)


class ObjectDetectionModelFactory:
    """Factory function to create models."""

    _models_dict = {
        ModelNames.FASTER_RCNN_RESNET50_FPN: FasterRCNNResnet50FPNWrapper,
        ModelNames.FASTER_RCNN_RESNET18_FPN: FasterRCNNResnet18FPNWrapper,
        ModelNames.FASTER_RCNN_MOBILENETV2: FasterRCNNMobilenetV2Wrapper
    }

    @staticmethod
    def _get_model_wrapper(number_of_classes=None, model_name=None, **kwargs):

        if model_name is None:
            model_name = DEFAULT_MODEL

        if model_name not in ObjectDetectionModelFactory._models_dict:
            raise ValueError('Unsupported model')

        return ObjectDetectionModelFactory._models_dict[model_name](number_of_classes=number_of_classes, **kwargs)
