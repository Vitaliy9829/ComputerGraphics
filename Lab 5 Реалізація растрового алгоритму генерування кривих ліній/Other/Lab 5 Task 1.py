from tkinter import *
import math

root = Tk()
canv = Canvas(root, width=1200, height=800)
canv.pack()

h = 250
k = 175
a = 150
b = 100
x = h - a
y = k
# canv.create_line(x, y, x+500,y+50)
def Elliptic(x):
    if (x <= h + a):
        y = k - (b / a) * math.sqrt(math.pow(a, 2) - math.pow((x - h), 2))
        canv.create_line(x, y,x+1000,y+50)
        y = k + (b / a) * math.sqrt(math.pow(a, 2) - math.pow((x - h), 2))
        canv.create_line(x, y, x+1000,y+50)
        x += 10
Elliptic(x)
canv.mainloop()