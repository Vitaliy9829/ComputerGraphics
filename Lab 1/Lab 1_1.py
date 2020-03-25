from tkinter import *
import numpy as np
from random import *
from math import *

root = Tk()
m = 1
X = 0
Y = 0

canv = Canvas(root, width=1200, height=1000)
# координатні осі x, y
canv.create_line(10, 0, 10, 1000, width=2, arrow=LAST)  # x
canv.create_line(0, 10, 1000, 10, width=2, arrow=LAST)  # y

for t in range(0, 1000, 50):
    k = t - 0
    canv.create_line(t, 5, t, 15, width=1, fill='black')
    canv.create_text(t + 15, 25, text=str(k), fill="purple", font=("Arial", "10"))
    if (k != 0):
        canv.create_line(5, t, 15, t, width=1, fill='black')
        canv.create_text(25, t, text=str(k), fill="purple", font=("Arial", "10"))

canv.pack()

tr = np.array([[m, 0, 0],
               [0, m, 0],
               [0, 0, 0]])

a = np.array([[X, Y, 1],
              [600.5, 505.5, 1],
              [550.5, 400.5, 1],
              [800.5, 350.5, 1],
              [850.5, 450.5, 1],

              [600.5, 205.5, 1],
              [550.5, 100.5, 1],
              [800.5, 50.5, 1],
              [850.5, 150.5, 1],

              [615.5, 500.5, 1],
              [568.5, 410.5, 1],
              [788.5, 365.5, 1],
              [835.5, 455.5, 1],

              [615.5, 200.5, 1],
              [570.5, 115.5, 1],
              [788.5, 70.5, 1],
              [835.5, 155.5, 1]])

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
canv.create_line(a[10][0], a[10][1], a[14][0], a[14][1], width=2,  fill='red')
canv.create_line(a[11][0], a[11][1], a[15][0], a[15][1], width=2)
canv.create_line(a[12][0], a[12][1], a[16][0], a[16][1], width=2)

canv.create_line(a[9][0], a[9][1], a[1][0], a[1][1], width=2)
canv.create_line(a[12][0], a[12][1], a[4][0], a[4][1], width=2)
canv.create_line(a[11][0], a[11][1], a[12][0], a[12][1], width=2)
canv.create_line(a[13][0], a[13][1], a[5][0], a[5][1], width=2)
canv.create_line(a[16][0], a[16][1], a[8][0], a[8][1], width=2)
root.mainloop()