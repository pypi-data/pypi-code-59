# -*- coding: UTF-8 -*-
import json
import numpy as np
from collections import defaultdict

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval


def get_file_annots(file_path):
    with open(file_path) as fp:
        data = json.load(fp)
    images = {i["id"]: i for i in data["images"]}
    annots = data["annotations"]
    image_annots = defaultdict(list)
    for annot in annots:
        image_id = annot["image_id"]
        image_annots[image_id].append(annot)
    return images, image_annots, data


def get_bbox(annot):
    bbox = np.array(annot["bbox"], dtype=np.float32)
    bbox[2] = bbox[0] + bbox[2]
    bbox[3] = bbox[1] + bbox[3]
    return bbox


def coco_keypoint_eval(res_file, gt_file):
    coco = COCO(gt_file)
    coco_dt = coco.loadRes(res_file)
    coco_eval = COCOeval(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return coco_eval.stats
