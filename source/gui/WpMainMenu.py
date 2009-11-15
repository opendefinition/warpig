## -*- coding: utf-8 -*
##---------------------------------------------------------------------------
##
## Class: WpMainMenu
## Desc: Class for managing the main menu of this application
##
##---------------------------------------------------------------------------
##
## Owner: Open Definition.
## Author: Roger C.B. Johnsen.
## License: Open Definiton General Lisence (ODGL). Available upon request.
##
##---------------------------------------------------------------------------

import wx

from gui.WpNewProject import WpNewProject
from gui.WpOpenProject import WpOpenProject
from gui.preferences.WpPreferences import WpPreferences

class WpMainMenu(wx.MenuBar):
    def __init__(self, parentFrame):
        wx.MenuBar.__init__(self)
        self.parentFrame = parentFrame
        self.Append(self.__setupFileMenu(), '&File')
        self.Append(self.__setupEditMenu(), '&Edit')
        self.Append(self.__setupEditMenu(), '&Edit')
	self.Append(self.__setupViewMenu(), '&View')
	self.Append(self.__setupPigletMenu(), '&Piglets')
	self.Append(self.__setupHelpMenu(), '&Help')

    ##--------------------------------------------------------------------------
    ## Menu structures
    ##--------------------------------------------------------------------------

    def __setupFileMenu(self):
        fileMenu = wx.Menu()

        openProject = wx.MenuItem(fileMenu, wx.ID_ANY, '&Open Project', 'Open project')
        newProject  = wx.MenuItem(fileMenu, wx.ID_ANY, '&New Project', 'Create new project')
	saveFileAs  = wx.MenuItem(fileMenu, wx.ID_ANY, '&Save File As', 'Save current file as...')
        openFile    = wx.MenuItem(fileMenu, wx.ID_ANY, '&Open File', 'Open file')
        saveFile    = wx.MenuItem(fileMenu, wx.ID_ANY, '&Save File', 'Save current file')
        newFile     = wx.MenuItem(fileMenu, wx.ID_ANY, '&New File', 'Create empty document')
	exit        = wx.MenuItem(fileMenu, wx.ID_ANY, '&Exit', 'Exit')

        fileMenu.AppendItem(newProject)
        fileMenu.AppendItem(openProject)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(newFile)
        fileMenu.AppendItem(openFile)
        fileMenu.AppendItem(saveFile)
        fileMenu.AppendItem(saveFileAs)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(exit)

        """
        self.parentFrame.Bind(wx.EVT_MENU, self.__onExit, id=exit.GetId())
	self.parentFrame.Bind(wx.EVT_MENU, self.__onNewProject, id=newProject.GetId())
	self.parentFrame.Bind(wx.EVT_MENU, self.__onOpenProject, id=openProject.GetId())

        ## @TODO: Fix this mangling of references
        self.parentFrame.Bind(wx.EVT_MENU, self.parentFrame.mainpanel._OnToolBarOpenPage, id=openFile.GetId())
	self.parentFrame.Bind(wx.EVT_MENU, self.parentFrame.mainpanel._OnToolBarNewPage, id=newFile.GetId())
	self.parentFrame.Bind(wx.EVT_MENU, self.parentFrame.mainpanel._OnToolBarSavePage, id=saveFile.GetId())
        """
        
        return fileMenu

    def __setupEditMenu(self):
        """
        Setup the edit menu
        """
        editMenu = wx.Menu()

        preferences = wx.MenuItem(editMenu, wx.ID_ANY, '&Preferences', 'Edit application preferences')

        # self.parentFrame.Bind(wx.EVT_MENU, self.__onPreferences, id=preferences.GetId())

	editMenu.AppendSeparator()
	editMenu.AppendItem(preferences)

        return editMenu

    def __setupViewMenu(self):
        """
        Setup the view menu
        """
        viewMenu = wx.Menu()
        return viewMenu

    def __setupPigletMenu(self):
        """
        Setup the piglet menu
        """
        pigletMenu = wx.Menu()
        return pigletMenu

    def __setupHelpMenu(self):
        """
        Setup the help menu
        """
        helpMenu = wx.Menu()
        
        seekHelp = wx.MenuItem(helpMenu, wx.ID_ANY, '&Help', 'Seek help')
        requestFeature = wx.MenuItem(helpMenu, wx.ID_ANY, 'Request feature', 'Request feature')
        reportBug = wx.MenuItem(helpMenu, wx.ID_ANY, 'Report bug', 'Submit bug')
        about = wx.MenuItem(helpMenu, wx.ID_ANY, '&About', 'About')

        helpMenu.AppendItem(seekHelp)
        helpMenu.AppendSeparator()
        helpMenu.AppendItem(requestFeature)
        helpMenu.AppendItem(reportBug)
        helpMenu.AppendSeparator()
        helpMenu.AppendItem(about)

        # self.parentFrame.Bind(wx.EVT_MENU, self.__onAbout, id=about.GetId())
        
        return helpMenu

    ##--------------------------------------------------------------------------
    ## Bind functions
    ##--------------------------------------------------------------------------

    def __onAbout(self, event):
        """
        Populates an about dialog and displays it
        """
        information = wx.AboutDialogInfo()

        information.SetName('Open Definition :: Warpig Code Environment')
        information.SetVersion('0.02 - Alpha Public')
        information.SetWebSite('http://www.opendefinition.com')
        information.SetCopyright('Open Definition(C)2009')
        information.AddDeveloper('Roger C.B. Johnsen')
        information.SetDescription('A simple but yet powerfull code evironment written in Python.')

        wx.AboutBox( information )

    def __onExit(self, event):
        """
        On exit event
        """
        dialog = wx.MessageDialog(
                            None,
                            'Are you sure to want to quit?',
                            'Question',
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
                        )

        status = dialog.ShowModal()

        if( status == wx.ID_YES ):
            dialog.Destroy()
            self.parentFrame.Close()
        else:
            dialog.Destroy()

    def __onPreferences(self, event):
        """
        Display the preference menu
        """
        preferences = WpPreferences()
	preferences.ShowModal()

    def __onNewProject( self, event ):
        """
        Display new project dialog window
        """

        None
        """
  	window = WpNewProject(self.parentFrame.mainpanel.leftsplit)
	window.ShowModal()
	window.Destroy()
        """

    def __onOpenProject( self, event ):
        """
        Display open project dialog window
        """
        None
        """
        window = WpOpenProject(self.parentFrame.mainpanel.leftsplit)
        window.ShowModal()
        """
