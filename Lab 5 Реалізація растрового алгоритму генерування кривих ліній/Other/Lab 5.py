from PIL import Image
from tkinter import *
import math

root = Tk()
canv = Canvas(root, width=1200, height=800)
canv.pack()
# def Line_1 (x1, y1, x2, y2, c):
#     a = ((y2-y1) / (x2-x1))
#     b = (y1 - a*x1)
#     for x in range(x1, x2):
#         Image.putpixel(x, (a * x + b), c)
A = 150
B = 100
K = 500
H = 500
x = H - A - 1
# y = K

def Line_2 (x, c):
    # a = (y2 - y1) / (x2 - x1)
    # y = y1
    # for q in range(x1,x2):
    while(x <= H + A):
        y = K - (B / A) * math.sqrt(math.pow(A, 2) - math.pow((x - H), 2))
        canv.create_line(x, y, x+1, y, fill=c)
        x = x + 1
        # x = math.sqrt(math.fabs((1 - (y * y) / (B * B)) * (A * A)))

        # x = math.sqrt(math.fabs((1 - (y*y)/(B*B))*(A*A)))
        # canv.create_line(x, y, x, y+1,fill= c)
        # y = y + 1
# Line_1(34,24,53,23,5)
Line_2(x,"black")
canv.mainloop()