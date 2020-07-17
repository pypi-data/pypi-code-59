from typing import Set
import pathlib


LEGAL_VIDEO_FILE_EXTENSIONS: Set[str] = {".mp4", ".3gp", ".ogg", ".wmv", ".webm", ".flv", ".avi", ".mkv"}

def is_legal_video_file_name(file_name: str):
    return pathlib.Path(file_name).suffix.lower() in LEGAL_VIDEO_FILE_EXTENSIONS
