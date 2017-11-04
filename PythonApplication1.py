import tkinter as tk
import time
import math
import random
import threading
from arcs import gArc_1 as arc1
from arcs import gArc_2 as arc2
from arcs import gArc_3 as arc3

Start = False
window = tk.Tk()
window.title('tkinter test')
window.geometry('400x400')

# 创建3个圆形
mycanvas = tk.Canvas(window, bg='white', height=250, width=250)
mycanvas.pack()
# [a*b for a, b in zip(arc1_xy,arc1_size)]
canvas_arc1 = mycanvas.create_arc(arc1.xy, arc1.xy[0] + arc1.size[0], arc1.xy[1] + arc1.size[1], start=arc1.startC,
                                  extent=arc1.extentC, fill=arc1.color)
canvas_arc2 = mycanvas.create_arc(arc2.xy, arc2.xy[0] + arc2.size[0], arc2.xy[1] + arc2.size[1], start=arc2.startC,
                                  extent=arc2.extentC, fill=arc2.color)
canvas_arc3 = mycanvas.create_arc(arc3.xy, arc3.xy[0] + arc3.size[0], arc3.xy[1] + arc3.size[1], start=arc3.startC,
                                  extent=arc3.extentC, fill=arc3.color)


# 设置生命体的外观
def init_arcs(who, name, x, y, sx, sy, start, extent, color, index):
    who.name = name
    who.xy = [x, y]
    who.size = [sx, sy]
    who.startC = start
    who.extentC = extent
    who.color = color
    who.index = index


# init_arcs(arctest,"a2",40,40,20,20,120,300,"blue",6)
# canvas_arctest2=arctest.creat(canvas)

##print(arc_test1.name)
##arc_test1.setname('g')
##print(arc_test1.name)
##print(arc_test2.name)
##arc_test2.setname('g1')
##print(arc_test2.name)

##def arctest(who):
##    print(who.name)

##arctest(arc_test1)
##arctest(arc_test2)

def arc1_move():
    global arc1_xy
    global canvas_arc1

    x = 1 * math.sin(math.radians(arc1_startC - 30 + 270))
    y = 1 * math.cos(math.radians(arc1_startC - 30 + 270))

    arc1_xy = [arc1_xy[0] + x, arc1_xy[1] + y]

    mycanvas.move(canvas_arc1, x, y)


def arc2_move():
    global arc2_xy
    global canvas_arc2

    x = 1 * math.sin(math.radians(arc2_start - 30 + 270))
    y = 1 * math.cos(math.radians(arc2_start - 30 + 270))

    mycanvas.move(canvas_arc2, x, y)

    arc2_xy = [arc2_xy[0] + x, arc2_xy[1] + y, arc2_xy[0] + x + 20, arc2_xy[1] + y + 20]


#####移动一个圆
def arc_move(who, canvas_arc):
    # 旋转角度坐标移动的计算
    x = 1 * math.sin(math.radians(who.startC - 30 + 270))
    y = 1 * math.cos(math.radians(who.startC - 30 + 270))
    mycanvas.move(canvas_arc, x, y)

    who.xy[0] += x
    who.xy[1] += y


def arc1_Rotate_right():
    global arc1_startC
    global canvas_arc1
    global arc1_xy
    arc1_startC -= 2
    mycanvas.delete(canvas_arc1)
    canvas_arc1 = mycanvas.create_arc(arc1_xy, start=arc1_startC, extent=300, fill='red')


def arc2_Rotate_right():
    global arc2_start
    global canvas_arc2
    global arc2_xy
    arc2_start -= 2
    mycanvas.delete(canvas_arc2)
    canvas_arc2 = mycanvas.create_arc(arc2_xy, start=arc2_start, extent=300, fill='blue')


def arc_Rotate_LR(who, LR):
    if LR == 0:
        who.startC += 5
    elif LR == 1:
        who.startC -= 5
    if who.index == 1:
        global canvas_arc1
        mycanvas.delete(canvas_arc1)
        canvas_arc1 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)
    elif who.index == 2:
        global canvas_arc2
        mycanvas.delete(canvas_arc2)
        canvas_arc2 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)
    elif who.index == 3:
        global canvas_arc3
        mycanvas.delete(canvas_arc3)
        canvas_arc3 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)


def arc_Rotate_right(who):
    who.startC -= 2
    if who.index == 1:
        global canvas_arc1
        mycanvas.delete(canvas_arc1)
        canvas_arc1 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)
    elif who.index == 2:
        global canvas_arc2
        mycanvas.delete(canvas_arc2)
        canvas_arc2 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)
    elif who.index == 3:
        global canvas_arc3
        mycanvas.delete(canvas_arc3)
        canvas_arc3 = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1], start=who.startC,
                                          extent=who.extentC, fill=who.color)


###随机移动 圆1
def arc1_randmove():
    arc_randmove(arc1, canvas_arc1)
    # arc_randRotate(arc1)


###随机移动 圆2
def arc2_randmove():
    arc_randmove(arc2, canvas_arc2)
    # arc_randRotate(arc2)


###随机移动 圆3
def arc3_randmove():
    arc_randmove(arc3, canvas_arc3)
    # arc_randRotate(arc3)


###随机旋转 圆1
def arc1_randRotate():
    arc_randRotate(arc1)


###随机旋转 圆2
def arc2_randRotate():
    arc_randRotate(arc2)


###随机旋转 圆3
def arc3_randRotate():
    arc_randRotate(arc3)


# def arc_check_edge():
#    if
# def arc1_check_edge():
#    if
# def arc2_check_edge():
#    if
# def arc3_check_edge():
#    if


####随机移动函数
def arc_randmove(who, canvas_arc):
    for i in range(20):
        if random.randint(0, 5) < 3:  # 前进
            for j in range(10):
                arc_move(who, canvas_arc)
                # mycanvas.move(canvas_arctest,2,2)
                # canvas_arctest.move(mycanvas)
                time.sleep(0.05)
                if Start == False:
                    break
        if Start == False:
            break


def arc_randRotate(who):
    for i in range(10):
        if random.randint(0, 5) < 3:  # 转向
            for j in range(10):
                arc_Rotate_LR(who, random.randint(0, 2))
                time.sleep(0.05)
                if Start == False:
                    break
        if Start == False:
            break


##动作开始
threads = []


def action1():
    global Start
    Start = True
    # added_thread_check_edge = threading.Thread(target=arc_check_edge)
    # added_thread_check_edge.start()

    ##添加自动移动到线程
    added_thread1 = threading.Thread(target=arc1_randmove)
    # threads.append(added_thread1)
    added_thread1.start()
    added_thread1a = threading.Thread(target=arc1_randRotate)
    # threads.append(added_thread1a)
    added_thread1a.start()

    added_thread2 = threading.Thread(target=arc2_randmove)
    added_thread2.start()
    added_thread2a = threading.Thread(target=arc2_randRotate)
    added_thread2a.start()

    added_thread3 = threading.Thread(target=arc3_randmove)
    added_thread3.start()
    added_thread3a = threading.Thread(target=arc3_randRotate)
    added_thread3a.start()


def action1_stop():
    print(threading.current_thread())
    print(threading.active_count())
    global Start
    Start = False


# 初始化按键
moveButton = tk.Button(window, text='move', \
    command=action1)
moveButton.pack()

moveButton2 = tk.Button(window, text='stop', \
    command=action1_stop)
moveButton2.pack()
# for i in range(10):
#    time.sleep(0.1)
#    Rotate_arc1()

# 窗口循环刷新
window.mainloop()

