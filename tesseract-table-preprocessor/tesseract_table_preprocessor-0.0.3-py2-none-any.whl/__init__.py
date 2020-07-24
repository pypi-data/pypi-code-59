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


def detect_lines_using_opencv(img):
  gray = 255 - img
  dilated = cv2.dilate(gray, np.ones((5, 1), np.uint8))
  horizontal_lines = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, np.ones((1, 101), np.uint8))
  horizontal_lines = np.uint8(255 * (horizontal_lines >= 150))
  #horizontal_lines = cv2.erode(horizontal_lines, np.ones((3, 1), np.uint8))

  dilated = cv2.dilate(gray, np.ones((1, 5), np.uint8))
  vertical_lines = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, np.ones((91, 1), np.uint8))
  vertical_lines = np.uint8(255 * (vertical_lines >= 150))
  #vertical_lines = cv2.erode(vertical_lines, np.ones((1, 3), np.uint8))

  return np.maximum(horizontal_lines, vertical_lines)


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
  sigmoid = nn.Sigmoid()
  img = read_img(image_path)
  img = img[:4 * (img.shape[0] // 4), :4 * (img.shape[1] // 4)]
  nn_input = torch.from_numpy(np.float32(255 - downsample(img)) / 255.0).unsqueeze(0).unsqueeze(0)
  logits = model(nn_input)
  nn_output = (sigmoid(logits).squeeze(dim=0).squeeze(dim=0).detach().numpy() < 0.5)
  nn_output = np.stack([nn_output] * 4, axis=1)
  nn_output = np.stack([nn_output] * 4, axis=-1)
  nn_output = nn_output.reshape(nn_output.shape[0] * 4, nn_output.shape[2] * 4)
  result = 255 - (255 - img) * nn_output
  result = np.maximum(result, detect_lines_using_opencv(img))
  save_img(result, image_path)
