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

a = np.array([[100.5, 300.5, 1],
              [250.5, 600.5, 1],
              [410.5, 300.5, 1],
              [250.5, 150.5, 1]])
a = a.dot(tr)

canv.create_line(a[0][0], a[0][1], a[1][0], a[1][1], width=2)
canv.create_line(a[1][0], a[1][1], a[2][0], a[2][1], width=2)


canv.create_line(a[0][0], a[0][1], a[3][0], a[3][1], width=2)
canv.create_line(a[0][0], a[0][1], a[2][0], a[2][1], width=2, fill="red")
canv.create_line(a[1][0], a[1][1], a[3][0], a[3][1], width=2)
canv.create_line(a[2][0], a[2][1], a[3][0], a[3][1], width=2)

root.mainloop()

# a = np.array([[0, 0, 0, 1],
#               [300, 252, 50 , 1],
#               [275, 200, 50 , 1],
#               [400, 175, 50 , 1],
#               [425, 225, 50 ,1],
#
#               [300, 102, -50 ,1],
#               [275, 50, -50 ,1],
#               [400, 25, -50 ,1],
#               [425, 75, -50 ,1],
#
#               [307, 250, 50 ,1],
#               [285, 202, 50 ,1],
#               [395, 182, 50 ,1],
#               [417, 227, 50 ,1],
#
#               [307, 100, -50 ,1],
#               [285, 57, -50 ,1],
#               [395, 35, -50 ,1],
#               [417, 77, -50 ,1]])


# canv.create_line(a[1][0], a[1][1], a[2][0], a[2][1], width=2)
    # canv.create_line(a[2][0], a[2][1], a[3][0], a[3][1], width=2)
    # canv.create_line(a[3][0], a[3][1], a[4][0], a[4][1], width=2)
    #
    # canv.create_line(a[5][0], a[5][1], a[6][0], a[6][1], width=2)
    # canv.create_line(a[6][0], a[6][1], a[7][0], a[7][1], width=2)
    # canv.create_line(a[7][0], a[7][1], a[8][0], a[8][1], width=2)
    #
    # canv.create_line(a[1][0], a[1][1], a[5][0], a[5][1], width=2)
    # canv.create_line(a[2][0], a[2][1], a[6][0], a[6][1], width=2)
    # canv.create_line(a[3][0], a[3][1], a[7][0], a[7][1], width=2, fill='red')
    # canv.create_line(a[4][0], a[4][1], a[8][0], a[8][1], width=2)
    #
    # #
    # canv.create_line(a[9][0], a[9][1], a[10][0], a[10][1], width=2)
    # canv.create_line(a[10][0], a[10][1], a[11][0], a[11][1], width=2)
    # canv.create_line(a[11][0], a[11][1], a[12][0], a[12][1], width=2)
    #
    # canv.create_line(a[13][0], a[13][1], a[14][0], a[14][1], width=2)
    # canv.create_line(a[14][0], a[14][1], a[15][0], a[15][1], width=2)
    # canv.create_line(a[15][0], a[15][1], a[16][0], a[16][1], width=2)
    #
    # canv.create_line(a[9][0], a[9][1], a[13][0], a[13][1], width=2)
    # canv.create_line(a[10][0], a[10][1], a[14][0], a[14][1], width=2, fill='red')
    # canv.create_line(a[11][0], a[11][1], a[15][0], a[15][1], width=2)
    # canv.create_line(a[12][0], a[12][1], a[16][0], a[16][1], width=2)
    #
    # canv.create_line(a[9][0], a[9][1], a[1][0], a[1][1], width=2)
    # canv.create_line(a[12][0], a[12][1], a[4][0], a[4][1], width=2)
    # canv.create_line(a[11][0], a[11][1], a[12][0], a[12][1], width=2)
    # canv.create_line(a[13][0], a[13][1], a[5][0], a[5][1], width=2)
    # canv.create_line(a[16][0], a[16][1], a[8][0], a[8][1], width=2)

    # canv.create_line(a[4][0], a[4][1], a[5][0], a[5][1], width=2)
    # canv.create_line(a[5][0], a[5][1], a[6][0], a[6][1], width=2)
    # canv.create_line(a[6][0], a[6][1], a[7][0], a[7][1], width=2)
    #
    # canv.create_line(a[4][0], a[4][1], a[7][0], a[7][1], width=2)