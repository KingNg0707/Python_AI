import tkinter as tk
import time
import math
import random
import threading
from arcs import gArc_1 as arcs

Start = False


def window_init():
    window = tk.Tk()
    window.title('tkinter test')
    window.geometry('400x400')
    return window


window = window_init()
mycanvas = tk.Canvas(window, bg='white', height=250, width=250)
mycanvas.pack()

arc_list = ["arc11", 20, 20, 20, 20, 120, 300, "red", 11], \
           ["arc12", 70, 70, 20, 20, 120, 300, "blue", 12], \
           ["arc13", 120, 120, 20, 20, 120, 300, "green", 13], \
           ["arc14", 170, 170, 20, 20, 120, 300, "yellow", 14]
arcst = [1, 2, 3, 4]
canvas_arcst = [1, 2, 3, 4]

# 初始化圆的值
for i in range(len(arc_list)):
    arcst[i] = arcs(name=arc_list[i][0], x=arc_list[i][1], y=arc_list[i][2], sx=arc_list[i][3], sy=arc_list[i][4],
                    start=arc_list[i][5], extent=arc_list[i][6], color=arc_list[i][7], index=arc_list[i][8])
    canvas_arcst[i] = mycanvas.create_arc(arcst[i].xy, arcst[i].xy[0] + arcst[i].size[0],
                                          arcst[i].xy[1] + arcst[i].size[1], start=arcst[i].startC,
                                          extent=arcst[i].extentC, fill=arcst[i].color)

arc1 = arcs("arc1", 10, 10, 20, 20, 120, 300, "black", 1)
arc2 = arcs("arc2", 60, 60, 20, 20, 120, 300, "black", 2)
arc3 = arcs("arc3", 110, 110, 20, 20, 120, 300, "black", 3)
arc4 = arcs("arc4", 160, 160, 20, 20, 120, 300, "black", 4)
# 创建空间
# [a*b for a, b in zip(arc1_xy,arc1_size)]

# 创建3个圆形
canvas_arc1 = mycanvas.create_arc(arc1.xy, arc1.xy[0] + arc1.size[0], arc1.xy[1] + arc1.size[1], start=arc1.startC,
                                  extent=arc1.extentC, fill=arc1.color)
canvas_arc2 = mycanvas.create_arc(arc2.xy, arc2.xy[0] + arc2.size[0], arc2.xy[1] + arc2.size[1], start=arc2.startC,
                                  extent=arc2.extentC, fill=arc2.color)
canvas_arc3 = mycanvas.create_arc(arc3.xy, arc3.xy[0] + arc3.size[0], arc3.xy[1] + arc3.size[1], start=arc3.startC,
                                  extent=arc3.extentC, fill=arc3.color)
canvas_arc4 = mycanvas.create_arc(arc4.xy, arc4.xy[0] + arc4.size[0], arc4.xy[1] + arc4.size[1], start=arc4.startC,
                                  extent=arc4.extentC, fill=arc4.color)


#####移动一个圆
def arc_move(who, canvas_arc):
    # 旋转角度坐标移动的计算
    x = 1 * math.sin(math.radians(who.startC - 30 + 270))
    y = 1 * math.cos(math.radians(who.startC - 30 + 270))
    mycanvas.move(canvas_arc, x, y)

    who.xy[0] += x
    who.xy[1] += y


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
    elif who.index == 11:
        # global canvas_arcst[0]
        mycanvas.delete(canvas_arcst[0])
        canvas_arcst[0] = mycanvas.create_arc(who.xy, who.xy[0] + who.size[0], who.xy[1] + who.size[1],
                                              start=who.startC,
                                              extent=who.extentC, fill=who.color)


###随机移动 圆1
def arc1_randmove():
    arc_randmove(arc1, canvas_arc1)
    # print(arc_check_place(arc1))
    # print(arc_check_Rotate(arc1))

    # arc_randRotate(arc1)


###随机移动 圆2
def arc2_randmove():
    arc_randmove(arc2, canvas_arc2)
    # arc_randRotate(arc2)


###随机移动 圆3
def arc3_randmove():
    arc_randmove(arc3, canvas_arc3)
    # arc_randRotate(arc3)


def arc4_randmove():
    arc_randmove(arc4, canvas_arc4)


def arcs_randmove():
    arc_randmove(arcst[0], canvas_arcst[0])


###随机旋转 圆1
def arc1_randRotate():
    arc_randRotate(arc1)


###随机旋转 圆2
def arc2_randRotate():
    arc_randRotate(arc2)


###随机旋转 圆3
def arc3_randRotate():
    arc_randRotate(arc3)


def arcs_randRotate():
    arc_randRotate(arcst[0])


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


def arc_check_place(who):
    return who.xy


def arc_check_Rotate(who):
    return who.startC


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

    added_thread4 = threading.Thread(target=arc4_randmove)
    added_thread4.start()

    added_thread5 = threading.Thread(target=arcs_randmove)
    added_thread5.start()
    added_thread5a = threading.Thread(target=arcs_randRotate)
    added_thread5a.start()


def action1_stop():
    print(threading.current_thread())
    print(threading.active_count())
    global Start
    Start = False


# 初始化按键
moveButton = tk.Button(window, text='move', command=action1)
moveButton.pack()

moveButton2 = tk.Button(window, text='stop', command=action1_stop)
moveButton2.pack()
# for i in range(10):
#    time.sleep(0.1)
#    Rotate_arc1()

# 窗口循环刷新
window.mainloop()
