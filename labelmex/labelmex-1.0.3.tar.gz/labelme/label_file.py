import base64
import io
import json
import os.path as osp

#JJ
import collections
import datetime
import uuid
import numpy as np
#import pycocotools.mask
import labelme

import PIL.Image

from labelme import __version__
from labelme.logger import logger
from labelme import PY2
from labelme import QT4
from labelme import utils


PIL.Image.MAX_IMAGE_PIXELS = None


class LabelFileError(Exception):
    pass


class LabelFile(object):

    suffix = '.json'

    def __init__(self, filename=None):
        self.shapes = []
        self.imagePath = None
        self.imageData = None
        if filename is not None:
            self.load(filename)
        self.filename = filename

    @staticmethod
    def load_image_file(filename):
        try:
            image_pil = PIL.Image.open(filename)
        except IOError:
            logger.error('Failed opening image file: {}'.format(filename))
            return

        # apply orientation to image according to exif
        image_pil = utils.apply_exif_orientation(image_pil)

        with io.BytesIO() as f:
            ext = osp.splitext(filename)[1].lower()
            if PY2 and QT4:
                format = 'PNG'
            elif ext in ['.jpg', '.jpeg']:
                format = 'JPEG'
            else:
                format = 'PNG'
            image_pil.save(f, format=format)
            f.seek(0)
            return f.read()

    def load(self, filename):
        keys = [
            'version',
            'imageData',
            'imagePath',
            'shapes',  # polygonal annotations
            'flags',   # image level flags
            'imageHeight',
            'imageWidth',
        ]
        shape_keys = [
            'label',
            'points',
            'group_id',
            'shape_type',
            'flags',
        ]
        try:
            with open(filename, 'rb' if PY2 else 'r') as f:
                data = json.load(f)
            version = data.get('version')
            if version is None:
                logger.warn(
                    'Loading JSON file ({}) of unknown version'
                    .format(filename)
                )
            elif version.split('.')[0] != __version__.split('.')[0]:
                logger.warn(
                    'This JSON file ({}) may be incompatible with '
                    'current labelme. version in file: {}, '
                    'current version: {}'.format(
                        filename, version, __version__
                    )
                )

            if data['imageData'] is not None:
                imageData = base64.b64decode(data['imageData'])
                if PY2 and QT4:
                    imageData = utils.img_data_to_png_data(imageData)
            else:
                # relative path from label file to relative path from cwd
                imagePath = osp.join(osp.dirname(filename), data['imagePath'])
                imageData = self.load_image_file(imagePath)
            flags = data.get('flags') or {}
            imagePath = data['imagePath']
            self._check_image_height_and_width(
                base64.b64encode(imageData).decode('utf-8'),
                data.get('imageHeight'),
                data.get('imageWidth'),
            )
            shapes = [
                dict(
                    label=s['label'],
                    points=s['points'],
                    shape_type=s.get('shape_type', 'polygon'),
                    flags=s.get('flags', {}),
                    group_id=s.get('group_id'),
                    other_data={
                        k: v for k, v in s.items() if k not in shape_keys
                    }
                )
                for s in data['shapes']
            ]
        except Exception as e:
            raise LabelFileError(e)

        otherData = {}
        for key, value in data.items():
            if key not in keys:
                otherData[key] = value

        # Only replace data after everything is loaded.
        self.flags = flags
        self.shapes = shapes
        self.imagePath = imagePath
        self.imageData = imageData
        self.filename = filename
        self.otherData = otherData

    @staticmethod
    def _check_image_height_and_width(imageData, imageHeight, imageWidth):
        img_arr = utils.img_b64_to_arr(imageData)
        if imageHeight is not None and img_arr.shape[0] != imageHeight:
            logger.error(
                'imageHeight does not match with imageData or imagePath, '
                'so getting imageHeight from actual image.'
            )
            imageHeight = img_arr.shape[0]
        if imageWidth is not None and img_arr.shape[1] != imageWidth:
            logger.error(
                'imageWidth does not match with imageData or imagePath, '
                'so getting imageWidth from actual image.'
            )
            imageWidth = img_arr.shape[1]
        return imageHeight, imageWidth

    def save(
        self,
        filename,
        shapes,
        imagePath,
        imageHeight,
        imageWidth,
        imageData=None,
        otherData=None,
        flags=None,
    ):
        if imageData is not None:
            imageData = base64.b64encode(imageData).decode('utf-8')
            imageHeight, imageWidth = self._check_image_height_and_width(
                imageData, imageHeight, imageWidth
            )
        if otherData is None:
            otherData = {}
        if flags is None:
            flags = {}
        data = dict(
            version=__version__,
            flags=flags,
            shapes=shapes,
            imagePath=imagePath,
            imageData=imageData,
            imageHeight=imageHeight,
            imageWidth=imageWidth,
        )
        for key, value in otherData.items():
            assert key not in data
            data[key] = value
        try:
            with open(filename, 'wb' if PY2 else 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.filename = filename
        except Exception as e:
            raise LabelFileError(e)

    # #JJ
    # def save_coco(
    #     self,
    #     filename,
    #     shapes,
    #     imagePath,
    #     imageHeight,
    #     imageWidth,
    #     imageData=None,
    #     otherData=None,
    #     flags=None,
    # ):
    #     if imageData is not None:
    #         imageData = base64.b64encode(imageData).decode('utf-8')
    #         imageHeight, imageWidth = self._check_image_height_and_width(
    #             imageData, imageHeight, imageWidth
    #         )
    #     if otherData is None:
    #         otherData = {}
    #     if flags is None:
    #         flags = {}
        
    #     now = datetime.datetime.now()

    #     data = dict(
    #         info=dict(
    #             description=None,
    #             url=None,
    #             version=None,
    #             year=now.year,
    #             contributor=None,
    #             date_created=now.strftime('%Y-%m-%d %H:%M:%S.%f'),
    #         ),
    #         licenses=[dict(
    #             url=None,
    #             id=0,
    #             name=None,
    #         )],
    #         images=[
    #             # license, url, file_name, height, width, date_captured, id
    #         ],
    #         type='instances',
    #         annotations=[
    #             # segmentation, area, iscrowd, image_id, bbox, category_id, id
    #         ],
    #         categories=[
    #             # supercategory, id, name
    #         ],
    #     )

    #     class_name_to_id = {}
    #     for i, shape in enumerate(shapes):
    #         class_name = shape['label']
    #         class_id = i + 1
    #         if class_name not in class_name_to_id:
    #             class_name_to_id[class_name] = class_id
    #             data['categories'].append(dict(
    #                 supercategory=None,
    #                 id=class_id,
    #                 name=class_name,
    #             ))

    #     img = np.asarray(PIL.Image.open(imagePath).convert('RGB'))

    #     data['images'].append(dict(
    #         license=0,
    #         url=None,
    #         file_name=osp.basename(imagePath),
    #         height=imageHeight,
    #         width=imageWidth,
    #         date_captured=None,
    #         id=1,
    #     ))

    #     masks = {}                                     # for area
    #     segmentations = collections.defaultdict(list)  # for segmentation
    #     for shape in shapes:
    #         points = shape['points']
    #         label = shape['label']
    #         group_id = shape.get('group_id')
    #         shape_type = shape.get('shape_type')
    #         mask = labelme.utils.shape_to_mask(
    #             img.shape[:2], points, shape_type
    #         )

    #         if group_id is None:
    #             group_id = uuid.uuid1()

    #         instance = (label, group_id)

    #         if instance in masks:
    #             masks[instance] = masks[instance] | mask
    #         else:
    #             masks[instance] = mask

    #         points = np.asarray(points).flatten().tolist()
    #         segmentations[instance].append(points)
    #     segmentations = dict(segmentations)

    #     for instance, mask in masks.items():
    #         cls_name, group_id = instance
    #         if cls_name not in class_name_to_id:
    #             continue
    #         cls_id = class_name_to_id[cls_name]

    #         mask = np.asfortranarray(mask.astype(np.uint8))
    #         mask = pycocotools.mask.encode(mask)
    #         area = float(pycocotools.mask.area(mask))
    #         bbox = pycocotools.mask.toBbox(mask).flatten().tolist()

    #         data['annotations'].append(dict(
    #             id=len(data['annotations']),
    #             image_id=1,
    #             category_id=cls_id,
    #             segmentation=segmentations[instance],
    #             area=area,
    #             bbox=bbox,
    #             iscrowd=0,
    #         ))

    #     try:
    #         with open(filename, 'wb' if PY2 else 'w') as f:
    #             json.dump(data, f, ensure_ascii=False, indent=2)
    #         self.filename = filename
    #     except Exception as e:
    #         raise LabelFileError(e)

    @staticmethod
    def is_label_file(filename):
        return osp.splitext(filename)[1].lower() == LabelFile.suffix
