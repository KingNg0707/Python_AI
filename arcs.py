import sys
import math
import time
import random
import threading


class Arc(threading.Thread):
    arc = None
    canvas = None

    name = 'arc1'
    index = 1
    xy = [10, 10]
    size = [20, 20]
    startC = 120
    extentC = 300
    color = 'red'

    event = threading.Event()

    def run(self):
        print(threading.current_thread())
        while True:
            try:
                self.event.wait()
                self.arc_rand_move()
                self.arc_rand_rotate()
            except:
                print(f"{self.name} thread end.\n{sys.exc_info()}")
                break

    def arcs_init(self, name, x, y, sx, sy, start, extent, color, index):
        self.name = name
        self.xy = [x, y]
        self.size = [sx, sy]
        self.startC = start
        self.extentC = extent
        self.color = color
        self.index = index

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def arc_move(self):
        # 旋转角度坐标移动的计算
        x = 1 * math.sin(math.radians(self.startC - 30 + 270))
        y = 1 * math.cos(math.radians(self.startC - 30 + 270))
        self.canvas.mycanvas.move(self.arc, *self.wall(x, y))

        self.xy[0] += x
        self.xy[1] += y

    def arc_rotate_lr(self, lr):
        if lr == 0:
            self.startC += 5
        elif lr == 1:
            self.startC -= 5

        self.canvas.mycanvas.delete(self.arc)
        self.arc = self.canvas.mycanvas.create_arc(self.xy,
                                                   self.xy[0] + self.size[0],
                                                   self.xy[1] + self.size[1],
                                                   start=self.startC,
                                                   extent=self.extentC,
                                                   fill=self.color)

    # ###随机移动函数
    def arc_rand_move(self):

        if random.randint(0, 5) < 3:  # 前进
            self.arc_move()

            time.sleep(0.01)

    def arc_rand_rotate(self):

        if random.randint(0, 5) < 3:  # 转向

            self.arc_rotate_lr(random.randint(0, 2))
            time.sleep(0.01)

    def wall(self, x, y):
        # FIXME 碰到下边时，有机会出墙
        # FIXME 碰到右边时，如果方向是向上方的，会反方向调头
        # print(self.startC)
        # print(f"{self.name}\t{self.xy}")
        place = self.arc_check_place()
        rotate = self.arc_check_rotate()
        ##右边
        if int(place[0]) > self.canvas.width - self.size[0]:
            if rotate > 120 < 300:
                # x = 0
                self.arc_x_x()


        ##左边
        elif int(place[0]) < 0:
            if rotate < 120 or rotate > 300:
                # x = 0
                self.arc_x_x()

        ##下边
        if int(place[1]) > self.canvas.height - self.size[1]:
            if rotate < 210 > 30:
                # y = 0
                self.arc_y_y()

        ##上边
        elif int(place[1]) < 0:
            if rotate > 210 or rotate < 30:
                # y = 0
                self.arc_y_y()

        return x, y

    def arc_check_place(self):
        return self.xy

    def arc_check_rotate(self):
        return self.startC

    def arc_check_edge(self):
        if self.arc_check_place() >= 400:
            pass

    def arc_x_x(self):  # FIXME x_x y_y两个函数内容相同
        a = self.startC + 270
        self.startC = a % 360

    def arc_y_y(self):
        a = self.startC + 270
        self.startC = a % 360
