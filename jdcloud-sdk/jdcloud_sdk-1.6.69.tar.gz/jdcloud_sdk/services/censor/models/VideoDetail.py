# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class VideoDetail(object):

    def __init__(self, audio_time=None, politics_frame_count=None, porn_frame_count=None, terrorism_frame_count=None, total_frame_count=None):
        """
        :param audio_time: (Optional) 音频识别总时长
        :param politics_frame_count: (Optional) 涉政截帧数
        :param porn_frame_count: (Optional) 涉黄截帧数
        :param terrorism_frame_count: (Optional) 暴恐截帧数
        :param total_frame_count: (Optional) 总截帧数
        """

        self.audio_time = audio_time
        self.politics_frame_count = politics_frame_count
        self.porn_frame_count = porn_frame_count
        self.terrorism_frame_count = terrorism_frame_count
        self.total_frame_count = total_frame_count
