import math
import tkinter as tk


def arctest_creat(self, window):
    window.create_arc(self.xy, self.xy[0] + self.size[0], self.xy[1] + self.size[1], start=self.startC,
                      extent=self.extentC, fill=self.color)


##画圆1
class arcs_1(object):
    name = 'arc1'
    index = 1
    xy = [10, 10]
    size = [20, 20]
    startC = 120
    extentC = 300
    color = 'red'

    def setName(self, name):
        self.name = name

    def setStartC(self, c):
        self.start = c

    def getName(self):
        return self.name


##画圆2
class arcs_2(object):
    name = 'arc2'
    index = 2
    xy = [60, 60]
    size = [20, 20]
    startC = 120
    extentC = 300
    color = 'blue'

    def setName(self, name):
        self.name = name

    def setStartC(self, c):
        self.start = c

    def getName(self):
        return self.name


##画圆3
class arcs_3(object):
    name = 'arc3'
    index = 3
    xy = [110, 110]
    size = [20, 20]
    startC = 120
    extentC = 300
    color = 'green'

    def setName(self, name):
        self.name = name

    def setStartC(self, c):
        self.start = c

    def getName(self):
        return self.name


# 定义3个园的名称 (4个)
gArc_1 = arcs_1()
gArc_2 = arcs_2()
gArc_3 = arcs_3()


def arc_move(xy):
    x = 1 * math.sin(math.radians(arc1_start - 30 + 270))
    y = 1 * math.cos(math.radians(arc1_start - 30 + 270))

    canvas.move(arc1, x, y)

    arc1_xy = [arc1_xy[0] + x, arc1_xy[1] + y, arc1_xy[0] + x + 20, arc1_xy[1] + y + 20]

    return xy



