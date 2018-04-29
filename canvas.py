import tkinter as tk


class Canva():
    def __init__(self, width, height):
        self.canvas = None
        self.mycanvas = None
        self.width = width
        self.height = height

    def mycanvas_init(self, window):
        self.mycanvas = tk.Canvas(window, bg='white', width=self.width, height=self.height)
        self.mycanvas.pack()
