import numpy as np
from typing import Tuple

from cv2 import VideoCapture
import cv2


def put_label(
        image: np.ndarray,
        text: str,
        position: Tuple[int, int],
        font_face: int,
        font_scale: float,
        font_thickness: int=1,
        alpha: float=0.5,
        text_color: Tuple[int, int, int]=(0, 0, 0),
        background_color: Tuple[int, int, int]=(255, 255, 255)
) -> np.ndarray:
    """
    put a label in an image, with background
    """
    overlay = image.copy()
    (text_width, text_height) = cv2.getTextSize(
        text, font_face, fontScale=font_scale, thickness=font_thickness
    )[0]
    box_coords = (
        (int(position[0]), int(position[1])),
        (int(position[0] + text_width + 2), int(position[1] - text_height - 2))
    )
    cv2.rectangle(overlay, box_coords[0], box_coords[1], background_color, cv2.FILLED)
    image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    cv2.putText(
        image, text, position, font_face, fontScale=font_scale, color=text_color, thickness=font_thickness
    )
    return image


def opencv_image_to_pil_image(image: np.ndarray):
    """
    :param image:
        image = cv2.imread("path/to/img.png")
    :return:
    """
    from PIL import Image
    import cv2
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image)


def get_fps(video: VideoCapture) -> float:
    return video.get(cv2.CAP_PROP_FPS)

def get_duration(video: VideoCapture) -> float:
    return video.get(cv2.CAP_PROP_FRAME_COUNT)


class VideoCaptureIter:
    def __init__(self, video: cv2.VideoCapture):
        self.video = video

    def __iter__(self):
        return self

    def __next__(self) -> np.ndarray:
        """
        :return: shape=(height, width, channel=3), format=BGR
        """
        return_val, frame = self.video.read()
        if not return_val:
            raise StopIteration()
        return frame



