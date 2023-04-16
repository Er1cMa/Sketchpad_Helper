import tkinter as tk

import win32api
import win32con
import win32gui


# region button commands
def m00_save():
    file()
    press('S')


# def m10_choose():
# def m11_draw():
# def m20_new_point():
def m21_point_on_obj():
    construct()
    press('P')


def m22_split_merge_dot():
    edit()
    press('S')


def m23_intersection():
    construct()
    press('I')


def m24_midpoint():
    construct()
    press('M')


def m30_line():
    construct()
    press('L')


def m31_segment():
    construct()
    press('S')


def m32_ray():
    construct()
    press('Y')


def m33_vector():
    transform()
    press('V')


def m40_perpendicular():
    construct()
    press('D')


def m41_parallel():
    construct()
    press('E')


def m42_angle_bisector():
    construct()
    press('B')


def m43_trace():
    display()
    press('R')


def m50_polygonal():
    construct()
    press('N')


def m60_circle_by_center_point():
    construct()
    press('C')


def m61_circle_by_center_radius():
    construct()
    press('R')


def m62_external_arc():
    construct()
    press('3')


def m80_measure_angle():
    measure()
    press('A')


def m81_constant_angle():
    transform()
    press('A')


def m82_measure_distance():
    measure()
    press('D')


def m83_measure_area():
    measure()
    press('E')


def m84_measure_slope():
    measure()
    press('S')


def m90_reflect():
    transform()
    press('F')


# def m91_centrosym():
def m92_rotation():
    transform()
    press('R')


def m93_translation():
    transform()
    press('T')


# def ma0_move():
def ma1_delete_all():
    activate()
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    press('A')
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_DELETE, 0, 0, 0)
    win32api.keybd_event(win32con.VK_DELETE, 0, win32con.KEYEVENTF_KEYUP, 0)


def ma2_erase():
    activate()
    win32api.keybd_event(win32con.VK_DELETE, 0, 0, 0)
    win32api.keybd_event(win32con.VK_DELETE, 0, win32con.KEYEVENTF_KEYUP, 0)


# def ma3_zoom_in():
# def ma4_zoom_out():
def ma5_hide_obj():
    activate()
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    press('H')
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def ma6_label():
    display()
    press('L')


# endregion
gspwin = win32gui.FindWindow("GSP5MainWin", None)
hwin = tk.Tk()
hwin.title("Sketchpad Helper")
hwin.geometry("350x560") # 70x70
hwin.iconbitmap("resources/sketchpad icon.ico")
hwin.attributes("-topmost", 1)
focus_time = 0
execute_time = 0


# region control functions
def activate():
    if gspwin != 0:
        win32gui.SetForegroundWindow(gspwin)


def menu(char):
    activate()
    win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
    win32api.keybd_event(ord(char), 0, 0, 0)
    win32api.keybd_event(ord(char), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)


def press(char):
    win32api.keybd_event(ord(char), 0, 0, 0)
    win32api.keybd_event(ord(char), 0, win32con.KEYEVENTF_KEYUP, 0)


def file():
    menu('F')


def edit():
    menu('E')


def display():
    menu('D')


def construct():
    menu('C')


def transform():
    menu('T')


def measure():
    menu('M')


def number():
    menu('N')


def graph():
    menu('G')


def window():
    menu('W')


# endregion
# region import image resources
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
# endregion
# region set buttons
tk.Button(hwin, image=img_00Save, command=m00_save).grid(row=10, column=5)
# tk.Button(hwin, image=img_10Choose,command=m1).grid(row=2, column=1)
# tk.Button(hwin, image=img_11Draw).grid(row=2, column=2)
# tk.Button(hwin, image=img_20NewPoint).grid(row=3, column=1)
tk.Button(hwin, image=img_21PointOnObj, command=m21_point_on_obj).grid(row=3, column=1)
tk.Button(hwin, image=img_22SeparateMergeDot, command=m22_split_merge_dot).grid(row=3, column=2)
tk.Button(hwin, image=img_23Intersection, command=m23_intersection).grid(row=3, column=3)
tk.Button(hwin, image=img_24Midpoint, command=m24_midpoint).grid(row=3, column=4)
tk.Button(hwin, image=img_30Line, command=m30_line).grid(row=4, column=1)
tk.Button(hwin, image=img_31Segment, command=m31_segment).grid(row=4, column=2)
tk.Button(hwin, image=img_32Ray, command=m32_ray).grid(row=4, column=3)
tk.Button(hwin, image=img_33Vector, command=m33_vector).grid(row=4, column=4)
tk.Button(hwin, image=img_40Perpendicular, command=m40_perpendicular).grid(row=5, column=1)
tk.Button(hwin, image=img_41Parallel, command=m41_parallel).grid(row=5, column=2)
tk.Button(hwin, image=img_42AngleBisector, command=m42_angle_bisector).grid(row=5, column=3)
tk.Button(hwin, image=img_43Track, command=m43_trace).grid(row=5, column=4)
tk.Button(hwin, image=img_50Polygonal, command=m50_polygonal).grid(row=6, column=1)
tk.Button(hwin, image=img_60Circle_OD, command=m60_circle_by_center_point).grid(row=7, column=1)
tk.Button(hwin, image=img_61Circle_OR, command=m61_circle_by_center_radius).grid(row=7, column=2)
tk.Button(hwin, image=img_62ExternalArc, command=m62_external_arc).grid(row=7, column=3)
tk.Button(hwin, image=img_80MeasureAngle, command=m80_measure_angle).grid(row=8, column=1)
tk.Button(hwin, image=img_81ConstantAngle, command=m81_constant_angle).grid(row=8, column=2)
tk.Button(hwin, image=img_82MeasureDistance, command=m82_measure_distance).grid(row=8, column=3)
tk.Button(hwin, image=img_83MeasureArea, command=m83_measure_area).grid(row=8, column=4)
tk.Button(hwin, image=img_84MeasureSlope, command=m84_measure_slope).grid(row=8, column=5)
tk.Button(hwin, image=img_90Reflect, command=m90_reflect).grid(row=9, column=1)
# tk.Button(hwin, image=img_91Centrosym).grid(row=9, column=2)
tk.Button(hwin, image=img_92Rotation, command=m92_rotation).grid(row=9, column=2)
tk.Button(hwin, image=img_93Translation, command=m93_translation).grid(row=9, column=3)
# tk.Button(hwin, image=img_a0Move).grid(row=10, column=1)
tk.Button(hwin, image=img_a1Delete, command=ma1_delete_all).grid(row=10, column=1)
tk.Button(hwin, image=img_a2Erase, command=ma2_erase).grid(row=10, column=2)
# tk.Button(hwin, image=img_a3ZoomIn).grid(row=10, column=4)
# tk.Button(hwin, image=img_a4ZoomOut).grid(row=10, column=5)
tk.Button(hwin, image=img_a5HideObj, command=ma5_hide_obj).grid(row=10, column=3)
tk.Button(hwin, image=img_a6HideLabel, command=ma6_label).grid(row=10, column=4)
# endregion
hwin.mainloop()
