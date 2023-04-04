import tkinter as tk
from random import randint

class Raindrop:
    def __init__(self, canvas, x, y, yspeed, length):
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.length = length
        self.canvas = canvas
        self.color = '#%02x%02x%02x' % (randint(0, 255), randint(0, 255), randint(0, 255))
        self.line = canvas.create_line(self.x, self.y, self.x, self.y+length, fill=self.color)

    def move(self):
        self.y += self.yspeed
        self.canvas.move(self.line, 0, self.yspeed)
        if self.y > 500:
            self.canvas.move(self.line, 0, -(500+self.length))
            self.y -= 500 + self.length

def redraw():
    for drop in drops:
        drop.move()
    fr.after(10, redraw)

fr = tk.Tk()
canvas = tk.Canvas(fr, height=500, width=500, bg= 'gray10')
canvas.pack()
drops = [Raindrop(canvas, x=randint(0, 500), y=randint(0, 500), 
                  yspeed=randint(3, 4), length=randint(5, 10)) for i in range(270)]
redraw()
fr.mainloop()



