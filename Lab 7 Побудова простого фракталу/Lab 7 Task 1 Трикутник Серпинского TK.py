from tkinter import *
import math
root = Tk()
canv = Canvas(root, width=700, height=700)
canv.pack()
def draw_sierpinski(length,depth, a , b):
       if depth==0:
           canv.create_line(a, b, a + length, b, fill = "Red", width = 2)
           ydt = math.sqrt(math.pow(length,2) - math.pow((length/2), 2))
           canv.create_line(a , b, a + length/2, b - ydt, fill = "Black", width = 3)
           canv.create_line(a + length/2, b - ydt, a + length, b)
       else:
           draw_sierpinski(length/2,depth-1, a , b)
           draw_sierpinski(length/2,depth-1, a - length/2, b)
           ydt = math.sqrt(math.pow(length/2,2) - math.pow((length/4), 2))
           draw_sierpinski(length/2,depth-1, a - length/4, b - ydt)
           
draw_sierpinski(300, 3, 450, 500)           
canv.mainloop()