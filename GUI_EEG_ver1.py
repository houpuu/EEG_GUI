# -*- coding: utf-8 -*-

import wx
import sys, os

APP_TITLE = u'WELCOME TO EEG WORLD'



class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()

    id_help = wx.NewId()
    id_about = wx.NewId()

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        self.Maximize()
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)

        self._CreateMenuBar()  # 菜单栏


    def _CreateMenuBar(self):
        '''创建菜单栏'''

        self.mb = wx.MenuBar()

        # 文件菜单
        m = wx.Menu()
        m.Append(self.id_open, u"打开文件")
        m.Append(self.id_save, u"保存文件")
        m.AppendSeparator()
        m.Append(self.id_quit, u"退出系统")
        self.mb.Append(m, u"文件")

        self.Bind(wx.EVT_MENU, self.OnOpen, id=self.id_open)
        self.Bind(wx.EVT_MENU, self.OnSave, id=self.id_save)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=self.id_quit)

        # 小波变换
        m = wx.Menu()
        m.Append(self.id_wavelet, u"小波变换")
        m.Append(self.id_save, u"保存文件")


        # 帮助菜单
        m = wx.Menu()
        m.Append(self.id_help, u"帮助主题")
        m.Append(self.id_about, u"关于...")
        self.mb.Append(m, u"帮助")

        self.Bind(wx.EVT_MENU, self.OnHelp, id=self.id_help)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.id_about)

        self.SetMenuBar(self.mb)





    def OnOpen(self, evt):
        '''打开文件'''

        self.sb.SetStatusText(u'打开文件', 1)

    def OnSave(self, evt):
        '''保存文件'''

        self.sb.SetStatusText(u'保存文件', 1)

    def OnQuit(self, evt):
        '''退出系统'''

        self.sb.SetStatusText(u'退出系统', 1)
        self.Destroy()

    def OnHelp(self, evt):
        '''帮助'''

        self.sb.SetStatusText(u'帮助', 1)

    def OnAbout(self, evt):
        '''关于'''

        self.sb.SetStatusText(u'关于', 1)


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True


if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()
