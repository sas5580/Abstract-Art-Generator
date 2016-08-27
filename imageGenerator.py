from PIL import Image, ImageDraw
from random import randint
from math import sin, cos, pi
from uuid import uuid1 as uuid
import os


def generate():
    width = 720
    height = 300
    white = (255, 255, 255)

    rexp = ["sin(pi*i/x)","cos(pi*i/x)"][randint(0,1)]
    gexp = ["cos((pi*i*j)/x)","sin((pi*i*j)/x)"][randint(0,1)]
    bexp = ["sin(pi*j/x)","cos(pi*j/x)"][randint(0,1)]
    tileSize = randint(2,5) 
    x = float([3,5,7,11,13,17,19,21][randint(0,7)]) 

    image = Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(image)

    for i in xrange(0,720,tileSize):
        for j in xrange(0,480,tileSize):
            r = int(eval(rexp)*1000%255)
            g = int(eval(gexp)*1000%255)
            b = int(eval(bexp)*1000%255)

            tileColor = "#"+hex(r)[2:].zfill(2)+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2)
            draw.rectangle([(i,j),(i+tileSize,j+tileSize)], tileColor, None)

    path = "static/img/"
    fileName = str(uuid().int)+".jpg"
    image.save(path+fileName, 'JPEG')

    return path+fileName

def getRandImage():
    imgs = [files for root, dirs, files in os.walk('.\\static\\img')][0]
    return "static/img/"+imgs[randint(0,len(imgs)-1)]

    

        

