
#%%
import torch
import torch.nn as nn
import torch.functional as F

# %%
class TensorType():
    def __init__(self, shape=None, transforms=[], 
    to_batch=False, device=None, from_single_value=False,
    random_values=False, to_numpy=False, detach=False,
    first_pipeline=None, second_pipeline=None):
        self.shape = shape
        self.transforms = transforms
        self.to_batch = to_batch
        self.device = device
        self.detach = detach
        self.to_numpy = to_numpy
        self.from_single_value = from_single_value
        self.random_values = random_values
        self.FirstPipeline = first_pipeline; self.SecondPipeline = second_pipeline
    def __lshift__(self, x):
        if self.FirstPipeline is not None and self.SecondPipeline is not None:
            x = self.FirstPipeline.__lshift__(x)
            x = self.SecondPipeline.__lshift__(x)
            return x
        if self.from_single_value:
            x = torch.ones(self.shape) * x
        if self.random_values:
            x = torch.rand(self.shape) * x
        if self.shape is not None:
            x = x.view(self.shape)
        if self.to_batch:
            x = x.unsqueeze(0)
        if self.detach:
            x = x.detach()
        if self.device is not None:
            x = x.to(self.device)
        if self.to_numpy:
            x = x.numpy()
        for t in self.transforms:
            x = t(x)
        return x
    def __add__(self, other):
        return TensorType(first_pipeline=self, second_pipeline=other)

#%%
my_type = TensorType(shape=(3, 100), from_single_value=True)
my_other_type = TensorType(to_batch=True)
my_test_input = my_type + my_other_type

# %%
