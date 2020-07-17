import tensorflow as tf
import cv2, os, glob
import numpy as np

from .preprocessing import anchor_targets_bbox, anchors_for_shape
from .utils import RetinanetConfig
from cral.data_feeder.object_detection_parser import DetectionBase


class RetinanetGenerator(DetectionBase):
    """docstring for RetinanetGenerator"""
    def __init__(self, config, *args, **kwargs):
      super(RetinanetGenerator, self).__init__(*args, **kwargs)
      assert isinstance(config, RetinanetConfig), 'please provide a `RetinanetConfig()` object'
      self.config = config

    def process_bboxes_labels(self, image_array, bboxes, labels):

        # delete bboxes containing [-1,-1,-1,-1]
        # tf.print('preprocess label bboxes',np.unique(labels), labels.shape, bboxes.shape)
        bboxes = bboxes[~np.all(bboxes<0, axis=-1)]

        # delete labels containing[-1]
        labels = labels[labels>-1]
        # print('after deleting label bboxes',np.unique(labels), labels.shape, bboxes.shape)

        # generate raw anchors
        raw_anchors = anchors_for_shape(
            image_shape=image_array.shape,
            sizes=self.config.sizes,
            ratios=self.config.ratios,
            scales=self.config.scales,
            strides=self.config.strides,
            pyramid_levels=[3, 4, 5, 6, 7],
            shapes_callback=None)

        # generate anchorboxes and class labels      
        gt_regression, gt_classification = anchor_targets_bbox(
              anchors=raw_anchors,
              image=image_array,
              bboxes=bboxes,
              gt_labels=labels,
              num_classes=self.num_classes,
              negative_overlap=0.4,
              positive_overlap=0.5)

        return gt_regression, gt_classification

    def yield_image_regression_classification(self, xmin_batch, ymin_batch, xmax_batch, ymax_batch, label_batch, image_batch):

        regression_batch = list()
        classification_batch = list()

        for index in range(self.batch_size):
            xmins, ymins, xmaxs, ymaxs, labels = xmin_batch[index], ymin_batch[index], xmax_batch[index], ymax_batch[index], label_batch[index]
            image_array = image_batch[index]
            bboxes = tf.convert_to_tensor([xmins,ymins,xmaxs,ymaxs], dtype=tf.keras.backend.floatx())
            bboxes = tf.transpose(bboxes)
            gt_regression, gt_classification = tf.numpy_function(self.process_bboxes_labels, [image_array, bboxes, labels], Tout=[tf.keras.backend.floatx(), tf.keras.backend.floatx()])

            regression_batch.append(gt_regression)
            classification_batch.append(gt_classification)

        return tf.convert_to_tensor(regression_batch), tf.convert_to_tensor(classification_batch)
