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
from gui.guid.guid import *
from system.WpDatabaseAPI import WpDatabaseAPI
from wx.lib.pubsub import Publisher as pub
import sys

class WpMainMenu(wx.MenuBar):
	def __init__(self, parentFrame):
		pub.subscribe(self.openFileSubscriber, 'mainmenu.openfile')
		pub.subscribe(self.rebuildRecentProjects, 'mainmenu.rebuildrecentprojects')

		self.db = WpDatabaseAPI()
		self.projectlog = {}

		wx.MenuBar.__init__(self)
		self.parentFrame = parentFrame
		self.Append(self.__setupFileMenu(), '&File')
		self.Append(self.__setupEditMenu(), '&Edit')
		self.Append(self.__setupViewMenu(), '&View')
		self.Append(self.__setupHelpMenu(), '&Help')

	##--------------------------------------------------------------------------
	## Menu structures
	##--------------------------------------------------------------------------

	def __setupFileMenu(self):
		fileMenu = wx.Menu()

		openProject		= wx.MenuItem(fileMenu, CONST_MENU_PROJECT_OPEN, '&Open Project', 'Open project')
		newProject		= wx.MenuItem(fileMenu, CONST_MENU_PROJECT_NEW, '&New Project', 'Create new project')
		saveFileAs		= wx.MenuItem(fileMenu, CONST_MENU_FILE_SAVE_AS, '&Save File As', 'Save current file as...')
		openFile		= wx.MenuItem(fileMenu, CONST_MENU_FILE_OPEN, '&Open File', 'Open file')
		saveFile		= wx.MenuItem(fileMenu, CONST_MENU_FILE_SAVE, '&Save File', 'Save current file')
		newFile			= wx.MenuItem(fileMenu, CONST_MENU_FILE_NEW, '&New File', 'Create empty document')
		exit			= wx.MenuItem(fileMenu, CONST_MENU_EXIT, '&Exit', 'Exit')

		self.recentProjects = wx.Menu()
		#self.recentProjects	= wx.MenuItem(fileMenu, CONST_MENU_PROJECT_RECENT, '&Recent Projects', 'Recent projects' )

		fileMenu.AppendItem(newProject)
		fileMenu.AppendItem(openProject)
		fileMenu.AppendMenu(CONST_MENU_PROJECT_RECENT, '&Recent Projects', self.recentProjects)
		fileMenu.AppendSeparator()
		fileMenu.AppendItem(newFile)
		fileMenu.AppendItem(openFile)
		fileMenu.AppendItem(saveFile)
		fileMenu.AppendItem(saveFileAs)
		fileMenu.AppendSeparator()
		fileMenu.AppendItem(exit)

		self.parentFrame.Bind(wx.EVT_MENU, self.__onExit, id=CONST_MENU_EXIT)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onNewProject, id=CONST_MENU_PROJECT_NEW)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onOpenProject, id=CONST_MENU_PROJECT_OPEN)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onOpenFile, id=CONST_MENU_FILE_OPEN)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onNewFile, id=CONST_MENU_FILE_NEW)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onSaveFile, id=CONST_MENU_FILE_SAVE)

		self.parentFrame.Bind(wx.EVT_MENU, self.__onOpenFile, id=CONST_WIDGET_BUTTON_OPEN)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onNewFile, id=CONST_WIDGET_BUTTON_NEW)
		self.parentFrame.Bind(wx.EVT_MENU, self.__onSaveFile, id=CONST_WIDGET_BUTTON_SAVE)

		pub.sendMessage( 'mainmenu.rebuildrecentprojects', True )

		return fileMenu

	def __setupEditMenu(self):
		"""
		Setup the edit menu
		"""
		editMenu = wx.Menu()
		preferences = wx.MenuItem(editMenu, CONST_MENU_PREFERENCES, '&Preferences', 'Edit application preferences')
		self.parentFrame.Bind(wx.EVT_MENU, self.__onPreferences, id=CONST_MENU_PREFERENCES)
		editMenu.AppendSeparator()
		editMenu.AppendItem(preferences)

		return editMenu

	def __setupViewMenu(self):
		"""
		Setup the view menu
		"""
		viewMenu = wx.Menu()
		return viewMenu

	def __setupHelpMenu(self):
		"""
		Setup the help menu
		"""
		helpMenu = wx.Menu()

		seekHelp = wx.MenuItem(helpMenu, wx.ID_ANY, '&Help', 'Seek help')
		requestFeature = wx.MenuItem(helpMenu, wx.ID_ANY, 'Request feature', 'Request feature')
		reportBug = wx.MenuItem(helpMenu, wx.ID_ANY, 'Report bug', 'Submit bug')
		about = wx.MenuItem(helpMenu, CONST_MENU_ABOUT, '&About', 'About')

		helpMenu.AppendItem(seekHelp)
		helpMenu.AppendSeparator()
		helpMenu.AppendItem(requestFeature)
		helpMenu.AppendItem(reportBug)
		helpMenu.AppendSeparator()
		helpMenu.AppendItem(about)

		self.parentFrame.Bind(wx.EVT_MENU, self.__onAbout, id=CONST_MENU_ABOUT)

		return helpMenu

	##--------------------------------------------------------------------------
	## Bind functions
	##--------------------------------------------------------------------------


	##--------------------------------------------------------------------------
	## Display about dialog
	##--------------------------------------------------------------------------
	def __onAbout(self, event):
		information = wx.AboutDialogInfo()

		information.SetName('Open Definition :: Warpig Code Environment')
		information.SetVersion('0.02 - Alpha Public')
		information.SetWebSite('http://www.opendefinition.com')
		information.SetCopyright('Open Definition(C)2009')
		information.AddDeveloper('Roger C.B. Johnsen')
		information.SetDescription('A simple but yet powerfull code evironment written in Python.')

		wx.AboutBox( information )

	##--------------------------------------------------------------------------
	## Display on exit dialog
	##--------------------------------------------------------------------------
	def __onExit(self, event):
		self.parentFrame.Close()

	##--------------------------------------------------------------------------
	## Display the preference menu
	##--------------------------------------------------------------------------
	def __onPreferences(self, event):
		pub.sendMessage('mainframe.showpane', 'settings')
		# self._mgr.GetPane("tree_content").Show(event.GetId() == ID_TreeContent)
		# preferences = WpPreferences()
	# preferences.ShowModal()

	##--------------------------------------------------------------------------
	## Display new project dialog window
	##--------------------------------------------------------------------------
	def __onNewProject(self, event):
		window = WpNewProject(self)
		window.Center()
		window.ShowModal()
		window.Destroy()

	##--------------------------------------------------------------------------
	## Disply open project dialog
	##--------------------------------------------------------------------------
	def __onOpenProject(self, event):
		window = WpOpenProject()
		window.ShowModal()

	##--------------------------------------------------------------------------
	## Add a new page to notebook
	##--------------------------------------------------------------------------
	def __onNewFile(self, event):
		data = {
				'file': None,
				'prjid': None
				}

		pub.sendMessage('notebook.addpage', data)

	##--------------------------------------------------------------------------
	## Disply open file dialog
	##--------------------------------------------------------------------------
	def __onOpenFile(self, event):
		self.__OpenPage()

	##--------------------------------------------------------------------------
	## Save file
	##--------------------------------------------------------------------------
	def __onSaveFile(self, event):
		focus = self.FindFocus()

		if( type( focus ).__name__ == 'WpTextEditor' ):
			focus.SaveFile()

	def openFileSubscriber(self, message):
		self.__OpenPage()

	def rebuildRecentProjects(self, message ):	
		list = self.db.GetProjectsLog()

		for entry in list:
			id = entry[0]
			title = entry[1]

			self.projectlog[title] = id

			entry = wx.MenuItem(self.recentProjects, wx.ID_ANY, title, title)
			self.recentProjects.AppendItem( entry )

			self.parentFrame.Bind(wx.EVT_MENU, self.__onOpenRecentProject, id=entry.GetId())

	def __onOpenRecentProject( self, event ):
		node = self.recentProjects.FindItemById( event.GetId() )
		projectid = self.projectlog[ node.GetItemLabel() ];
		
		project = self.db.GetProject(projectid)
		
		# Open tab
		pub.sendMessage('notebook.opensavedtabs', projectid)

		# Populate the tree
		pub.sendMessage('projecttree.populate', project)

		# Resave open status in order to get the correct date in the database
		self.db.AddRecentProjectLogEntry( projectid )
		
	def __OpenPage(self):
		dialog = wx.FileDialog ( None, style = wx.OPEN )

		if dialog.ShowModal() == wx.ID_OK:
			data = {
					'file': dialog.GetPath(),
					'prjid': None
				}

			pub.sendMessage('notebook.addpage', data)

		dialog.Destroy()


