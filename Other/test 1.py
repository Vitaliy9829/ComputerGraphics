import math
from tkinter import *

N = 20


def getRotMatrix(theta):
    return [[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]]


def matrix2vector(_matrix, _vector):
    x1 = _matrix[0][0] * _vector[0] + _matrix[0][1] * _vector[1]
    y1 = _matrix[1][0] * _vector[0] + _matrix[1][1] * _vector[1]
    return [x1, y1]


def deg2rad(degr):
    return degr / 57.2958


def rotateVector(vector, theta):
    theta = deg2rad(theta)
    return matrix2vector(getRotMatrix(theta), vector)


def getScreenSpace(vector):
    vector[1] = screen[1] - vector[1]
    return vector


def drawLine(source, dst, offset):
    x1 = offset[0] + source[0]
    y1 = offset[1] + source[1]
    x2 = offset[0] + dst[0]
    y2 = offset[1] + dst[1]
    vec1 = getScreenSpace([x1, y1])
    vec2 = getScreenSpace([x2, y2])
    canv.create_line(vec1[0], vec1[1], vec2[0], vec2[1])


def drawBase(source, side, angle, deep):
    p1 = rotateVector([0, 0], angle)
    p2 = rotateVector([side, 0], angle)
    p3 = rotateVector([side, side], angle)
    p4 = rotateVector([0, side], angle)
    p5 = rotateVector([side / 2, 3 / 2 * side], angle)
    drawLine(p1, p2, source)
    drawLine(p2, p3, source)
    drawLine(p3, p5, source)
    drawLine(p5, p4, source)
    drawLine(p4, p1, source)

    offset1 = [source[0] + p5[0], source[1] + p5[1]]
    offset2 = [source[0] + p4[0], source[1] + p4[1]]

    if (deep > 0):
        deep -= 1
        drawBase(offset1, side * math.sqrt(2) / 2, angle + 45, deep)
        drawBase(offset2, side * math.sqrt(2) / 2, angle - 45, deep)


root = Tk();
root.title("Pifagor's tree")

screen = [900, 600]
canv = Canvas(root, width=screen[0], height=screen[1], bg="lightgreen")
canv.pack()

drawBase([300, 300], 50, 0, N)

root.mainloop()