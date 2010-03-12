import wx
from wx.lib.agw import aui as aui
from gui.guid.guid import *

class MainButtonPanel(aui.AuiToolBar):
    def __init__(self, parent):
        aui.AuiToolBar.__init__(self, parent, CONST_PANE_MAIN_BUTTONS, wx.DefaultPosition, wx.DefaultSize, aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        self.__setup()

    def __setup(self):

        self.AddSimpleTool(CONST_WIDGET_BUTTON_NEW, "New", wx.Bitmap("./gui/icons/page.png"))
        self.AddSimpleTool(CONST_WIDGET_BUTTON_OPEN, "Open", wx.Bitmap("./gui/icons/folder.png"))
        self.AddSimpleTool(CONST_WIDGET_BUTTON_SAVE, "Save", wx.Bitmap("./gui/icons/save.png"))

        self.Realize()