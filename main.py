from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/address
@app.route('/display-images', methods=["GET"])
def address_get():
    files = os.listdir('./images/upload')
    print(files)
    return render_template("display-images.html", images=files)

# http://127.0.0.1:5000/
@app.route('/')
def index():
    pass

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(port=8888, debug=True)
