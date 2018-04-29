from windows import Windows
from canvas import Canva
from creatures import Creature


def main():
    wds = Windows()
    wds.window_init()
    window = wds.window

    mc = Canva(300,250)
    mc.mycanvas_init(window)
    # mycanvas = mc.mycanvas

    creatures = Creature(mc)
    creatures.arcs_init()

    wds.button_init(creatures)

    creatures.run_threads()

    # for i in range(10):
    #    time.sleep(0.1)
    #    Rotate_arc1()

    # 窗口循环刷新

    window.mainloop()


if __name__ == "__main__":
    main()
