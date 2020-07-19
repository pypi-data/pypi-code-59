import numpy as np
import cv2
import torch
import os

def encode_gray_label(labels):
    """
    将标签图的灰度值转换成类别id
    注意：ignoreInEval为True的都当分类0处理
    @param labels: 标签灰度图
    """
    encoded_labels = np.zeros_like(labels)
    # 除了下面特意转换的，其余都属于类别0
    # 1
    encoded_labels[labels == 200] = 1
    encoded_labels[labels == 204] = 1
    encoded_labels[labels == 209] = 1
    # 2
    encoded_labels[labels == 201] = 2
    encoded_labels[labels == 203] = 2
    # 3
    encoded_labels[labels == 217] = 3
    # 4
    encoded_labels[labels == 210] = 4
    # 5
    encoded_labels[labels == 214] = 5
    # 6
    encoded_labels[labels == 220] = 6
    encoded_labels[labels == 221] = 6
    encoded_labels[labels == 222] = 6
    encoded_labels[labels == 224] = 6
    encoded_labels[labels == 225] = 6
    encoded_labels[labels == 226] = 6
    # 7
    encoded_labels[labels == 205] = 7
    encoded_labels[labels == 227] = 7
    encoded_labels[labels == 250] = 7
    return encoded_labels

def decode_gray_label(labels: torch.Tensor):
    """
    将类别id恢复成灰度值
    @params labels: shape=(h, w)
    """
    decoded_labels = torch.zeros(labels.size(), dtype=torch.int)
    # 1
    decoded_labels[labels == 1] = 204
    # 2
    decoded_labels[labels == 2] = 203
    # 3
    decoded_labels[labels == 3] = 217
    # 4
    decoded_labels[labels == 4] = 210
    # 5
    decoded_labels[labels == 5] = 214
    # 6
    decoded_labels[labels == 6] = 224
    # 7
    decoded_labels[labels == 7] = 227
    return decoded_labels

def decode_color_label(labels: torch.Tensor):
    """
    将类别id恢复成RGB值
    @params labels: shape=(h, w)
    """
    decoded_labels = torch.zeros((3, labels.shape[0], labels.shape[1]), dtype=torch.int)
    # 1  dividing
    decoded_labels[0][labels == 1] = 70
    decoded_labels[1][labels == 1] = 130
    decoded_labels[2][labels == 1] = 180
    # 2  guiding
    decoded_labels[0][labels == 2] = 0
    decoded_labels[1][labels == 2] = 0
    decoded_labels[2][labels == 2] = 142
    # 3  stopping
    decoded_labels[0][labels == 3] = 153
    decoded_labels[1][labels == 3] = 153
    decoded_labels[2][labels == 3] = 153
    # 4  parking
    decoded_labels[0][labels == 4] = 128
    decoded_labels[1][labels == 4] = 64
    decoded_labels[2][labels == 4] = 128
    # 5  zebra
    decoded_labels[0][labels == 5] = 190
    decoded_labels[1][labels == 5] = 153
    decoded_labels[2][labels == 5] = 153
    # 6 thru/turn
    decoded_labels[0][labels == 6] = 128
    decoded_labels[1][labels == 6] = 78
    decoded_labels[2][labels == 6] = 160
    # 7  reductiion
    decoded_labels[0][labels == 7] = 255
    decoded_labels[1][labels == 7] = 128
    decoded_labels[2][labels == 7] = 0
    return decoded_labels


def  crop_resize_data(image, label, out_size, height_crop_offset):
    roi_img = image[height_crop_offset:]
    roi_img = cv2.resize(roi_img, out_size, interpolation=cv2.INTER_LINEAR)
    if label is not None:
        roi_label = label[height_crop_offset:]
        roi_label = cv2.resize(roi_label, out_size, interpolation=cv2.INTER_LINEAR)
    else:
        roi_label = None
    return roi_img, roi_label

def train_data_generate(image_list, label_list, batch_size, out_size, heignt_crop_offset):

    indices = np.arange(0, len(image_list))
    out_images = []
    out_labels = []
    out_images_filename = []
    while True:
        np.random.shuffle(indices)
        for i in indices:
            try:
                image = cv2.imread(image_list[i])
                label = cv2.imread(label_list[i],cv2.IMREAD_GRAYSCALE)
            except:
                continue
            if image is None or label is None:
                continue
            image, label = crop_resize_data(image, label, out_size, heignt_crop_offset)

            label = encode_gray_label(label)
            out_images.append(image)
            out_labels.append(label)
            out_images_filename.append(image_list[i])
            if len(out_images) == batch_size:
                out_images = np.array(out_images, dtype=np.float32)
                out_labels = np.array(out_labels, dtype=np.int64)
                out_images = out_images[:,:,:,::-1]
                out_images = out_images.transpose(0, 3, 1, 2)
                out_images = out_images* 2 /255-1
                yield torch.from_numpy(out_images), torch.from_numpy(out_labels).long(), out_images_filename
                out_images = []
                out_labels = []
                out_images_filename = []

def val_data_generator( image_list, label_list, batch_size, out_size, height_crop_offset):
    """
    验证数据生成器
    :@param image_list: 图片文件的绝对地址
    :@param label_list: 标签文件的绝对地址
    :@param batch_size: 每批取多少张图片
    :@param image_size: 输出的图片尺寸
    :@param crop_offset: 在高度的方向上，将原始图片截掉多少
    """
    out_images = []
    out_labels = []
    out_images_filename = []
    while True:  # 每一轮验证都应该从头开始
        for i in range(len(image_list)):
            try:
                image = cv2.imread(image_list[i])
                label = cv2.imread( label_list[i], cv2.IMREAD_GRAYSCALE)
            except:
                continue
            if image is None or label is None:
                continue
            # crop & resize
            image, label = crop_resize_data(image, label, out_size, height_crop_offset)
            # encode
            label = encode_gray_label(label)

            out_images.append(image)
            out_labels.append(label)
            out_images_filename.append(image_list[i])
            if len(out_images) == batch_size:
                out_images = np.array(out_images, dtype=np.float32)
                out_labels = np.array(out_labels, dtype=np.int64)
                # 转换成RGB
                out_images = out_images[:, :, :, ::-1]
                # 维度改成 (n, c, h, w)
                out_images = out_images.transpose(0, 3, 1, 2)
                # 归一化 -1 ~ 1
                out_images = out_images*2/255 - 1
                yield torch.from_numpy(out_images), torch.from_numpy(out_labels).long(), out_images_filename
                out_images = []
                out_labels = []
                out_images_filename = []
            else:
                if len(out_images) > 0:  # 这个时候输出的图片数量必然小于batchsize，可以通过这个数量关系得知本轮遍历结束
                    out_images = np.array(out_images, dtype=np.float32)
                    out_labels = np.array(out_labels, dtype=np.int64)
                    # 转换成RGB
                    out_images = out_images[:, :, :, ::-1]
                    # 维度改成 (n, c, h, w)
                    out_images = out_images.transpose(0, 3, 1, 2)
                    # 归一化 -1 ~ 1
                    out_images = out_images * 2 / 255 - 1
                    yield torch.from_numpy(out_images), torch.from_numpy(out_labels).long(), out_images_filename
                    out_images = []
                    out_labels = []
                    out_images_filename = []
                else:
                    yield None, None, None

def decodePredicts(predicts, out_size, height_pad_offset, mode='gray'):
    predicts = torch.argmax(predicts, dim=1)
    n, h, w = predicts.shape
    predicts = predicts.view((n, -1))
    if mode == "gray":
        predicts = decode_gray_label(predicts)
        predicts = predicts.view((n, 1, h, w))
        c = 1
    else:
        raise ValueError('mode wrong.')

    dsize = (out_size[1] - height_pad_offset, out_size[0])
    outs = torch.zeros((n, c, out_size[1], out_size[0]), dtype=torch.int)
    outs[:, :, height_pad_offset:, :] = torch.nn.UpsamplingNearest2d(dsize)(predicts.float()).int()

    return outs


if __name__ == '__main__':
    import pandas as pd
    import os
    image_root = os.path.abspath(os.path.join(os.getcwd(), '../..'))
    print(image_root)
    image_root = image_root + '\lane_dataset\data_list'
    print(image_root)
    df_train = pd.read_csv(os.path.join(image_root,'train.csv'))
    df_train=df_train[0:5]
    print(df_train.size)
    print(df_train['image'])
    datas = train_data_generate(df_train['image'], df_train['label'], 2, (768,256), 690)
    print('111')
    for step, data in enumerate(datas, 0):
        image, label ,file= data
        # print(image)
        # print(label)
        print(file)

