from Tkinter import *
from random import randint
from math import sin,cos,pi


master = Tk()
        
w = Canvas(master, width=720, height=480)
w.pack()


rexp = ["sin(pi*i/x)","cos(pi*i/x)"][randint(0,1)]
gexp = ["cos((pi*i*j)/x)","sin((pi*i*j)/x)"][randint(0,1)]
bexp = ["sin(pi*j/x)","cos(pi*j/x)"][randint(0,1)]
sz = randint(2,5) 
x = float([3,5,7,11,13,17,19,21][randint(0,7)]) 

"""
sz=4
x=1
"""

for i in xrange(0,720,sz):
    for j in xrange(0,480,sz):
        r = int(eval(rexp)*1000%255) #int(sin(pi*i/x)*1000%255)
        g = int(eval(gexp)*1000%255) #int(cos((pi*i*j)/x)*1000%255)
        b = int(eval(bexp)*1000%255) #int(sin(pi*j/x)*1000%255)

        """
        r = int(sin(pi*i/x)*1000%255)
        g = int(cos((pi*i*j)/x)*1000%255)
        b = int(sin(pi*j/x)*1000%255)
        """
        cl = "#"+hex(r)[2:].zfill(2)+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2)       
        w.create_rectangle(i,j,i+sz,j+sz,fill=cl,outline=cl)


w.postscript('image.ps')
mainloop()

