def nitika(filepath):
    import cv2

    im = cv2.imread(filepath)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

    print(th)
    # 117.0

    cv2.imwrite('opencv_th_otsu.jpg', im_gray_th_otsu)