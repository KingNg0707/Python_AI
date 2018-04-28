import threading
from arcs import Arc


class Creature():
    def __init__(self, mycanvas):
        self._mycanvas = mycanvas
        self._arc = Arc
        self.start = False
        self.arcs_list = []
        self.canvas_arcst = []

        self.arc_list = ["arc1", 20, 20, 20, 20, 120, 300, "red", 1], \
                        ["arc2", 70, 70, 20, 20, 120, 300, "blue", 2], \
                        ["arc3", 120, 120, 20, 20, 120, 300, "green", 3], \
                        ["arc4", 170, 170, 20, 20, 120, 300, "yellow", 4]
        #
        # self.arc1 = self._arcs.arcs_init("arc1", 10, 10, 20, 20, 120, 300, "black", 1)
        # self.arc2 = self._arcs.arcs_init("arc2", 60, 60, 20, 20, 120, 300, "black", 2)
        # self.arc3 = self._arcs.arcs_init("arc3", 110, 110, 20, 20, 120, 300, "black", 3)
        # self.arc4 = self._arcs.arcs_init("arc4", 160, 160, 20, 20, 120, 300, "black", 4)
        #
        # self.canvas_arc1 = None
        # self.canvas_arc2 = None
        # self.canvas_arc3 = None
        # self.canvas_arc4 = None

    def arcs_init(self):
        # 初始化圆的值
        for i in range(len(self.arc_list)):
            self.arcs_list.append(self._arc())
            self.arcs_list[i].event.clear()
            self.arcs_list[i].arcs_init(name=self.arc_list[i][0],
                                        x=self.arc_list[i][1],
                                        y=self.arc_list[i][2],
                                        sx=self.arc_list[i][3],
                                        sy=self.arc_list[i][4],
                                        start=self.arc_list[i][5],
                                        extent=self.arc_list[i][6],
                                        color=self.arc_list[i][7],
                                        index=self.arc_list[i][8])

            arc = self._mycanvas.create_arc(self.arcs_list[i].xy,
                                            self.arcs_list[i].xy[0] + self.arcs_list[i].size[0],
                                            self.arcs_list[i].xy[1] + self.arcs_list[i].size[1],
                                            start=self.arcs_list[i].startC,
                                            extent=self.arcs_list[i].extentC,
                                            fill=self.arcs_list[i].color)
            self.arcs_list[i]._canvas = self._mycanvas
            self.arcs_list[i]._arc = arc
            self.canvas_arcst.append(arc)

    def run_threads(self):
        print(threading.current_thread())
        for i in self.arcs_list:
            i.start()

    #     self.arcs_creat(mycanvas)
    #
    # # 创建空间
    # # [a*b for a, b in zip(arc1_xy,arc1_size)]
    # def arcs_creat(self, mycanvas):
    #     # 创建3个圆形
    #     canvas_arc1 = mycanvas.create_arc(self.arc1.xy, self.arc1.xy[0] + self.arc1.size[0],
    #                                       self.arc1.xy[1] + self.arc1.size[1],
    #                                       start=self.arc1.startC,
    #                                       extent=self.arc1.extentC, fill=self.arc1.color)
    #     canvas_arc2 = mycanvas.create_arc(self.arc2.xy, self.arc2.xy[0] + self.arc2.size[0],
    #                                       self.arc2.xy[1] + self.arc2.size[1],
    #                                       start=self.arc2.startC,
    #                                       extent=self.arc2.extentC, fill=self.arc2.color)
    #     canvas_arc3 = mycanvas.create_arc(self.arc3.xy, self.arc3.xy[0] + self.arc3.size[0],
    #                                       self.arc3.xy[1] + self.arc3.size[1],
    #                                       start=self.arc3.startC,
    #                                       extent=self.arc3.extentC, fill=self.arc3.color)
    #     canvas_arc4 = mycanvas.create_arc(self.arc4.xy, self.arc4.xy[0] + self.arc4.size[0],
    #                                       self.arc4.xy[1] + self.arc4.size[1],
    #                                       start=self.arc4.startC,
    #                                       extent=self.arc4.extentC, fill=self.arc4.color)

    def arc_check_place(self, who):
        return who.xy

    def arc_check_rotate(self, who):
        return who.startC

    def action(self):
        self.start = True
        # added_thread_check_edge = threading.Thread(target=arc_check_edge)
        # added_thread_check_edge.start()
        #
        # # #添加自动移动到线程
        # added_thread1 = threading.Thread(target=arc1_randmove)
        # # threads.append(added_thread1)
        # added_thread1.start()
        # added_thread1a = threading.Thread(target=arc1_rand_rotate)
        # # threads.append(added_thread1a)
        # added_thread1a.start()
        #
        # added_thread2 = threading.Thread(target=arc2_randmove)
        # added_thread2.start()
        # added_thread2a = threading.Thread(target=arc2_rand_rotate)
        # added_thread2a.start()
        #
        # added_thread3 = threading.Thread(target=arc3_randmove)
        # added_thread3.start()
        # added_thread3a = threading.Thread(target=arc3_rand_rotate)
        # added_thread3a.start()
        #
        # added_thread4 = threading.Thread(target=arc4_randmove)
        # added_thread4.start()

        # added_thread5 = threading.Thread(target=self._arcs.arc_randmove,
        #                                  args=[self.arcst, self.canvas_arcst, self._mycanvas, ])
        # added_thread5.start()
        #
        # added_thread5a = threading.Thread(target=self._arcs.arc_rand_rotate,
        #                                   args=[self.arcst, self.canvas_arcst, self._mycanvas, ])
        # added_thread5a.start()
        for i in self.arcs_list:
            i.event.set()
        print(threading.active_count())

    def action_stop(self):

        for i in self.arcs_list:
            i.event.clear()
        self.start = False
