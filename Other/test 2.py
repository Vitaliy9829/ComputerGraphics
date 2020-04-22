from math import ceil
import numpy as np
import matplotlib.pyplot as plt



class Pixel():
def __init__(self, x, y):
    self.x = x
    self.y = y
    self.filled = 0
def filled_check(self, n):
    if n >= 1:
        if (self.x % 3 == 2 and self.y % 3 == 2):
            self.filled = 1
        else:
            self.x = ceil(self.x / 3)
            self.y = ceil(self.y / 3)
            self.filled_check(n - 1)
def sierpinski_graph(n):
    p = 3 ^ n
    line = 1
    matrix_s = []
    for i in range(1, p + 1):
        matrix_row = []
        for j in range(1, p + 1):
            pixel = Pixel(j, i)
            pixel.filled_check(n)
            matrix_row.append(pixel.filled)
        matrix_s.append(matrix_row)
    return matrix_s

sierpinski_graph(5)
