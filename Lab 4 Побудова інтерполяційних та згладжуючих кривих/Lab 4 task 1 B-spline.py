from tkinter import *
import numpy as np
import time
from math import *

root = Tk()
canv = Canvas(root, width=1200, height=800)
# координатні осі x, y
canv.create_line(500, 0, 500, 1000, width=2, arrow=LAST)  # x
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)  # y

for t in range(-500, 500, 50):
    k = t - 0
    canv.create_line(t + 500, 500, t + 500, 510, width=1, fill='black')
    canv.create_text(t + 500, 515, text=str(k), fill="purple", font=("Arial", "10"))
for t in range(1000, 0, -50):
    k = t - 0
    if (k != 0):
        canv.create_line(490, t, 500, t, width=1, fill='black')
        canv.create_text(480, t, text=str(-k + 500), fill="purple", font=("Arial", "10"))
canv.pack()

# Радіус "точок"
eps = 5


def N0(t):
    return ((1 - t) * (1 - t) * (1 - t)) / 6


def N1(t):
    return (3 * t * t * t - 6 * t * t + 4) / 6


def N2(t):
    return (-3 * t * t * t + 3 * t * t + 3 * t + 1) / 6


def N3(t):
    return (t * t * t) / 6
# def N4(t):
#     return t * 0


def line(x1, y1, x2, y2, row):
    h, w = 500, 500
    if row == 1:
        canv.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            fill='red'
        )
    else:
        canv.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            dash=(2, 4)
        )


def Oval(x1, y1, x2, y2):
    h, w = 500, 500
    canv.create_oval(
        x1 + w, h - y1,
        x2 + w, h - y2,
    )


# Задаємо початкові значення
pX = np.zeros(5)
pY = np.zeros(5)
pX[0] = 0 * 200
pY[0] = 66 * 2
pX[1] = 0.45 * 200
pY[1] = 44 * 2
pX[2] = 0.9 * 200
pY[2] = 119 * 2
pX[3] = 1.35 * 200
pY[3] = 63 * 2

pX[4] = 1.8 * 200
pY[4] = 10 * 2

m = 5
i = 0
while ((m - i) > 3):
    Oval(pX[i+0]-eps,pY[i+0]-eps,pX[i+0]+eps,pY[i+0]+eps)
    Oval(pX[i+1]-eps,pY[i+1]-eps,pX[i+1]+eps,pY[i+1]+eps)
    Oval(pX[i+2]-eps,pY[i+2]-eps,pX[i+2]+eps,pY[i+2]+eps)
    Oval(pX[i+3]-eps,pY[i+3]-eps,pX[i+3]+eps,pY[i+3]+eps)

    line(pX[i+0],pY[i+0],pX[i+1],pY[i+1],0)
    line(pX[i+1],pY[i+1],pX[i+2],pY[i+2],0)
    line(pX[i+2],pY[i+2],pX[i+3],pY[i+3],0)
    line(pX[i+3],pY[i+3],pX[i+1],pY[i+1],0)

    line(pX[i+0],pY[i+0],pX[i+2],pY[i+2],0)
    t = 0
    dt = 0.0001
    while t <= 1:
        x = pX[i + 0] * N0(t) + pX[i + 1] * N1(t) + pX[i + 2] * N2(t) + pX[i + 3] * N3(t) #+ pX[i + 4] * N4(t)
        y = pY[i + 0] * N0(t) + pY[i + 1] * N1(t) + pY[i + 2] * N2(t) + pY[i + 3] * N3(t) #+ pY[i + 4] * N4(t)
        t = t + dt
        xdt = pX[i + 0] * N0(t) + pX[i + 1] * N1(t) + pX[i + 2] * N2(t) + pX[i + 3] * N3(t) #+ pX[i + 4] * N4(t)
        ydt = pY[i + 0] * N0(t) + pY[i + 1] * N1(t) + pY[i + 2] * N2(t) + pY[i + 3] * N3(t) #+ pY[i + 4] * N4(t)
        line(x, y, xdt, ydt, 1)
    i = i + 1
root.mainloop()
