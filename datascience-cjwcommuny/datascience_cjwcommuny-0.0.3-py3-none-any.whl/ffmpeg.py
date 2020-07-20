import ffmpeg
from dataclasses import dataclass

@dataclass
class VideoInfo:
    width: int
    height: int
    num_frames: int
    duration: float
    fps: float

    @staticmethod
    def from_video(filename: str) -> 'VideoInfo':
        probe = ffmpeg.probe(filename)
        video_probed = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
        return VideoInfo(
            width=int(video_probed['width']),
            height=int(video_probed['height']),
            num_frames=int(video_probed['nb_frames']),
            duration=float(video_probed['duration']),
            fps=int(video_probed['nb_frames']) / float(video_probed['duration'])
        )

