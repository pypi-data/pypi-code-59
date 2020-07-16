from unittest import TestCase
from pathlib import Path

from mdocspoofer import FramesDir

class TestFramesDir(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frames = Path('..', 'example_data', 'frames')
        self.frames_tom1 = Path('tom', 'frames1')
        self.frames_tom2 = Path('tom', 'frames2')

    def test_framesdir(self):
        f = FramesDir(self.frames, dose_per_image=3)
        f.write()

    def test_tom(self):
        f = FramesDir(self.frames_tom1, dose_per_image=3)

