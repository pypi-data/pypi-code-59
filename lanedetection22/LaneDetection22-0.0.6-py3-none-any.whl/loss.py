import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class SoftmaxCrossEntropyLoss(nn.Module):
    def __init__(self, num_classes):
        super(SoftmaxCrossEntropyLoss, self).__init__()
        self.num_classes = num_classes

    def forward(self, inputs, labels):
        if inputs.dim() > 2:
            inputs = inputs.view(inputs.size(0), inputs.size(1),-1)
            inputs = inputs.transpose(1,2)
            inputs = inputs.contiguous().view(-1, self.num_classes)
        labels = labels.view(-1)
        return nn.CrossEntropyLoss(reduction='mean')(inputs, labels)
def make_one_hot(input, num_classes):

    shape = np.array(input.shape)
    shape[1] = num_classes
    shape = tuple(shape)
    result = torch.zeros(shape)
    result = result.scatter_(1, input.cpu(), 1)

    return result

class BinaryDicelLoss(nn.Module):
    def __init__(self, smooth=1, p=2, reduction='mean'):
        super(BinaryDicelLoss, self).__init__()
        self.smooth = smooth
        self.p = p
        self.reduction = reduction

    def forward(self, predict, target):
        assert predict.shape[0] == target.shape[0]
        predict = predict.contiguous().view(predict.shape[0],-1)
        target = target.contiguous().view(target.shape[0],-1)
        num = 2 * torch.sum(torch.mul(predict,target),dim=1) + self.smooth
        den = torch.sum(predict.pow(self.p)+ target.pow(self.p),dim=1)+ self.smooth

        loss = 1 - num / den

        if self.reduction == "mean":
            return loss.mean()
        elif self.reduction == "sum":
            return loss.sum()
        elif self.reduction == "none":
            return loss
        else:
            raise Exception("Unexpected reduction format.")

class DiceLoss(nn.Module):
    def __init__(self, weight= None, ignore_index=None, **kwargs):
        super(DiceLoss, self).__init__()
        self.kwargs = kwargs
        self.weight = weight
        self.ignore_index = ignore_index

    def forward(self, predict, target):
        assert predict.shape == target.shape, 'predict & target shape do not match'
        dice = BinaryDicelLoss(**self.kwargs)
        total_loss = 0
        predict = F.softmax(predict, dim=1)

        for i in range(target.shape[1]):
            if i != self.ignore_index:
                dice_loss = dice(predict[:, i], target[:, i])
                if self.weight is not None:
                    assert self.weight.shape[0] == target.shape[1], \
                        'Expect weight shape [{}], get[{}]'.format(target.shape[1], self.weight.shape[0])
                    dice_loss *= self.weight[i]
                total_loss += dice_loss

        return  total_loss/target.shape[1]