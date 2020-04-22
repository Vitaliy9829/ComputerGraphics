from tkinter import *
root = Tk()
xy = 600
canv = Canvas(root, width=xy, height=xy)
canv.pack()
i = 5


cycle = 0
def drawCarpet(a, b, c, d, n):
    ++cycle
    if(n <= 0):
        return 0
    #визначення вершин
    a1 = 2 * a / 3 + c / 3
    c1 = a / 3 + 2 * c / 3
    b1 = 2 * b / 3 + d / 3
    d1 = b / 3 + 2 * d / 3

    #малюэ прямокутник
    canv.create_rectangle(a1, b1, c1, d1, fill = "Black")

    drawCarpet(a, b, a1, b1, n - 1)
    drawCarpet(a1, b, c1, b1, n - 1)
    drawCarpet(c1, b, c, b1, n - 1)

    drawCarpet(a, b1, a1, d1, n - 1)
    drawCarpet(c1, b1, c, d1, n - 1)

    drawCarpet(a, d1, a1, d, n - 1)
    drawCarpet(a1, d1, c1, d, n - 1)
    drawCarpet(c1, d1, c, d, n - 1)

    canv.create_rectangle(0, 0, cycle * 9 , 16, fill = "Black")

drawCarpet(0, 0, xy, xy, i)
canv.mainloop()