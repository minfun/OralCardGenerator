import wx

'''
frame(窗口)：带标题和边框的最顶层窗体
panel(面板)：容器类，提供空间放其他组件，包括其他panel
'''


class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        # 创建一个Panel实例
        pn1 = wx.Panel(self)

        # 在pn1上创建一个静态文本组件(StaticText)
        # +label表示要显示的文本内容
        # +pos表示文本显示位置
        st = wx.StaticText(pn1, label="A simple wxPython demo!", pos=(25, 25))

        # 设置文本内容字号并粗体显示
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # 创建菜单栏
        self.makeMenuBar()
        # 创建状态栏
        self.CreateStatusBar()
        # 设置状态栏要显示的文本内容
        self.SetStatusText("Ready to update to Hello World v3.0!")

    def makeMenuBar(self):
        # 创建菜单对象fileMenu(菜单栏主选项1)
        fileMenu = wx.Menu()

        # 在fileMenu中添加子项createItem
        # +item表示子项
        # +helpString表示对子项的说明，当鼠标移动到子项上时，会在状态栏显示
        # \t...语法允许用户键盘操作触发子项
        createItem = fileMenu.Append(wx.ID_ANY, item=u"新建文件(N)...\tCtrl-H", helpString="创建一个新的文件")

        # 在各子项中添加起分隔作用的横线
        fileMenu.AppendSeparator()

        # 在fileMenu中添加子项exitItem
        exitItem = fileMenu.Append(wx.ID_EXIT, item=u"退出")

        # 创建菜单对象helpMenu(菜单栏主选项2)
        helpMenu = wx.Menu()
        # 在fileMenu中添加子项aboutItem
        aboutItem = helpMenu.Append(wx.ID_ABOUT, item=u"关于")

        # 创建菜单栏
        menuBar = wx.MenuBar()
        # 添加各个菜单栏主选项到菜单栏中
        # "&"后的首字母+"alt"键触发菜单选项。该首字母会以下划线着重显示，按住alt键即能看见。
        menuBar.Append(fileMenu, u"文件(&F)")
        menuBar.Append(helpMenu, u"帮助(&H)")
        # 添加菜单栏到窗口
        self.SetMenuBar(menuBar)

        # 将主菜单的所有子项绑定动作
        self.Bind(wx.EVT_MENU, self.OnCreate, source=createItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, source=aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, source=exitItem)

    def OnExit(self, event):
        # 关闭窗口
        self.Close(True)

    def OnCreate(self, event):
        wx.MessageBox(u"创建文件成功")

    def OnAbout(self, event):
        # MessageBox(message, caption=MessageBoxCaptionStr, style=OK|CENTRE, parent=None, x=DefaultCoord, y=DefaultCoord)
        # +调用message()方法将会弹出一个对话窗口
        # +message表示对话窗口显示的正文信息
        # +caption表示对话窗口的标题
        # +style表示对话窗口的按钮和图标样式
        wx.MessageBox("Hello World v2.0\r\nproducted by wxPython.",
                      "About",
                      wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App()
    frame = HelloFrame(None, title="Hello World v2.0")
    frame.Show()
    app.MainLoop()