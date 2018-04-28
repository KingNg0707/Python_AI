import tkinter as tk


class Canva():
    def __init__(self):
        self.canvas = None

    def mycanvas_init(self, window):
        self.mycanvas = tk.Canvas(window, bg='white', width=600, height=500)
        self.mycanvas.pack()
