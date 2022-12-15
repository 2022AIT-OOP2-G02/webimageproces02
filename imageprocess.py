#import sys
import time
import logging
import cv2
import sys
import os
import datetime

from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler


def Canny_imagecreate(filepath):
    #ファイルパスからファイル名取得
    #拡張子なし
    inputname_without_jpg = os.path.splitext(os.path.basename(filepath))[0]

    #'image.jpgを読み込む'
    img = cv2.imread(filepath)

    # 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
    if img is None:
        sys.exit("Could not read the image.")
    # Canny : Canny法を用いて、エッジ検出を行う
    img_Canny = cv2.Canny(img, 50, 100)
    #output.jpgを出力
    cv2.imwrite(inputname_without_jpg + '_Canny_Flter.jpg', img_Canny)

def grayscale(filepath):
    import cv2
    import numpy as np
    im = cv2.imread(filepath)
    print(im.shape)
    # (225, 400, 3)

    print(im.dtype)
    # uint8

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    print(im_gray.shape)
    # (225, 400)

    print(im_gray.dtype)
    # uint8

    cv2.imwrite('opencv_gray_cvtcolr.jpg', im_gray)

def nitika(filepath):
    import cv2

    im = cv2.imread(filepath)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

    print(th)
    # 117.0

    cv2.imwrite('opencv_th_otsu.jpg', im_gray_th_otsu)

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

    grayscale('input_image/lena.jpg')
    Canny_imagecreate('input_image/camera_capture.png')
    
    
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
