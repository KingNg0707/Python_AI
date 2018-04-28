import math
import time
import random
import threading


# #画圆1
class Arc(threading.Thread):
    _arc = None
    _canvas = None

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
            self.event.wait()
            self.arc_rand_move()
            self.arc_rand_rotate()

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

    # ####移动一个圆
    def arc_move(self):
        # 旋转角度坐标移动的计算
        x = 1 * math.sin(math.radians(self.startC - 30 + 270))
        y = 1 * math.cos(math.radians(self.startC - 30 + 270))
        self._canvas.move(self._arc, x, y)

        self.xy[0] += x
        self.xy[1] += y

    def arc_rotate_lr(self, lr):
        if lr == 0:
            self.startC += 5
        elif lr == 1:
            self.startC -= 5

        self._canvas.delete(self._arc)
        self._arc = self._canvas.create_arc(self.xy,
                                            self.xy[0] + self.size[0],
                                            self.xy[1] + self.size[1],
                                            start=self.startC,
                                            extent=self.extentC,
                                            fill=self.color)

    # ###随机移动函数
    def arc_rand_move(self):

        if random.randint(0, 5) < 3:  # 前进
            self.arc_move()
            # mycanvas.move(canvas_arctest,2,2)
            # canvas_arctest.move(mycanvas)
            time.sleep(0.01)

    def arc_rand_rotate(self):

        if random.randint(0, 5) < 3:  # 转向

            self.arc_rotate_lr(random.randint(0, 2))
            time.sleep(0.01)
        # if who.index == 1:
        #     global canvas_arc1
        #     mycanvas.delete(canvas_arc1)
        #     canvas_arc1 = mycanvas.create_arc(who.xy,
        #                                       who.xy[0] + who.size[0],
        #                                       who.xy[1] + who.size[1],
        #                                       start=who.startC,
        #                                       extent=who.extentC,
        #                                       fill=who.color)
        # elif who.index == 2:
        #     global canvas_arc2
        #     mycanvas.delete(canvas_arc2)
        #     canvas_arc2 = mycanvas.create_arc(who.xy,
        #                                       who.xy[0] + who.size[0],
        #                                       who.xy[1] + who.size[1],
        #                                       start=who.startC,
        #                                       extent=who.extentC,
        #                                       fill=who.color)
        # elif who.index == 3:
        #     global canvas_arc3
        #     mycanvas.delete(canvas_arc3)
        #     canvas_arc3 = mycanvas.create_arc(who.xy,
        #                                       who.xy[0] + who.size[0],
        #                                       who.xy[1] + who.size[1],
        #                                       start=who.startC,
        #                                       extent=who.extentC,
        #                                       fill=who.color)

    #
    # # ##随机移动 圆1
    # def arc1_randmove():
    #     arc_randmove(arc1, canvas_arc1)
    #     # print(arc_check_place(arc1))
    #     # print(arc_check_Rotate(arc1))
    #
    #     # arc_randRotate(arc1)
    #
    #
    # # ##随机移动 圆2
    # def arc2_randmove():
    #     arc_randmove(arc2, canvas_arc2)
    #     # arc_randRotate(arc2)
    #
    #
    # # ##随机移动 圆3
    # def arc3_randmove():
    #     arc_randmove(arc3, canvas_arc3)
    #     # arc_randRotate(arc3)
    #
    #
    # def arc4_randmove():
    #     arc_randmove(arc4, canvas_arc4)
    #
    # def arcs_rand_move(self, arcst, canvas_arcst, canvas):
    #     self.arc_randmove(arcst[0], canvas_arcst[0], canvas)
    #
    # # ##随机旋转 圆1
    # def arc1_rand_rotate(self, arc, canvas_arcst, canva):
    #     self.arc_rand_rotate(arc, canvas_arcst, canva)

    # # ##随机旋转 圆2
    # def arc2_rand_rotate(self):
    #     self.arc_rand_rotate(self.arc2)
    #
    # # ##随机旋转 圆3
    # def arc3_rand_rotate(self):
    #     self.arc_rand_rotate(self.arc3)
    #
    # def arcs_rand_rotate(self):
    #     self.arc_rand_rotate(self.arcst[0])

    # def arc_check_edge():
    #    if
    # def arc1_check_edge():
    #    if
    # def arc2_check_edge():
    #    if
    # def arc3_check_edge():
    #    if

#
#
# def arctest_creat(self, window):
#     window.create_arc(self.xy, self.xy[0] + self.size[0], self.xy[1] + self.size[1], start=self.startC,
#                       extent=self.extentC, fill=self.color)
#
#
# def arc_move(xy):
#     x = 1 * math.sin(math.radians(arc1_start - 30 + 270))
#     y = 1 * math.cos(math.radians(arc1_start - 30 + 270))
#
#     canvas.move(arc1, x, y)
#
#     arc1_xy = [arc1_xy[0] + x, arc1_xy[1] + y, arc1_xy[0] + x + 20, arc1_xy[1] + y + 20]
#
#     return xy
