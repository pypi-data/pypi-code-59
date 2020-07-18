import torch
from .loss import make_one_hot, DiceLoss
import numpy as np
import torch.nn.functional as F

def creat_loss(predicts:torch.Tensor, labels:torch.Tensor, num_classes, cal_miou=True):
    predicts = predicts.permute((0, 2, 3, 1))
    predicts = predicts.reshape((-1, num_classes))
    bce_loss = F.cross_entropy(predicts, labels.flatten(), reduction="mean")
    labels_one_hot = make_one_hot(labels.reshape((-1, 1)), num_classes)
    dice_loss = DiceLoss()(predicts, labels_one_hot.to(labels.device))
    loss = bce_loss + dice_loss
    if cal_miou:
        ious = compute_iou(predicts, labels.reshape((-1, 1)), num_classes)
        miou = np.nanmean(ious)
    else:
        miou = None
    return loss, miou

def compute_iou(predicts, labels, num_classes):

    ious = torch.zeros(num_classes)
    predicts = F.softmax(predicts, dim=1)
    predicts = torch.argmax(predicts, dim=1, keepdim=True)
    for i in range(num_classes):
        intersect = torch.sum((predicts == i) * (labels == i))
        area = torch.sum(predicts == i) + torch.sum(labels == i) - intersect
        if area == 0 and intersect == 0:
            ious[i] = np.nan
        else:
            ious[i] = intersect.float() / area.float()
    return ious

