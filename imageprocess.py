import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
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

if __name__ == "__main__":
    grayscale('input_image/lena.jpg')
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