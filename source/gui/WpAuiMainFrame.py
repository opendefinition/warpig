import wx
import wx.aui

from gui.WpMainMenu import WpMainMenu

from gui.tree.WpTreeCtrl import WpTreeCtrl
from gui.WpNoteBook import WpNoteBook

from gui.buttons.mainbuttonpanel import MainButtonPanel

class WpAuiMainFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER)
        self.SetTitle( 'Open Definition :: Warpig Code Environment' )
    
        self.projecttree = WpTreeCtrl(self)
        self.notebook = WpNoteBook( self )

        self.__setup()

	self.Centre()
	self.Maximize()
	self.Show( True )

    def __setup(self):
        ## Menubar
	self.SetMenuBar(WpMainMenu(self))

        mainbuttonpanel = MainButtonPanel(self)


        self.__manager = wx.aui.AuiManager(self)

        ## Adding main button toolbar
        self.__manager.AddPane(
                mainbuttonpanel,
                wx.aui.AuiPaneInfo()
                    .CaptionVisible(False)
                    .Top()
                    .Gripper(False)
            )
        self.__manager.AddPane(self.notebook, wx.CENTER)
        self.__manager.AddPane(self.projecttree, wx.RIGHT, 'Project')
        self.__manager.Update()
        self.notebook.AddDefaultPage()

    def OnClose(self, event):
        # deinitialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()