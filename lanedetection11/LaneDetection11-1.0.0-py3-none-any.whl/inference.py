from packaging_tutorial.lanedetection.Config import ConfigTrain
import packaging_tutorial.lanedetection.utilss
from packaging_tutorial.lanedetection.model.deeplab import DeepLab
import numpy as np
import pandas as pd
import cv2
import torch
from torchvision import transforms
from packaging_tutorial.lanedetection.utilss.data import decodePredicts

def inference():
    cfg = ConfigTrain()
    print('please input your device: cpu or cuda')
    device = input()
    device = torch.device(device)
    net = DeepLab(num_classes=cfg.NUM_CLASSES)
    print('please input your pretrain weight path:')
    weight_path = input()
    # weight_path = 'F:/pycharm/xiangmu_week7/weight/road04_4'
    net.load_state_dict(torch.load(weight_path))
    net = net.to(device)
    net.eval()
    print('please input your picture path:')
    input_image_path = input()
    input_image = cv2.imread(input_image_path)
    # input_image = cv2.imread('C:/Users/Administrator/Desktop/170927_064448134_Camera_5.jpg')
    input_image = cv2.resize(input_image, (1024,384) )
    import matplotlib.pyplot as plt
    plt.imshow(input_image)
    plt.show()
    preprocess = transforms.Compose([transforms.ToTensor()])
    input_image = preprocess(input_image)
    input_image = input_image.unsqueeze(0)
    print(input_image.shape)
    input_image=input_image.to(device)
    output = net(input_image)
    print(output.shape)


    # output = output[0]
    # print(output.shape)
    # print(output[0].shape)
    # output = output.detach().numpy()

    outs = decodePredicts(output, (3384, 1710), cfg.CROP)
    print(outs.shape)
    # outs = outs.permute((0, 2, 3, 1)).numpy().astype(np.uint8)
    # for i in range(outs.shape[0]):
    outs = outs[0][0]
    plt.imshow(outs)
    plt.show()
    #


if __name__ == '__main__':
    inference()
