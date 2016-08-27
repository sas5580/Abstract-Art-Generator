from flask import Flask, render_template, request, Response
from imageGenerator import *

app = Flask(__name__)

@app.route('/')
@app.route('/<go>')
def index(go=None):
    imgId = None
    if go:        
        imgId = generate()     
        
    return render_template("index.html", imgUrl = imgId if imgId else getRandImage())

if __name__ == "__main__":    
    app.run()
