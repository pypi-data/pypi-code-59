#  Copyright (c) intmain 2020.

import sys
from queue import Queue


class Redirection:
    def __init__(self, buffer_size=512):
        self.buffer = Queue(maxsize=512)
        self._console = sys.stdout
        # 自定义的输出端
        self.custom = None

    def write(self, output_stream):
        # 加入缓冲区队列
        self.buffer.put(output_stream)

    def to_console(self):
        sys.stdout = self._console
        # 出列
        while not self.buffer.empty():
            print(self.buffer.get())

    def to_file(self, file_path):
        with open(file_path, 'w+') as f:
            sys.stdout = f
            while not self.buffer.empty():
                print(self.buffer.get())
            f.close()

    def to_custom(self):
        while not self.buffer.empty():
            self.custom(self.buffer.get())

    def to_list(self):
        data = []
        while not self.buffer.empty():
            data.append(self.buffer.get())
        return data

    def flush(self):
        self.buffer.empty()

    def reset(self):
        sys.stdout = self._console
