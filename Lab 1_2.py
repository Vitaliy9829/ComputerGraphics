from tkinter import *
import numpy as np
import time
from random import *
from math import *

m = 0.2
x0 = 500
y0 = 500
x = 0
y = 0
colors = ['red','green','blue', 'yellow','brown']

Q = 1

root = Tk()
canv = Canvas(root, width=1200, height=700)
canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)
canv.pack()

while Q < 50:
    x = randint(0, 800)
    y = randint(0, 400)
    m = randint(1,5)
    ind = randint(0,4)

    tr = np.array([[m/10, 0, 0],
                   [0, m/10, 0],
                   [x, y, 0]])

    a = np.array([[x0, y0, 1],
                  [600.5, 500.5, 1],
                  [550.5, 400.5, 1],
                  [800.5, 350.5, 1],
                  [850.5, 450.5, 1],

                  [600.5, 200.5, 1],
                  [550.5, 100.5, 1],
                  [800.5, 50.5, 1],
                  [850.5, 150.5, 1]])

    a = a.dot(tr)
    for i in range(1, 8):
        if i == 4:
            pass
        else:
            canv.create_line(a[i][0], a[i][1], a[i + 1][0], a[i + 1][1], width=2, fill=colors[ind])

    for i in range(1, 5):
        canv.create_line(a[i][0], a[i][1], a[i + 4][0], a[i + 4][1], width=2, fill=colors[ind])
    canv.update()
    time.sleep(0.1)
    Q = Q + 1

root.mainloop()