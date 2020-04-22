import math
from tkinter import *
import numpy as np
from multiprocessing import Process, freeze_support
import time
import math
# from numba import vectorize,jit,cuda
import numba
from numba import cuda

print(cuda.gpus)

root = Tk()
canvas = Canvas(root, width=800, height=800, bg="lightgrey")


# @vectorize(['float32(float32, float32)'], target='cuda')

class Pyramide:

    def Drawline(self, x1, y1, x2, y2):
        h, w = 400, 400
        canvas.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            # fill=self.fg_color,
            # dash=(20, 40)
        )

    def DrawOS(self, x1, y1, x2, y2):
        h, w = 400, 400
        canvas.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            width=2, arrow=LAST
        )

    def DrawlineWithDash(self, x1, y1, x2, y2):
        h, w = 400, 400
        canvas.create_line(
            x1 + w, h - y1,
            x2 + w, h - y2,
            # fill=self.fg_color,
            dash=(20, 40)
        )

    def DrawOSText(self, x1, y1, t):
        h, w = 400, 400
        canvas.create_text(x1 + w, h - y1, width=80, text=t)

    def OSI(self, b):
        self.DrawOS(b[0][0], b[0][1], b[1][0], b[1][1])
        self.DrawOSText(b[1][0], b[1][1] - 20, 'x')
        self.DrawOS(b[0][0], b[0][1], b[2][0], b[2][1])
        self.DrawOSText(b[2][0] + 20, b[2][1] + 10, 'y')
        self.DrawOS(b[0][0], b[0][1], b[3][0], b[3][1])
        self.DrawOSText(b[3][0] + 10, b[3][1] + 10, 'z')

    def DrawlineXA(self, x1, y1, x2, y2, x3, y3, x4, y4, k1, k2):
        h, w = 400, 400
        while x1 <= x3 and x2 <= x4:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            x1 = x1 + k1
            x2 = x2 + k1
            y1 = y1 + k2
            y2 = y2 + k2

    def DrawlineX(self, x1, y1, x2, y2, x3, y3, x4, y4):
        h, w = 400, 400
        while x1 <= x4 and x2 <= x3:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            x1 = x1 + 5
            x2 = x2 + 5
            y1 = y1 + 1.2
            y2 = y2 + 1.2

    def DrawlineY(self, x1, y1, x2, y2, x3, y3, x4, y4):
        h, w = 400, 400
        while y1 <= y4 and y2 <= y3:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            # x1 = x1 + 10
            # x2 = x2 + 10
            y1 = y1 + 5
            y2 = y2 + 5

    def DrawlineYA(self, x1, y1, x2, y2, x3, y3, x4, y4, k1, k2):
        h, w = 400, 400
        while y1 <= y3 and y2 <= y4:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            x1 = x1 + k1
            x2 = x2 + k1
            y1 = y1 + k2
            y2 = y2 + k2

    def DrawlineXR(self, x1, y1, x2, y2, x3, y3, x4, y4):
        h, w = 400, 400
        while x1 >= x3 and x2 >= x4:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            x1 = x1 - 5
            x2 = x2 - 5
            y1 = y1 - 1.2
            y2 = y2 - 1.2

    def DrawlineYR(self, x1, y1, x2, y2, x3, y3, x4, y4):
        h, w = 400, 400
        while y1 >= y3 and y2 >= y4:
            canvas.create_line(
                x1 + w, h - y1,
                x2 + w, h - y2,
                # fill=self.fg_color,
                # dash=(20, 40)
            )
            # x1 = x1 + 10
            # x2 = x2 + 10
            y2 = y2 - 5
            y1 = y1 - 5

    def down(self, a):
        i = 0
        j = 0
        self.DrawlineX(a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1], a[j + 2][i], a[j + 3][i + 1],
                       a[j + 2][i], a[j + 2][i + 1])

        self.DrawlineY(a[j + 3][i], a[j + 3][i + 1], a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1],
                       a[j + 2][i], a[j + 2][i + 1])

    def up(self, a):
        i = 0
        j = 4
        self.DrawlineX(a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1], a[j + 2][i], a[j + 3][i + 1],
                       a[j + 2][i], a[j + 2][i + 1])

        self.DrawlineY(a[j + 3][i], a[j + 3][i + 1], a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1],
                       a[j + 2][i], a[j + 2][i + 1])

    def esle(self, a):
        i = 0
        for j in range (2):
            if j ==0:
                self.DrawlineXA(a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1], a[j + 4][i], a[j + 4][i + 1],
                                a[j + 5][i], a[j + 5][i + 1], 5, -4.5)
                self.DrawlineYA(a[j][i], a[j][i + 1], a[j + 4][i], a[j + 4][i + 1], a[j + 1][i], a[j + 1][i + 1],
                                a[j + 5][i], a[j + 5][i + 1], 0, 5)
                self.DrawlineXA(a[j + 3][i], a[j + 3][i + 1], a[j][i], a[j][i + 1], a[j + 7][i], a[j + 7][i + 1],
                                a[j + 4][i], a[j + 4][i + 1], 5, -4.5)
                self.DrawlineYA(a[j + 3][i], a[j + 3][i + 1], a[j + 7][i], a[j + 7][i + 1], a[j + 2][i],
                                a[j + 2][i + 1],
                                a[j + 6][i], a[j + 6][i + 1], 0, 5)
            else:
                self.DrawlineXA(a[j][i], a[j][i + 1], a[j + 1][i], a[j + 1][i + 1], a[j + 4][i], a[j + 4][i + 1],
                                a[j + 5][i], a[j + 5][i + 1], 4.4, -4)
                self.DrawlineYA(a[j][i], a[j][i + 1], a[j + 4][i], a[j + 4][i + 1], a[j + 1][i], a[j + 1][i + 1],
                                a[j + 5][i], a[j + 5][i + 1], 4.4, 1)
                self.DrawlineXA(a[j + 1][i], a[j + 1][i + 1], a[j + 2][i], a[j + 2][i + 1], a[j + 5][i],
                                a[j + 5][i + 1],
                                a[j + 6][i], a[j + 6][i + 1], 5, -4.5)
                self.DrawlineXA(a[j - 1][i], a[j - 1][i + 1], a[j + 3][i], a[j + 3][i + 1], a[j + 2][i],
                                a[j + 2][i + 1],
                                a[j + 6][i], a[j + 6][i + 1], 5, 1.2)




    def MoveForward(self, a, m, k):
        fi = 0.45
        psi = 0.5
        b = np.array([
            [math.cos(fi) * 0.5, math.sin(psi) * math.sin(fi) * 0.5, 0, 0],
            [0, math.cos(fi) * 0.5, 0, 0],
            [math.sin(fi) * 0.5, -math.sin(fi) * math.cos(fi) * 0.5, 0, 0],
            [400, 500, 0, 1]
        ])
        # b = b.transpose()
        # b = np.array([[0.5, 0, 0],
        #               [0, 0.5, 0],
        #               [0, 0, 0]])
        a = a.dot(b)
        k = k.dot(b)
        # self.poll(a)
        # self.OSI(k)
        self.down(a)
        self.up(a)
        self.esle(a)

    def Move(self, k, a, m):
        for i in range(1, k):
            canvas.delete("all")
            # X += X
            # Y += Y
            canvas.create_text(300, 10, fill="darkblue", font="Times 20 italic bold",
                               text="Паралелепіпед , площина")
            self.MoveForward(a, i, m)
            root.update_idletasks()
            root.update()
        canvas.mainloop()


def main():
    canvas.pack()
    b = Pyramide()
    x0 = 500
    y0 = 500
    z0 = 1
    a = np.array([[0, 0, 0, 0],
                  [0, 300, 0, 0],
                  [400, 300, 0, 0],
                  [400, 0, 0, 0],
                  [0, 0, 400, 0],
                  [0, 300, 400, 0],
                  [400, 300, 400, 0],
                  [400, 0, 400, 0]])
    m = np.array([
        [0, 0, 0, 1],
        [500, 0, 0, 1],
        [0, -400, 0, 1],
        [0, 0, 500, 1]
    ])
    m = m.transpose()
    b.Move(2, a, m)


if __name__ == '__main__':
    main()
