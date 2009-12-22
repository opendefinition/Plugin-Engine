import wx

from gui.mainframe import Mainframe

class Application(wx.App):
    def OnInit(self):
        frame = Mainframe(None)
        frame.Centre()
        frame.Show(True)
        self.SetTopWindow(frame)

        return True