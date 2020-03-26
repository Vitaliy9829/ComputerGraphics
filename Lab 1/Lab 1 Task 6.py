from tkinter import *
import numpy as np
import time
from math import *

root = Tk()
t = 0
m = 1
X = 200
Y = 100

canv = Canvas(root, width=1200, height=800)
canv.pack()


while True:
    canv.create_line(0, 10, 1200, 10, width=2, arrow=LAST)  # x
    canv.create_line(10, 0, 10, 600, width=2, arrow=LAST)  # y
    for p in range(0, 1100, 50):
        k = p - 0
        canv.create_line(p, 5, p, 15, width=1, fill='black')
        canv.create_text(p + 15, 25, text=str(k), fill="purple", font=("Arial", "10"))
    for p in range(0, 600, 50):
        k = p - 0
        canv.create_line(5, p, 15, p, width=1, fill='black')
        canv.create_text(25, p, text=str(k), fill="purple", font=("Arial", "10"))

    tr = np.array([
        [m, 0, 0],
        [0, m, 0],
        [X*cos(t),Y*sin(t), 1]
    ])

    a = np.array([[0, 0, 1],
                  [300, 452, 1],
                  [275, 400, 1],
                  [400, 375, 1],
                  [425, 425, 1],

                  [300, 302, 1],
                  [275, 250, 1],
                  [400, 225, 1],
                  [425, 275, 1],

                  [307, 450, 1],
                  [285, 402, 1],
                  [395, 382, 1],
                  [417, 427, 1],

                  [307, 300, 1],
                  [285, 257, 1],
                  [395, 235, 1],
                  [417, 277, 1]])

    a = a.dot(tr)

    canv.create_line(a[1][0], a[1][1], a[2][0], a[2][1], width=2)
    canv.create_line(a[2][0], a[2][1], a[3][0], a[3][1], width=2)
    canv.create_line(a[3][0], a[3][1], a[4][0], a[4][1], width=2)

    canv.create_line(a[5][0], a[5][1], a[6][0], a[6][1], width=2)
    canv.create_line(a[6][0], a[6][1], a[7][0], a[7][1], width=2)
    canv.create_line(a[7][0], a[7][1], a[8][0], a[8][1], width=2)

    canv.create_line(a[1][0], a[1][1], a[5][0], a[5][1], width=2)
    canv.create_line(a[2][0], a[2][1], a[6][0], a[6][1], width=2)
    canv.create_line(a[3][0], a[3][1], a[7][0], a[7][1], width=2, fill='red')
    canv.create_line(a[4][0], a[4][1], a[8][0], a[8][1], width=2)

    #
    canv.create_line(a[9][0], a[9][1], a[10][0], a[10][1], width=2)
    canv.create_line(a[10][0], a[10][1], a[11][0], a[11][1], width=2)
    canv.create_line(a[11][0], a[11][1], a[12][0], a[12][1], width=2)

    canv.create_line(a[13][0], a[13][1], a[14][0], a[14][1], width=2)
    canv.create_line(a[14][0], a[14][1], a[15][0], a[15][1], width=2)
    canv.create_line(a[15][0], a[15][1], a[16][0], a[16][1], width=2)

    canv.create_line(a[9][0], a[9][1], a[13][0], a[13][1], width=2)
    canv.create_line(a[10][0], a[10][1], a[14][0], a[14][1], width=2, fill='red')
    canv.create_line(a[11][0], a[11][1], a[15][0], a[15][1], width=2)
    canv.create_line(a[12][0], a[12][1], a[16][0], a[16][1], width=2)

    canv.create_line(a[9][0], a[9][1], a[1][0], a[1][1], width=2)
    canv.create_line(a[12][0], a[12][1], a[4][0], a[4][1], width=2)
    canv.create_line(a[11][0], a[11][1], a[12][0], a[12][1], width=2)
    canv.create_line(a[13][0], a[13][1], a[5][0], a[5][1], width=2)
    canv.create_line(a[16][0], a[16][1], a[8][0], a[8][1], width=2)

    canv.update()
    time.sleep(0.001)
    t = t + 0.015

    if t >= 2:
        m -= 0.002
        if t >= 4:
            m += 0.0038
            if t >= 6.25:
                t = 0
                m = 1


    canv.delete("all")
root.mainloop()