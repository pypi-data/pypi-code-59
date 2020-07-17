from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import time
import threading
import os
import pandas
import config as cfg
from __future__ import print_function

def Start_Stream(self):
    print('starting websocket')
    self.WebSocketManager = BinanceWebSocketApiManager() #initiate api manager
    self.WebSocketManager.exchange = self.Market
    print('websocket created')

    #makes sure asset list is in string for subscription purposes
    i = 0
    if type(self.Assets) == list:
        for i in range(len(self.Assets)):
            self.Assets[i] = str(self.Assets[i])
            i += 1
    print('Opening streams..')
    print(type(self.Assets))
    self.WebSocketManager.create_stream(self.Resolution, self.Assets)
    print('Stream Opened')

    def print_stream_data_from_stream_buffer(WebSocketManager):
        print("waiting 1 seconds, then we start flushing the stream_buffer")
        time.sleep(1)
        print("now printing...")
        while True:
            if WebSocketManager.is_manager_stopping():
                exit(0)
            oldest_stream_data_from_stream_buffer = WebSocketManager.pop_stream_data_from_stream_buffer()
            if oldest_stream_data_from_stream_buffer is False:
                time.sleep(0.01)
            else:
                try:
                    print(oldest_stream_data_from_stream_buffer)
                except Exception:
                    # not able to process the data? write it back to the stream_buffer
                    WebSocketManager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)


    # start a worker process to process to move the received stream_data from the stream_buffer to a print function
    worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(self.WebSocketManager,))
    worker_thread.start()