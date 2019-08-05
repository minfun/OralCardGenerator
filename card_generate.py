"""
1. 选择题型
    普通算式 x +/-/*// y
    类型算式1 x +/- y +/- z
    类型算式2 x +/- y * z
    类型算式3 x +/- y / z
2. 选择题量
3. 生成题目 / 打印题目
"""
import random

import wx
import os
import time

from student import math1, math2, math3, math4

'''
frame(窗口)：带标题和边框的最顶层窗体
panel(面板)：容器类，提供空间放其他组件，包括其他panel
'''
math_list = [math1, math2, math3, math4]


class MyApp(wx.App):

    def __init__(self):
        wx.App.__init__(self)
        self.selected_list = []
        self.math_list = []
        self.total_num = 40

    def OnInit(self):
        self.Frame = wx.Frame(parent=None, title="口算题卡生成器", pos=(100, 100), size=(300, 200))
        self.Frame.SetMaxSize((300, 300))
        self.Frame.SetMinSize((300, 300))
        self.SetTopWindow(self.Frame)
        self.panel = wx.Panel(self.Frame, -1)
        self.Set_Math_Type()
        self.Set_Add_Data_Button()
        self.Set_Generate_Button()
        self.Frame.Show()
        return True

    def Set_Generate_Button(self):
        print('set generate button')
        self.generate_button = wx.Button(self.panel, -1, "生成题目", pos=(150, 100), size=(150, 50))
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.generate_button.SetFont(font)
        self.generate_button.SetBackgroundColour("black")
        self.generate_button.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.generate_data, self.generate_button)

    def Set_Add_Data_Button(self):
        print('set add data button')
        self.add_data_button = wx.Button(self.panel, -1, "增加题目", pos=(0, 100), size=(150, 50))
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.add_data_button.SetFont(font)
        self.add_data_button.SetBackgroundColour("black")
        self.add_data_button.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.add_data, self.add_data_button)

    def Set_Math_Type(self):
        list1 = ["普通算式 x +/-/*// y", "类型算式1 x +/- y +/- z", "类型算式2 x +/- y * z", "类型算式3 x +/- y / z"]
        # self.mathlistbox1 = wx.ListBox(self.panel, -1, (-1, -1), (200, 60), list1, wx.LB_MULTIPLE)
        self.mathlistbox1 = wx.CheckListBox(self.panel, -1, (-1, -1), (300, 150), list1)
        # self.mathlistbox1.Bind(wx.EVT_CHECKLISTBOX, self.printselect1)
        self.mathlistbox1.Bind(wx.EVT_CHECKLISTBOX, self.printselect1)

    def generate_data(self, event):
        print("generate data")
        print(self.total_num)
        for i in range(int(self.total_num / 4)):
            for j in range(4):
                k = random.randint(0, len(self.math_list) - 1)
                self.math_list[k](1, 10)
            print('\n')

    def add_data(self, event):
        self.total_num += 40
        print(self.total_num)

    def printselect1(self, data):
        self.selected_list.append(data.GetInt())
        print(self.selected_list)
        self.math_list.append(math_list[data.GetInt()])
        print(self.math_list)


def loop_new():
    MyApp().MainLoop()


if __name__ == "__main__":
    loop_new()
