import wx
import wx.aui

from wx.lib.pubsub import Publisher as pub
from gui.WpMainMenu import WpMainMenu
from gui.tree.WpTreeCtrl import WpTreeCtrl
from gui.WpNoteBook import WpNoteBook
from gui.preferences.WpPreferences import WpPreferences
from gui.buttons.mainbuttonpanel import MainButtonPanel



class WpAuiMainFrame(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER)
        self.SetTitle( 'Open Definition :: Warpig Code Environment' )
    
        self.projecttree    = WpTreeCtrl(self)
        self.notebook       = WpNoteBook(self)
        self.preferences    = WpPreferences(self)

        self.__setup()

	self.Centre()
	self.Maximize()
	self.Show( True )

        pub.subscribe(self.__showPaneSubscriber, 'mainframe.showpane')
        pub.subscribe(self.__setPaneCaption, 'mainframe.setpanetitle')

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
        self.__manager.AddPane(
                            self.projecttree,
                            wx.aui.AuiPaneInfo()
                                .Name("project")
                                .Caption("Project tree")
                                .Right()
                                .BottomDockable(False)
                                .TopDockable(False)
                        )

        self.__manager.AddPane(
                            self.preferences,
                            wx.aui.AuiPaneInfo()
                                .Name("settings")
                                .Caption("Warpig Settings")
                                .Dockable(False)
                                .Float()
                                .Hide()
                                .Center()
                                .MinimizeButton(True))

        self.__manager.Update()
        self.notebook.AddDefaultPage()

    def OnClose(self, event):
        # deinitialize the frame manager
        self._mgr.UnInit()
        # delete the frame
        self.Destroy()

    def __showPaneSubscriber(self, message):
        self.__manager.GetPane(message.data).Show()
        self.__manager.Update()

    def __setPaneCaption(self, message):
        pane_name = message.data['pane']
        caption = message.data['caption']

        pane = self.__manager.GetPane(pane_name)
        pane.Caption('Project: ' + str(caption))

        self.__manager.Update()