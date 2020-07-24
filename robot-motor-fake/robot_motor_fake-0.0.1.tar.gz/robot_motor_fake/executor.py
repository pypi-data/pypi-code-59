import cv2
from robot_core.executor.executor import Executor


class FakeMotorExecutor(Executor):
    # Start Capture
    cap = cv2.VideoCapture(0)

    # Get frame dimensions
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def execute(self, **kwargs):
        if kwargs["command"] == "forward":
            return self.forward()
        elif kwargs["command"] == "backward":
            return self.backward()
        elif kwargs["command"] == "right":
            return self.right()
        elif kwargs["command"] == "left":
            return self.left()

    def forward(self):
        x = 50
        y = 50
        img = cv2.imread('forward.png')
        img_height, img_width, _ = img.shape
        ret, frame = self.cap.read()
        frame[y:y + img_height, x:x + img_width] = img
        return frame

    def backward(self):
        self.vs.stop()

    def right(self):
        return self.vs.read()

    def left(self):
        return self.vs.read()

