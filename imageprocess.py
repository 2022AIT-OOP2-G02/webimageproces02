#import sys
import time
#import logging
import os
import datetime
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from watchdog.events import RegexMatchingEventHandler

#grayscale('../GitHub/webimageproces02/input_image/')
#nitika

class MyFileWatchHandler(RegexMatchingEventHandler):
    def __init__(self, regexes):
        super().__init__(regexes=regexes)

    # ファイル作成時の動作
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print(f"{datetime.datetime.now()} {filename} created")
         # ファイル変更時の動作
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print(f"{datetime.datetime.now()} {filename} changed")

    # ファイル削除時の動作
    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print(f"{datetime.datetime.now()} {filename} deleted")

    # ファイル移動時の動作
    def on_moved(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print(f"{datetime.datetime.now()} {filename} moved")

if __name__ == "__main__":
    # 対象ディレクトリ
    DIR_WATCH = './input_image'
    # 対象ファイルパスのパターン
    PATTERNS = [r'^\.*\.txt$']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)

    event_handler = MyFileWatchHandler(PATTERNS)
    
    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
    #logging.basicConfig(level=logging.INFO,
      #                  format='%(asctime)s - %(message)s',
        #                datefmt='%Y-%m-%d %H:%M:%S')
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #event_handler = LoggingEventHandler()
    #observer = Observer()
    #observer.schedule(event_handler, path, recursive=True)
    #observer.start()
    #try:
    #    while True:
     #       time.sleep(1)
    #except KeyboardInterrupt:
    #    observer.stop()
    #observer.join()