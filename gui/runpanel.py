import wx
import wx.richtext

class Runpanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = self.setup(sizer)
        self.SetSizer(sizer)

    def setup(self, sizer):
        self.terminal = wx.richtext.RichTextCtrl(self, wx.ID_ANY)

        sizer.Add(self.terminal, 1, wx.EXPAND)
        return sizer