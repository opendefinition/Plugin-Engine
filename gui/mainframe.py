import wx
import wx.aui

class Mainframe(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER)
        self.CreateStatusBar()
        self.auimanager = wx.aui.AuiManager(self)
        self.setup()
        self.auimanager.Update()

    def setup(self):
        None
