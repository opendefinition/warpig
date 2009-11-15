import wx

from wx.lib.agw import aui as aui

class MainButtonPanel(aui.AuiToolBar):
    def __init__(self, parent):
        aui.AuiToolBar.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        self.__setup()

    def __setup(self):

        self.AddSimpleTool(wx.ID_ANY, "New", wx.Bitmap("./gui/icons/document-new.png"))
        self.AddSimpleTool(wx.ID_ANY, "Open", wx.Bitmap("./gui/icons/folder.png"))
        self.AddSimpleTool(wx.ID_ANY, "Save", wx.Bitmap("./gui/icons/media-floppy.png"))

        self.Realize()