# webimageproces02

# 仕様
- 取り扱う画像はjpegファイル
- アップロード画像、グレースケール化、輪郭抽出を表示する
- アップロードした画像は`static/images/upload/`、グレースケールした画像は`static/images/grayscale/`に保存
- Python3.10.6
- OpenCV
- Watchdog

# 動作確認
- webはアップロード、一覧表示まで動作確認済み(main.py)
- 画像処理は輪郭抽出、グレースケール化、２値化はそれぞれ動作済み、watchdogによるファイルの受け取り、受け渡しが未完成
