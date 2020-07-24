from os.path import join, abspath, dirname, basename, exists, isdir

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import cv2

from tesseract_table_preprocessor.model import LineRemover


THIS_DIR = dirname(abspath(__file__))


model = LineRemover()
model.load_state_dict(torch.load(join(THIS_DIR, 'state_dict.pt')))
model.eval()


def preprocess(image_path):
  def downsample(img):
    orig_h, orig_w = img.shape
    h = orig_h // 4
    w = orig_w // 4
    img = img[:4*h, :4*w]
    return img.reshape(h, 4, w, 4).min(axis=(1, 3))
  def read_img(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
  def save_img(img, path):
    cv2.imwrite(path, cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
  img = read_img(image_path)
  img = img[:4 * (img.shape[0] // 4), :4 * (img.shape[1] // 4)]
  nn_input = torch.from_numpy(np.float32(255 - downsample(img)) / 255.0).unsqueeze(0).unsqueeze(0)
  logits = model(nn_input)
  nn_output = (sigmoid(logits).squeeze(dim=0).squeeze(dim=0).detach().numpy() < 0.5)
  nn_output = np.stack([nn_output] * 4, axis=1)
  nn_output = np.stack([nn_output] * 4, axis=-1)
  nn_output = nn_output.reshape(nn_output.shape[0] * 4, nn_output.shape[2] * 4)
  result = 255 - (255 - img) * nn_output
  save_img(result, image_path)
