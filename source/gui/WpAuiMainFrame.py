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

        self.Bind(wx.EVT_CLOSE, self.onCloseApplication)

    def onCloseApplication(self, event):
        self.closeApplication()

    def closeApplication(self):
        dialog = wx.MessageDialog(
                                None,
                                'Are you sure you want to quit?',
                                'Question',
                                 wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
                            )

        status = dialog.ShowModal()

        if status == wx.ID_YES:
            ## Save notebook state (opened tabs)
            pub.sendMessage('notebook.savetabstate', True)

            ## De-initialize the frame manager
            self.__manager.UnInit()

            ## Delete the frame
            self.Destroy()
        else:
            dialog.Destroy()

    def __setup(self):
        ## Menubar
        self.SetMenuBar(WpMainMenu(self))

        mainbuttonpanel = MainButtonPanel(self)

        self.__manager = wx.aui.AuiManager(self)

        ## We always need a statusbar
        self.CreateStatusBar()

        ## Adding main button toolbar
        self.__manager.AddPane(
                mainbuttonpanel,
                wx.aui.AuiPaneInfo()
                    .CaptionVisible(False)
                    .Top()
                    .Gripper(False)
                        )

        self.__manager.AddPane(
                            self.notebook,
                            wx.aui.AuiPaneInfo()
                                .Name("notebook")
                                .Caption("Notebook")
                                .CaptionVisible(False)
                                .CloseButton(False)
                                .MaximizeButton(False)
                                .MinimizeButton(False)
                                .Center()
                        )

        self.__manager.AddPane(
                            self.projecttree,
                            wx.aui.AuiPaneInfo()
                                .Name("project")
                                .Caption("Project tree")
                                .CloseButton(False)
                                .Right()
                                .Hide()
                                .BottomDockable(False)
                                .TopDockable(False)
                                .MinSize((200,200))
                        )

        self.__manager.AddPane(
                            self.preferences,
                            wx.aui.AuiPaneInfo()
                                .Name("settings")
                                .Caption("Warpig Settings")
                                .Dockable(False)
                                .Float()
                                .Hide()
                                .MinimizeButton(True))

        self.__manager.Update()

        if self.notebook.openTabs() == 0:
            self.notebook.AddDefaultPage()

    def __showPaneSubscriber(self, message):
        self.__manager.GetPane(message.data).Show()
        self.__manager.Update()

    def __setPaneCaption(self, message):
        pane_name = message.data['pane']
        caption = message.data['caption']

        pane = self.__manager.GetPane(pane_name)
        pane.Caption('Project: ' + str(caption))

        self.__manager.Update()