from deepdata.cifar import CIFAR10
from deepdata import MNIST, KMNIST, FashionMNIST, DataLoader
import deepdata.urls

# dataset = CIFAR10("data", download=True)

# dataset = MNIST("data", download=True)
dataset = FashionMNIST("data", download=True)
data_loader = DataLoader(dataset.train(), batch_size=32, num_worker=4)
for item in dataset:
    print(item)
