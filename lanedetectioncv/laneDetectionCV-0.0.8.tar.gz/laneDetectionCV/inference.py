from PIL import Image
import numpy as np
import torch
from .nets.deeplab import DeepLab
from .utils.data import decodePredicts
from torchvision import transforms


def infer(img, model_pt):
    device = torch.device('cuda')
    model = DeepLab(output_stride=16, num_classes=8)
    model.eval()

    model.load_state_dict(torch.load(model_pt))
    if torch.cuda.is_available():
        model = model.to(device)

    input_image = Image.open(img)
    preprocess = transforms.Compose([transforms.ToTensor()])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    if torch.cuda.is_available():
        input_batch = input_batch.cuda()
    predicts = model(input_batch)
    outs = decodePredicts(predicts, (1536, 512), 690)
    outs = outs.permute((0, 2, 3, 1).numpy().astype(np.uint8))

    return outs
