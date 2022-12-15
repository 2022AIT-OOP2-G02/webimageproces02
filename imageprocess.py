import sys
import time
import logging
import cv2
import sys
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

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
if __name__ == "__main__":
    Canny_imagecreate('input_image/camera_capture.png')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
