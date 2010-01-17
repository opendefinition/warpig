import wx

from gui.preferences.WpEditorSettings import WpEditorSettings
from gui.preferences.WpProjectsSettings import WpProjectsSettings

class WpPreferenceTree(wx.Treebook):
    def __init__(self, parent, id ):
        wx.Treebook.__init__(self, parent, id, style=wx.BK_DEFAULT|wx.EXPAND, size=(500, 480))
        self.Setup()

    def Setup( self ):
        ## Adding pages
        panelGeneral = wx.Panel(self, wx.ID_ANY)
        panelProjects = wx.Panel(self, wx.ID_ANY)

        ## Editor settings subpage
        self.AddPage(panelGeneral, "General")
        self.AddSubPage(WpEditorSettings(self), text="Editor")

        ## Project settings subpage
        self.AddPage(panelProjects, "Projects")
        self.AddSubPage(WpProjectsSettings(self), text="Excludes")

        wx.FutureCall( 100, self.AdjustSize )

    def AdjustSize(self):
        self.GetTreeCtrl().InvalidateBestSize()
        self.SendSizeEvent()