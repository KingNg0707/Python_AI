import math
import time
import random
import threading


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
            try:
                self.event.wait()
                self.arc_rand_move()
                self.arc_rand_rotate()
            except:
                print(f"{self.name} thread end.")
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

            time.sleep(0.02)

    def arc_rand_rotate(self):

        if random.randint(0, 5) < 3:  # 转向

            self.arc_rotate_lr(random.randint(0, 2))
            time.sleep(0.02)

    def arc_check_place(self):
        return self.xy

    def arc_check_rotate(self):
        return self.startC

    def arc_check_edge(self):
        if self.arc_check_place() >= 400:
            pass
