import numpy as np
import cv2
import torch


def encode_gray_label(labels):
    """
    标签图转换成类型id
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
    encoded_labels[labels == 224] = 6
    encoded_labels[labels == 225] = 6
    encoded_labels[labels == 226] = 6
    # 7
    encoded_labels[labels == 205] = 7
    encoded_labels[labels == 227] = 7
    encoded_labels[labels == 250] = 7
    return encoded_labels


def decode_gray_label(labels):
    decoded_labels = torch.zeros(labels.size(), dtype=torch.int)
    decoded_labels[labels == 1] = 204
    decoded_labels[labels == 2] = 203
    decoded_labels[labels == 3] = 217
    decoded_labels[labels == 4] = 210
    decoded_labels[labels == 5] = 214
    decoded_labels[labels == 6] = 224
    decoded_labels[labels == 7] = 227
    return decoded_labels


def crop_resize_data(image, label, out_size, height_crop_offset):
    roi_image = image[height_crop_offset:]
    roi_image = cv2.resize(roi_image, out_size, interpolation=cv2.INTER_LINEAR)
    if label is not None:
        roi_label = label[height_crop_offset:]
        roi_label = cv2.resize(roi_label, out_size, interpolation=cv2.INTER_NEAREST)
    else:
        roi_label = None
    return roi_image, roi_label


def train_data_generator(image_path_list, label_path_list, batch_size, out_size, height_crop_offset):
    indices = np.arange(0, len(image_path_list))
    out_images = []
    out_labels = []
    while True:
        np.random.shuffle(indices)
        for i in indices:
            try:
                image = cv2.imread(image_path_list[i])
                label = cv2.imread(label_path_list[i], cv2.IMREAD_GRAYSCALE)
            except:
                continue
            image, label = crop_resize_data(image, label, out_size, height_crop_offset)
            label = encode_gray_label(label)

            out_images.append(image)
            out_labels.append(label)
            if len(out_images) == batch_size:
                out_images = np.array(out_images, dtype=np.float32)
                out_labels = np.array(out_labels, dtype=np.int64)
                # RGB
                out_images = out_images[:, :, :, ::-1]
                # (N,C,H,W)
                out_images = out_images.transpose(0, 3, 2, 1)
                # normalize
                out_images = out_images * 2 / 255 - 1
                yield torch.from_numpy(out_images), torch.from_numpy(out_labels).long()
                out_images = []
                out_labels = []


def val_data_generator(img_path, label_path, batch_size, out_size, height_crop_offset):
    out_images = []
    out_labels = []
    out_images_filename = []
    while True:
        for i in range(len(img_path)):
            try:
                img = cv2.imread(img_path[i])
                label = cv2.imread(label_path[i], cv2.IMREAD_GRAYSCALE)
            except:
                continue

            img, label = crop_resize_data(img, label, out_size, height_crop_offset)
            label = encode_gray_label(label)

            out_images.append(img)
            out_labels.append(label)
            if len(out_images) == batch_size:
                out_images = np.array(out_images, dtype=np.float32)
                out_labels = np.array(out_labels, dtype=np.int64)
                out_images = out_images[:, :, :, ::-1]
                out_images = out_images.transpose(0, 3, 1, 2)
                out_images = out_images * 2 / 255 - 1
                yield torch.from_numpy(out_images), torch.from_numpy(out_labels).long()
                out_images = []
                out_labels = []


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
