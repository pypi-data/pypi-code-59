import os

import cv2

from deepdata import Dataset, DataLoader
import deepdata.transforms as transforms


class CSVImageFolder(Dataset):
    def __init__(self, data_dir, csv_file, img_dir=None, transform=None, sep="\t", encoding="utf8"):
        self.data_dir = data_dir
        self.csv_file = csv_file
        self.transform = transform
        if img_dir is not None:
            if not os.path.isabs(img_dir):
                img_dir = os.path.join(data_dir, img_dir)
            self.img_dir = img_dir
        else:
            self.img_dir = data_dir

        self.csv_data = self.load_csv(csv_file, sep=sep, encoding=encoding)

    def load_csv(self, file_path, sep, encoding):
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.data_dir, file_path)

        ls = []
        with open(file_path, "r", encoding=encoding) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue

                ss = list(line.split(sep))
                if len(ss) > 1:
                    ss[1] = int(ss[1])
                ls.append(ss)
        return ls

    def __len__(self):
        return len(self.csv_data)

    def __getitem__(self, index):
        img, label = self.csv_data[index]
        if not os.path.isabs(img):
            img = os.path.join(self.img_dir, img)

        img = cv2.imread(img)
        if self.transform:
            img = self.transform(img)

        return img, label


if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.Normalize(0, 255)
    ])

    my_dataset = CSVImageFolder("/home/killf/dlab/paddle_caltech101/data", "Train.txt", img_dir="Images",
                                transform=transform)
    my_loader = DataLoader(my_dataset, shuffle=True)
    for img, label in my_loader:
        print(img.shape)
        pass
