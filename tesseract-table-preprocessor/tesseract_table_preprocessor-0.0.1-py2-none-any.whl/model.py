import torch
import torch.nn as nn
import torch.nn.functional as F


class ComboPool2d(nn.Module):
    def __init__(self):
        super(ComboPool2d, self).__init__()
        self.h5 = nn.AvgPool2d(kernel_size=(1, 5), padding=(0, 2), stride=1)
        self.h9 = nn.AvgPool2d(kernel_size=(1, 9), padding=(0, 4), stride=1)
        self.v5 = nn.AvgPool2d(kernel_size=(5, 1), padding=(2, 0), stride=1)
        self.v9 = nn.AvgPool2d(kernel_size=(9, 1), padding=(4, 0), stride=1)

    def forward(self, x):
        xh5 = self.h5(x[:, 0:3, :, :])
        xh9 = self.h9(x[:, 3:5, :, :])
        xv5 = self.v5(x[:, 5:8, :, :])
        xv9 = self.v9(x[:, 8:10, :, :])
        xid = x[:, 10:, :, :]
        return torch.cat([xh5, xh9, xv5, xv9, xid], dim=1)


class LineRemover(nn.Module):
    def __init__(self):
        super(LineRemover, self).__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            ComboPool2d(),
            nn.Conv2d(16, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            ComboPool2d(),
            nn.Conv2d(16, 16, kernel_size=1),
            nn.ReLU(),
            nn.Conv2d(16, 1, kernel_size=3, padding=1),
        )

    def forward(self, x):
        return self.layers(x)
