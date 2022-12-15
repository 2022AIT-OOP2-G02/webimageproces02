from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/address
@app.route('/display-images', methods=["GET"])
def address_get():
    type = request.args.get('type', None)
    if type == 'upload':
        folder_path = './static/images/upload'
        type_jp = 'アップロード画像'
    elif type == 'grayscale':
        folder_path = './static/images/grayscale'
        type_jp = 'グレースケール画像'
    else:
        return redirect('/display-images?type=upload')

    files = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]
    return render_template("display-images.html", images=files, type_jp=type_jp)

# http://127.0.0.1:5000/
@app.route('/')
def index():
    pass

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=8888, debug=True)
