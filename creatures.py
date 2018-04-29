import threading
from arcs import Arc


class Creature():
    def __init__(self, mc):
        self._mc = mc
        self._arc = Arc
        self.arcs_list = []
        self.canvas_arcst = []

        self.arc_list = ["arc1", 20, 20, 20, 20, 120, 300, "red", 1], \
                        ["arc2", 70, 70, 20, 20, 120, 300, "blue", 2], \
                        ["arc3", 120, 120, 20, 20, 120, 300, "green", 3], \
                        ["arc4", 170, 170, 20, 20, 120, 300, "yellow", 4], \
                        ["arc5", 220, 220, 20, 20, 120, 300, "grey", 5]

    def arcs_init(self):

        # 初始化圆的值
        for i in range(len(self.arc_list)):
            self.arcs_list.append(self._arc())
            self.arcs_list[i].event.clear()
            self.arcs_list[i].arcs_init(name=self.arc_list[i][0],
                                        x=self.arc_list[i][1], y=self.arc_list[i][2],
                                        sx=self.arc_list[i][3], sy=self.arc_list[i][4],
                                        start=self.arc_list[i][5], extent=self.arc_list[i][6],
                                        color=self.arc_list[i][7],
                                        index=self.arc_list[i][8])

            arc = self._mc.mycanvas.create_arc(self.arcs_list[i].xy,
                                               self.arcs_list[i].xy[0] + self.arcs_list[i].size[0],
                                               self.arcs_list[i].xy[1] + self.arcs_list[i].size[1],
                                               start=self.arcs_list[i].startC, extent=self.arcs_list[i].extentC,
                                               fill=self.arcs_list[i].color)
            self.arcs_list[i].canvas = self._mc
            self.arcs_list[i].arc = arc
            self.canvas_arcst.append(arc)

    def run_threads(self):
        print(threading.current_thread())
        for i in self.arcs_list:
            i.start()

    def action(self):
        for i in self.arcs_list:
            i.event.set()
        print(threading.active_count())

    def action_stop(self):
        for i in self.arcs_list:
            i.event.clear()
