# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os.path

wx.ID_Open = 1000
wx.ID_Save = 1001
wx.ID_SaveAs = 1002
wx.ID_Exit = 1003
wx.ID_About1 = 1004


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"", pos=wx.DefaultPosition, size=wx.Size(728, 457),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_File = wx.Menu()
        self.m_Open = wx.MenuItem(self.m_File, wx.ID_Open, u"打开", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Open)

        self.m_Save = wx.MenuItem(self.m_File, wx.ID_Save, u"保存", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Save)

        self.m_SaveAs = wx.MenuItem(self.m_File, wx.ID_SaveAs, u"另存", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_SaveAs)

        self.m_File.AppendSeparator()

        self.m_Exit = wx.MenuItem(self.m_File, wx.ID_Exit, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_Exit)

        self.m_menubar1.Append(self.m_File, u"文件")

        self.m_About = wx.Menu()
        self.m_About1 = wx.MenuItem(self.m_About, wx.ID_About1, u"关于...", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_About.Append(self.m_About1)

        self.m_menubar1.Append(self.m_About, u"关于")

        self.SetMenuBar(self.m_menubar1)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_Text1 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        bSizer1.Add(self.m_Text1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events

        self.Bind(wx.EVT_MENU, self.m_OpenClick, id=self.m_Open.GetId())
        self.Bind(wx.EVT_MENU, self.m_SaveClick, id=self.m_Save.GetId())
        self.Bind(wx.EVT_MENU, self.m_SaveAsClick, id=self.m_SaveAs.GetId())
        self.Bind(wx.EVT_MENU, self.m_ExitClick, id=self.m_Exit.GetId())
        self.Bind(wx.EVT_MENU, self.m_About1Click, id=self.m_About1.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_OpenClick(self, event):
        pass

    def m_SaveClick(self, event):
        pass

    def m_SaveAsClick(self, event):
        pass

    def m_ExitClick(self, event):
        pass

    def m_About1Click(self, event):
        pass


class MainWindow(MyFrame1):
    def __init__(self, parent, filename='noname.txt'):
        self.filename = filename
        self.dirname = '.'
        MyFrame1.__init__(self, parent)

    def SetTitle(self):
        # MainWindow.SetTitle overrides wx.Frame.SetTitle, so we have to
        # call it using super:
        super(MainWindow, self).SetTitle('Editor %s' % self.filename)

    def defaultFileDialogOptions(self):
        ''' Return a dictionary with file dialog options that can be
            used in both the save file dialog as well as in the open
            file dialog. '''
        return dict(message='Choose a file', defaultDir=self.dirname, wildcard='*.*')

    def askUserForFilename(self, **dialogOptions):
        dialog = wx.FileDialog(self, **dialogOptions)
        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.filename = dialog.GetFilename()
            self.dirname = dialog.GetDirectory()
            self.SetTitle()  # Update the window title with the new filename
        else:
            userProvidedFilename = False
        dialog.Destroy()
        return userProvidedFilename

    def m_About1Click(self, event):
        dialog = wx.MessageDialog(self, 'A sample editor in wxPython', 'About Sample Editor', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def m_ExitClick(self, event):
        self.Close()

    def m_OpenClick(self, event):
        if self.askUserForFilename(style=wx.FD_OPEN, **self.defaultFileDialogOptions()):
            textfile = open(os.path.join(self.dirname, self.filename), 'r', encoding='iso-8859-1')
            data = textfile.read()
            data = data.encode('iso-8859-1').decode('utf-8')
            self.m_Text1.SetValue(data)
            textfile.close()

    def m_SaveClick(self, event):
        textfile = open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8')
        textfile.write(self.m_Text1.GetValue())
        textfile.close()

    def m_SaveAsClick(self, event):
        if self.askUserForFilename(style=wx.FD_SAVE, **self.defaultFileDialogOptions()):
            self.m_SaveClick(event)


if __name__ == '__main__':
    app = wx.App()
    main_win = MainWindow(None)
    main_win.Show()
    app.MainLoop()


