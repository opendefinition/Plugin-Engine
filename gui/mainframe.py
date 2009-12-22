import wx
import wx.aui

from gui.runpanel import Runpanel
from gui.suitespanel import Suitespanel
from wx.lib.pubsub import Publisher as pub

class Mainframe(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER)
        self.CreateStatusBar()
        self.auimanager = wx.aui.AuiManager(self)
        self.setup()
        self.auimanager.Update()

        ## Populate widgets with data
        pub.sendMessage('suiteslist.populate', True)

    def setup(self):
        ## Widgets
        self.suitespanel = Suitespanel(self)
        self.runpanel = Runpanel(self)

        ## Left panel
        self.auimanager.AddPane(
                            self.suitespanel,
                            wx.aui.AuiPaneInfo()
                                .Name('suitespanel')
                                .Caption('Suites')
                                .CloseButton(False)
                                .MaximizeButton(False)
                                .MinimizeButton(False)
                                .Left()
                        )

        ## Center panel
        self.auimanager.AddPane(
                    self.runpanel,
                    wx.aui.AuiPaneInfo()
                        .Name('runpanel')
                        .Caption('Run')
                        .CloseButton(False)
                        .MaximizeButton(False)
                        .MinimizeButton(False)
                        .Center()
                )