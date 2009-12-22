import wx
from lib.command import Command
from wx.lib.pubsub import Publisher as pub

class Suitespanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        ## Helper methods
        self.command = Command()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = self.setup(sizer)
        self.SetSizer(sizer)

        ## Subscriptions
        pub.subscribe(self.populatelist, 'suiteslist.populate')

    def setup(self, sizer):
        self.suiteslist = wx.ListBox(self, wx.ID_ANY)

        ## Registering widgets
        sizer.Add(self.suiteslist, 1, wx.EXPAND)

        return sizer

    ##--------------------------------------------------------------------------
    ## Subscription handlers
    ##--------------------------------------------------------------------------

    def populatelist(self, message):
        list = self.command.getCommandSuites()
        self.suiteslist.InsertItems(list, 0)