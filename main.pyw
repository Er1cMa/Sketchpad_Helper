import tkinter as tk
from tkinter import messagebox
import win32con
import win32gui
import win32api
import time

'''
def save():
    # 00
def choose():
    # 10
def draw():
    # 11
def new_point():
    # 20
def point_on_obj():
    # 21
def separate_merge_dot():
    # 22
def intersection():
    # 23
def midpoint():
    # 24
def line():
    # 30
def segment():
    # 31
def ray():
    # 32
def vector():
    # 33
def perpendicular():
    # 40
def parallel():
    # 41
def angle_bisector():
    # 42
def track():
    # 43
def polygonal():
    # 50
def circle_od():
    # 60
def circle_or():
    # 61
def external_arc():
    # 62
def measure_angle():
    # 80
def constant_angle():
    # 81
def measure_distance():
    # 82
def measure_area():
    # 83
def measure_slope():
    # 84
def reflect():
    # 90
def centrosym():
    # 91
def rotation():
    # 92
def translation():
    # 93
def move():
    # a0
def delete():
    # a1
def erase():
    # a2
def zoom_in():
    # a3
def zoom_out():
    # a4
def hide_obj():
    # a5
def hide_label():
    # a6
'''

gspwin = win32gui.FindWindow("GSP5MainWin", None)
hwin = tk.Tk()
hwin.title("Sketchpad Helper")
hwin.geometry("760x760")  # 490x700
hwin.iconbitmap("resources/sketchpad icon.ico")
focus_time = 0
execute_time = 0


# tk.Label(hwin, text="Sketchpad Helper", font=("Microsoft YaHei UI", 10)).grid(row=0,column=8)
# MUST remember to grid anything.
def test():
    if gspwin != 0:
        # 将应用程序窗口激活
        win32gui.SetForegroundWindow(gspwin)
        time.sleep(focus_time)
        # 发送Alt+C击键
        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)  # 按下Alt键
        win32api.keybd_event(ord('C'), 0, 0, 0)  # 按下C键
        win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开C键
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开Alt键

        # 等待一段时间，让菜单栏弹出
        time.sleep(execute_time)

        # 发送<M>击键
        win32api.keybd_event(ord('M'), 0, 0, 0)  # 按下<M>键
        win32api.keybd_event(ord('M'), 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开<M>键
        # print("GSP hWnd =", gspwin, ". Function proceeded successfully.")
        messagebox.showinfo(title='Maybe Success?',
                            message="GSP hWnd =" + str(gspwin) + ". Function proceeded successfully.\n"
                                                                 "Please check your Sketchpad!\n If there is any "
                                                                 "problem, please do the checklist below:\n1. Have "
                                                                 "you selected a SEGMENT? If not, select one and try "
                                                                 "again.\n2. Have you clicked the main window after "
                                                                 "clicking the button? If yes, don't click and try "
                                                                 "again. !!! If you've checked all above and still "
                                                                 "find problems, plz contact @Er1cMa.")


img_00Save = tk.PhotoImage(file="resources/ggb64x64icon/00Save.png")
img_10Choose = tk.PhotoImage(file="resources/ggb64x64icon/10Choose.png")
img_11Draw = tk.PhotoImage(file="resources/ggb64x64icon/11Draw.png")
img_20NewPoint = tk.PhotoImage(file="resources/ggb64x64icon/20NewPoint.png")
img_21PointOnObj = tk.PhotoImage(file="resources/ggb64x64icon/21PointOnObj.png")
img_22SeparateMergeDot = tk.PhotoImage(file="resources/ggb64x64icon/22SeparateMergeDot.png")
img_23Intersection = tk.PhotoImage(file="resources/ggb64x64icon/23Intersection.png")
img_24Midpoint = tk.PhotoImage(file="resources/ggb64x64icon/24Midpoint.png")
img_30Line = tk.PhotoImage(file="resources/ggb64x64icon/30Line.png")
img_31Segment = tk.PhotoImage(file="resources/ggb64x64icon/31Segment.png")
img_32Ray = tk.PhotoImage(file="resources/ggb64x64icon/32Ray.png")
img_33Vector = tk.PhotoImage(file="resources/ggb64x64icon/33Vector.png")
img_40Perpendicular = tk.PhotoImage(file="resources/ggb64x64icon/40Perpendicular.png")
img_41Parallel = tk.PhotoImage(file="resources/ggb64x64icon/41Parallel.png")
img_42AngleBisector = tk.PhotoImage(file="resources/ggb64x64icon/42AngleBisector.png")
img_43Track = tk.PhotoImage(file="resources/ggb64x64icon/43Track.png")
img_50Polygonal = tk.PhotoImage(file="resources/ggb64x64icon/50Polygonal.png")
img_60Circle_OD = tk.PhotoImage(file="resources/ggb64x64icon/60Circle_OD.png")
img_61Circle_OR = tk.PhotoImage(file="resources/ggb64x64icon/61Circle_OR.png")
img_62ExternalArc = tk.PhotoImage(file="resources/ggb64x64icon/62ExternalArc.png")
img_80MeasureAngle = tk.PhotoImage(file="resources/ggb64x64icon/80MeasureAngle.png")
img_81ConstantAngle = tk.PhotoImage(file="resources/ggb64x64icon/81ConstantAngle.png")
img_82MeasureDistance = tk.PhotoImage(file="resources/ggb64x64icon/82MeasureDistance.png")
img_83MeasureArea = tk.PhotoImage(file="resources/ggb64x64icon/83MeasureArea.png")
img_84MeasureSlope = tk.PhotoImage(file="resources/ggb64x64icon/84MeasureSlope.png")
img_90Reflect = tk.PhotoImage(file="resources/ggb64x64icon/90Reflect.png")
img_91Centrosym = tk.PhotoImage(file="resources/ggb64x64icon/91Centrosym.png")
img_92Rotation = tk.PhotoImage(file="resources/ggb64x64icon/92Rotation.png")
img_93Translation = tk.PhotoImage(file="resources/ggb64x64icon/93Translation.png")
img_a0Move = tk.PhotoImage(file="resources/ggb64x64icon/a0Move.png")
img_a1Delete = tk.PhotoImage(file="resources/ggb64x64icon/a1Delete.png")
img_a2Erase = tk.PhotoImage(file="resources/ggb64x64icon/a2Erase.png")
img_a3ZoomIn = tk.PhotoImage(file="resources/ggb64x64icon/a3ZoomIn.png")
img_a4ZoomOut = tk.PhotoImage(file="resources/ggb64x64icon/a4ZoomOut.png")
img_a5HideObj = tk.PhotoImage(file="resources/ggb64x64icon/a5HideObj.png")
img_a6HideLabel = tk.PhotoImage(file="resources/ggb64x64icon/a6HideLabel.png")
tk.Label(hwin, text="Try Midpoint Button.").grid(row=0)
tk.Button(hwin, image=img_00Save).grid(row=1, column=1)
tk.Button(hwin, image=img_10Choose).grid(row=2, column=1)
tk.Button(hwin, image=img_11Draw).grid(row=2, column=2)
tk.Button(hwin, image=img_20NewPoint).grid(row=3, column=1)
tk.Button(hwin, image=img_21PointOnObj).grid(row=3, column=2)
tk.Button(hwin, image=img_22SeparateMergeDot).grid(row=3, column=3)
tk.Button(hwin, image=img_23Intersection).grid(row=3, column=4)
tk.Button(hwin, image=img_24Midpoint, command=test).grid(row=3, column=5)
tk.Button(hwin, image=img_30Line).grid(row=4, column=1)
tk.Button(hwin, image=img_31Segment).grid(row=4, column=2)
tk.Button(hwin, image=img_32Ray).grid(row=4, column=3)
tk.Button(hwin, image=img_33Vector).grid(row=4, column=4)
tk.Button(hwin, image=img_40Perpendicular).grid(row=5, column=1)
tk.Button(hwin, image=img_41Parallel).grid(row=5, column=2)
tk.Button(hwin, image=img_42AngleBisector).grid(row=5, column=3)
tk.Button(hwin, image=img_43Track).grid(row=5, column=4)
tk.Button(hwin, image=img_50Polygonal).grid(row=6, column=1)
tk.Button(hwin, image=img_60Circle_OD).grid(row=7, column=1)
tk.Button(hwin, image=img_61Circle_OR).grid(row=7, column=2)
tk.Button(hwin, image=img_62ExternalArc).grid(row=7, column=3)
tk.Button(hwin, image=img_80MeasureAngle).grid(row=8, column=1)
tk.Button(hwin, image=img_81ConstantAngle).grid(row=8, column=2)
tk.Button(hwin, image=img_82MeasureDistance).grid(row=8, column=3)
tk.Button(hwin, image=img_83MeasureArea).grid(row=8, column=4)
tk.Button(hwin, image=img_84MeasureSlope).grid(row=8, column=5)
tk.Button(hwin, image=img_90Reflect).grid(row=9, column=1)
tk.Button(hwin, image=img_91Centrosym).grid(row=9, column=2)
tk.Button(hwin, image=img_92Rotation).grid(row=9, column=3)
tk.Button(hwin, image=img_93Translation).grid(row=9, column=4)
tk.Button(hwin, image=img_a0Move).grid(row=10, column=1)
tk.Button(hwin, image=img_a1Delete).grid(row=10, column=2)
tk.Button(hwin, image=img_a2Erase).grid(row=10, column=3)
tk.Button(hwin, image=img_a3ZoomIn).grid(row=10, column=4)
tk.Button(hwin, image=img_a4ZoomOut).grid(row=10, column=5)
tk.Button(hwin, image=img_a5HideObj).grid(row=10, column=6)
tk.Button(hwin, image=img_a6HideLabel).grid(row=10, column=7)

"""
tk.Label(hwin, text="Time from setting focus on sketchpad to activate menu bar = ").grid(row=11, column=1)
tk.Label(hwin, text="Time from activating menu bar to send keys = ").grid(row=12, column=1)
# 创建输入框控件
focus_input = tk.Entry(hwin)
# 放置输入框，并设置位置
focus_input.grid(row=11, column=2)
focus_input.delete(0, "end")
# 插入默认文本
focus_input.insert(0, "1.00")
execute_input = tk.Entry(hwin)
execute_input.grid(row=12, column=2)
execute_input.delete(0, "end")
execute_input.insert(0, "1.00")


def send_change_time_com():
    global focus_time
    global execute_time
    focus_time = float(focus_input.get())
    execute_time = float(execute_input.get())


tk.Button(hwin, text="Change focus/execute time.", command=send_change_time_com).grid(row=13)
"""
hwin.mainloop()
