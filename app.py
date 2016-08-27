from flask import Flask, render_template, request, jsonify
from imageGenerator import *

app = Flask(__name__)

@app.route('/')
def index(go=None):
    imgId  = generate()
    return render_template("index.html", imgUrl =imgId)

@app.route('/_new_art')
def new_art():
    imgId = generate()
    return jsonify(url = imgId)

if __name__ == "__main__":    
    app.run(host="0.0.0.0")
