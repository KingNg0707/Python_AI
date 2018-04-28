import tkinter as tk


class Windows():
    def __init__(self):
        self.window = None

    def window_init(self):
        self.window = tk.Tk()
        self.window.title('Creatures')
        self.window.geometry('800x600')

    def button_init(self, creatures):
        # 初始化按键
        move_button = tk.Button(self.window, text='move', command=creatures.action)
        move_button.pack()

        move_button2 = tk.Button(self.window, text='stop', command=creatures.action_stop)
        move_button2.pack()
