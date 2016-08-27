from flask import Flask, render_template, request, jsonify
from imageGenerator import *

app = Flask(__name__)

@app.route('/')
def index(go=None):       
    return render_template("index.html", imgUrl = getRandImage())

@app.route('/_new_art')
def new_art():
    imgId = generate()
    return jsonify(url = imgId)

if __name__ == "__main__":    
    app.run()
