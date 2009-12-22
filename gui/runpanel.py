import wx

from wx.lib.pubsub import Publisher as pub

class Runpanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = self.setup(sizer)
        self.SetSizer(sizer)

        pub.subscribe(self.showcommands, 'run.commands')

    def setup(self, sizer):
        self.terminal = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_RICH)
        self.terminal.SetBackgroundColour("#000000")
        self.terminal.SetForegroundColour('#99CC00')

        ## Info bar with run button
        self.infopanel = wx.Panel(self, wx.ID_ANY)
        infopanelsizer = wx.FlexGridSizer(rows=4, cols=2, vgap=5, hgap=5)

        self.filenamelbl = wx.StaticText(self.infopanel, wx.ID_ANY, '')
        self.filelbl = wx.StaticText(self.infopanel, wx.ID_ANY, '')
        self.commandslbl = wx.StaticText(self.infopanel, wx.ID_ANY, '')
        self.runtimelbl = wx.StaticText(self.infopanel, wx.ID_ANY, '')

        infopanelsizer.AddMany(
            [
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Name:'), 1, wx.EXPAND),
                (self.filenamelbl, 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'File:'), 1, wx.EXPAND),
                (self.filelbl, 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Commands:'), 1, wx.EXPAND),
                (self.commandslbl, 1, wx.EXPAND),
                (wx.StaticText(self.infopanel, wx.ID_ANY, 'Estimated runtime:'), 1, wx.EXPAND),
                (self.runtimelbl, 1, wx.EXPAND)
            ]
        )


        self.infopanel.SetSizer(infopanelsizer, wx.EXPAND)

        sizer.Add(self.infopanel, 0, wx.EXPAND)
        sizer.Add(self.terminal, 1, wx.EXPAND)

        return sizer

    def showcommands(self, message):
        data = message.data
        metadata = data['metadata']

        self.filelbl.SetLabel(str(metadata['file']))
        self.filenamelbl.SetLabel(str(metadata['suite']))
        self.commandslbl.SetLabel(str(metadata['commands']))
        self.runtimelbl.SetLabel(str(metadata['sleeptime']))



