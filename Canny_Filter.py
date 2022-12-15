import cv2
import sys
import os

#ファイルパスを設定（現在未設定）
filepath = '/Users/k21097kk/Documents/GitHub/webimageproces02/Sample'
#ファイルパスからファイル名取得
#拡張子あり
inputname = os.path.basename(filepath)
#拡張子なし
inputname_without_jpg = os.path.splitext(os.path.basename(filepath))[0]

#'image.jpgを読み込む'
img = cv2.imread(inputname)

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# Canny : Canny法を用いて、エッジ検出を行う
img_Canny = cv2.Canny(img, 50, 100)
#output.jpgを出力
cv2.imwrite(inputname_without_jpg + '_Canny_Flter,jpg', img)