from tkinter import *
import numpy as np
import time
from math import *

root = Tk()
t = 0

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
        [cos(t), sin(t), 0, 0],
        [-sin(t), cos(t), sin(t), 0],
        [0, -sin(t), cos(t), 0],
        [350, 320, 0, 1]
    ])


    a = np.array([
        [-200, 150, 100, 1],
        [-25, -100, 100, 1],
        [150, 150, 100, 1],
        [-100, -75, -100, 1],
    ])
    a = a.dot(tr)



    canv.create_line(a[0][0], a[0][1], a[1][0], a[1][1], width=2)
    canv.create_line(a[1][0], a[1][1], a[2][0], a[2][1], width=2, fill="red")

    canv.create_line(a[0][0], a[0][1], a[3][0], a[3][1], width=2)
    canv.create_line(a[0][0], a[0][1], a[2][0], a[2][1], width=2)
    canv.create_line(a[1][0], a[1][1], a[3][0], a[3][1], width=2)
    canv.create_line(a[2][0], a[2][1], a[3][0], a[3][1], width=2)
    canv.update()
    time.sleep(0.01)

    t = t + 0.02
    canv.delete("all")
root.mainloop()