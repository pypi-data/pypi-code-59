# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from .intersect import intersection, get_interpolate


def draw_bbox(img_bgr, bbox, is_ratio=False, label='', color=(0, 255, 0), text_size=0.8, text_pos_bottom=True):
    font = cv2.FONT_HERSHEY_SIMPLEX
    left, top, right, bottom = bbox[:4]
    if is_ratio:
        height, width = img_bgr.shape[:2]
        left, right = [i * width for i in [left, right]]
        top, bottom = [i * height for i in [top, bottom]]
    left, top, right, bottom = [int(i) for i in [left, top, right, bottom]]
    confidience = ''
    if len(bbox) == 5 and bbox[4] > 0:
        confidience = '%.2f' % bbox[-1]

    cv2.rectangle(img_bgr, (left, top), (right, bottom), color, 2)
    if confidience or label:
        text = '%s %s' % (label, confidience)
        if text_pos_bottom:
            pos = (max(0, left + 2 * len(text)), max(0, bottom - 2))
        else:
            pos = (max(0, left + 2 * len(text)), max(0, top + 2))

        # cv2.rectangle(img_bgr, (pos[0], bottom - 12), (right, bottom), color, 2)
        cv2.putText(img_bgr, text, pos, font, text_size, color, 2)

    return img_bgr


def draw_landmark(img_bgr, landmarks, is_ratio=False, color=(0, 255, 255), draw_order=False):
    height, width = img_bgr.shape[:2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    nrof_landmark = len(landmarks)
    if not nrof_landmark:  # no landmarks
        return img_bgr

    for i in range(nrof_landmark):
        pos = np.squeeze(landmarks[i,])
        if is_ratio:
            pos = (width * pos[0], height * pos[1])
        pos = tuple([int(p) for p in pos])
        cv2.circle(img_bgr, pos, 3, color, -1)
        # check landmarks order
        if draw_order:
            cv2.putText(
                img_bgr, '%d' % i, (pos[0] - 2, pos[1] - 2), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    return img_bgr


def view_image(img_bgr, name='image', position_x=0, position_y=0, win_width=960, win_height=640):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, (win_width, win_height))
    cv2.moveWindow(name, position_x, position_y)
    cv2.imshow(name, img_bgr)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        sys.exit(-1)


def plot_roc(threshold_li, precision_li, recall_li, save_path='', block=False, figsize=(16, 9), target_precision=0.9,
             title='Similarity', draw_hline=False, acc_li=None):
    plt.figure(figsize=figsize)
    if draw_hline:
        plt.axhline(y=target_precision, color='g', linestyle='-')

    plt.plot(threshold_li, precision_li, label='precision')
    plt.plot(threshold_li, recall_li, label='recall')
    if acc_li is not None:
        plt.plot(threshold_li, acc_li, label='accuracy')

    stats_li = []
    header = ['threshold', 'precision', 'recall']
    xs, ys = intersection(np.array(threshold_li), np.array(recall_li), np.array(threshold_li), np.array(precision_li))
    if len(xs) and len(ys) and ys[0] >= target_precision:
        stats_li.append([xs[0], ys[0], ys[0]])
        plt.plot([xs[0]], [ys[0]], marker='*', c='black')
        plt.text(xs[0], ys[0], '(%.3f, %.5f)' % (xs[0], ys[0]), fontsize=12)
    else:
        xy0 = get_interpolate(threshold_li, precision_li, target_precision)  ### get threshold when precision@0.9
        xy1 = tuple(reversed(get_interpolate(recall_li, threshold_li, xy0[0])))
        stats_li.append([xy0[0], xy0[1], xy1[1]])  ### thresh, pre, rec
        plt.text(xy0[0], xy0[1], '(%.3f, %.5f)' % (xy0[0], xy0[1]), fontsize=12)
        plt.text(xy1[0], xy1[1], '(%.3f, %.5f)' % (xy1[0], xy1[1]), fontsize=12)

    plt.xlabel('Distance threshold')
    plt.ylabel('Precision and recall')
    max_thresh = np.max(threshold_li)
    plt.xlim(0, max_thresh + 0.01)
    plt.ylim(0, 1.01)

    plt.xticks(np.arange(0, max_thresh + 0.01, 0.01), rotation=90)
    plt.yticks(np.arange(0, 1.01, 0.02))
    plt.title('Precision and recall for %s' % (title))
    plt.legend()  # loc=8, prop={'size': 12})
    plt.grid(which='both')

    if save_path:
        plt.savefig(save_path)
        print('Saving to ', save_path)
    plt.show(block=block)

    stats_df = pd.DataFrame(stats_li, columns=header, index=None)
    return stats_df
