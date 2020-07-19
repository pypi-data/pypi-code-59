from os.path import dirname, abspath

from os.path import join as pjoin
import pandas as pd
import os
from sklearn.utils import shuffle
from tqdm import tqdm

"""
main
"""
if __name__ == '__main__':

    image_list = []
    label_list = []
    path_root = os.path.abspath(os.path.join(os.getcwd(),'..\..\lane_detection_data'))
    print(path_root)
    image_root = pjoin(path_root, 'Image_Data')
    label_root = pjoin(path_root, 'Gray_Label')
    for d2 in os.listdir(image_root):
        # Record001, ...
        d2_image_root = pjoin(image_root , d2)
        # print(d2_image_root)
        if not os.path.isdir(d2_image_root):
            continue
        d2_label_root = pjoin(label_root, +d2)
        # print(d2_label_root)

        for d3 in os.listdir(d2_image_root):
            # 'Camera 5', ...
            d3_image_root = pjoin(d2_image_root, d3)
            print(d3_image_root)
            if not os.path.isdir(d3_image_root):
                continue
            d3_label_root = pjoin(d2_label_root, d3)
            # print(d3_label_root)
            for file in os.listdir(d3_image_root):
                print(file)
                if not file.endswith('.jpg'):
                    continue
                label_file_name = file.replace('.jpg', '_bin.png')
                print(label_file_name)
                if not os.path.exists(pjoin(d3_label_root, label_file_name)):
                    continue
                image_list.append(pjoin(d3_image_root, file))
                label_list.append(pjoin(d3_label_root, label_file_name))
    print(len(image_list), len(label_list))
    df = pd.DataFrame({'image':image_list, 'label':label_list})
    df = shuffle(df)
    num_train = int(0.8 * len(df))
    df_train = df[0:num_train]
    df_val = df[num_train:]
    print('train:', len(df_train), ' val:', len(df_val))
    df_train.to_csv(pjoin('.', 'train.csv'), index=False)
    df_val.to_csv(pjoin('.', 'val.csv'), index=False)
