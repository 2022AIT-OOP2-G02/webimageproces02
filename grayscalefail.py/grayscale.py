def grayscale():
    import cv2
    import numpy as np

    im = cv2.imread('lena.jpg')
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