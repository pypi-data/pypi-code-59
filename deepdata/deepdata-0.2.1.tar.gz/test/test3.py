from deepdata import FashionMNIST, DataLoader
import deepdata.mirror.zh

dataset = FashionMNIST("data", download=True)
data_loader1 = DataLoader(dataset, batch_size=512, num_worker=4)
for images, labels in data_loader1:
    print(images.shape)

# from torch.utils.data import DataLoader
#
# data_loader2 = DataLoader(dataset, batch_size=512, num_workers=4)
# for images, labels in data_loader2:
#     print(images.shape)
