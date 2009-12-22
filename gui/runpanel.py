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

        ## Info bar with run button
        self.infopanel = wx.Panel(self, wx.ID_ANY)
        infopanelsizer = wx.FlexGridSizer(rows=1, cols=4, vgap=5, hgap=5)

        infopanelsizer.AddMany(
            [
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Name:'), 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'File:'), 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Commands:'), 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Estimated runtime:'), 1, wx.EXPAND),
            ]
        )


        self.infopanel.SetSizer(infopanelsizer, wx.EXPAND)

        sizer.Add(self.infopanel, 0, wx.EXPAND)
        sizer.Add(self.terminal, 1, wx.EXPAND)

        self.infopanel.Hide()
        return sizer