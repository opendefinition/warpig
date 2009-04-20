# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpMainFrame
# Desc: Class for managing this application mainframe
#
#---------------------------------------------------------------------------
#
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#
#---------------------------------------------------------------------------

import wx
import wx.stc as stc
from gui.WpMainPanel import WpMainPanel
from gui.WpNewProject import WpNewProject
from gui.WpPreferences import WpPreferences

from system.WpFileSystem import WpFileSystem

class WpMainFrame( wx.Frame ):
	def __init__( self, *args, **kwargs ):
		wx.Frame.__init__( self, *args, **kwargs )
		self.SetTitle( 'WarPig code Environment' )
		
		self._Setup()
	
	#---------------------------------------------------------------
	# Prepare mainframe
	#---------------------------------------------------------------
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Rows, Cols - gaps are left to nil
		##
		self.flexgrid = wx.FlexGridSizer( 2, 1, 0, 0 )
		
		##
		# Main widgets
		##
		self.mainpanel = WpMainPanel( self )
		
		##
		# Menubar
		##
		self.SetMenuBar( self._SetupMenuBar() )
		
		##
		# Adding it all to the mix
		##
		self.flexgrid.AddMany( 
			[
				( self.mainpanel, 1, wx.EXPAND ),
				( self._SetupStatusBar(), 1, wx.EXPAND )
			]
		)
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		
		##
		# Display
		##
		self.Centre()
		self.Maximize()
		self.Show( True )
		
		
	#---------------------------------------------------------------
	# Create and setup menubar
	# @return object menubar
	#---------------------------------------------------------------
	def _SetupMenuBar( self ):
		self.menubar = wx.MenuBar()
		
		file = wx.Menu()
		edit = wx.Menu()
		view = wx.Menu()
		piglets = wx.Menu()
		help = wx.Menu()
		
		self.menubar.Append( file, '&File' )
		self.menubar.Append( edit, '&Edit' )
		self.menubar.Append( view, '&View' )
		self.menubar.Append( piglets, '&Piglets' )
		self.menubar.Append( help, '&Help' )
		
		##
		# File menu entries
		##
		newproject = wx.MenuItem( file, 10101, '&New Project', 'Create new project' )
		openproject = wx.MenuItem( file, 10102, '&Open Project', 'Open project' )
		openfile = wx.MenuItem( file, 10103, '&Open File', 'Open file' )
		newfile = wx.MenuItem( file, 10104, '&New File', 'Create empty document' )
		savefile = wx.MenuItem( file, 10105, '&Save File', 'Save current file' )
		savefileas = wx.MenuItem( file, 10106, '&Save File As', 'Save current file as...' )
		exit = wx.MenuItem( file, 10107, '&Exit', 'Exit' )
	
		file.AppendItem( newproject )
		file.AppendItem( openproject )
		file.AppendSeparator()
		file.AppendItem( newfile )
		file.AppendItem( openfile )
		file.AppendItem( savefile )
		file.AppendItem( savefileas )
		file.AppendSeparator()
		file.AppendItem( exit )
		
		##
		# Edit menu entries
		##
		preferences = wx.MenuItem( edit, 20210, '&Preferences', 'Edit application preferences' )
		
		edit.AppendSeparator()
		edit.AppendItem( preferences )
		
		##
		# Help menu entries
		##
		
		helphelp = wx.MenuItem( help, 10501, '&Help', 'Get help' )
		helprequestfeature = wx.MenuItem( help, 10502, 'Request feature', 'Request feature' )
		helpreportbug = wx.MenuItem( help, 10503, 'Report bug', 'Submit bug' )
	 	helpabout = wx.MenuItem( help, 10510, '&About', 'About WarPig'  )
		
		help.AppendItem( helphelp )
		help.AppendSeparator()
		help.AppendItem( helprequestfeature )
		help.AppendItem( helpreportbug ) 
		help.AppendSeparator()
		help.AppendItem( helpabout )
		
		self.Bind( wx.EVT_MENU, self._OnAbout, id=10510 )
		self.Bind( wx.EVT_MENU, self._OnExit, id=10107 )
		self.Bind( wx.EVT_MENU, self._OnNewProject, id=10101 )
		self.Bind( wx.EVT_MENU, self._OnOpenProject, id=10102 )
		self.Bind( wx.EVT_MENU, self.mainpanel._OnToolBarOpenPage, id=10103 )
		self.Bind( wx.EVT_MENU, self.mainpanel._OnToolBarNewPage, id=10104 )
		self.Bind( wx.EVT_MENU, self.mainpanel._OnToolBarSavePage, id=10105 )
		self.Bind( wx.EVT_MENU, self._OnPreferences, id=20210 )
		
		return self.menubar
		
	#---------------------------------------------------------------
	# Create and setup statusbar
	# @return object statusbar
	#---------------------------------------------------------------
	def _SetupStatusBar( self ):
		self.statusbar = wx.StatusBar( self, -1 )
		
		return self.statusbar
		
	#---------------------------------------------------------------
	# Bindings Section
	#---------------------------------------------------------------
	
	#---------------------------------------------------------------
	# Populates an about dialog and dispays it
	#---------------------------------------------------------------
	def _OnAbout( self, event ):
		information = wx.AboutDialogInfo()
 		information.SetName( 'WarPig Code Environment' )
 		information.SetVersion( '0.01 - Alpha Public' )
  		information.SetDescription( 'A simple but yet powerfull code evironment written in Python.' )
  		information.SetCopyright('Open Definition(C)2009' )
  		information.SetWebSite( 'http://www.opendefinition.com' )
  		information.AddDeveloper( 'Roger C.B. Johnsen' )
  		
  		wx.AboutBox( information )
  	
	#---------------------------------------------------------------
	# Handle 'on exit' event
	#---------------------------------------------------------------
  	def _OnExit( self, event ):
		dialog = wx.MessageDialog( None, 
									'Are you sure to want to quit?', 
									'Question',
									wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION 
								)
		
		status = dialog.ShowModal()
	
		if( status == wx.ID_YES ):
			dialog.Destroy()
			self.Close()
		else:
			dialog.Destroy()
  		
	#---------------------------------------------------------------
	# Handle 'on new project' event
	#---------------------------------------------------------------
  	def _OnNewProject( self, event ):
  		window = WpNewProject( self.mainpanel.leftsplit )
		window.ShowModal()
		window.Destroy()
	
	#---------------------------------------------------------------
	# Handle 'on open project' event
	#---------------------------------------------------------------
	def _OnOpenProject( self, event ):
		filter = 'WarPig Project File (*.wpf)|*.wpf'
		dialog = wx.FileDialog( None, 'Open Project', wildcard=filter, style=wx.OPEN )
		
		if( dialog.ShowModal() == wx.ID_OK ):
			path = dialog.GetPath()
			structure = WpFileSystem.LoadProjectFile( path )
			self.mainpanel.leftsplit.treectrl.PopulateTree(  structure[ 'dirlist' ], structure[ 'fname' ] )
	
		dialog.Destroy()
		
	def _OnPreferences( self, event ):
		preferences = WpPreferences()
		preferences.ShowModal()
		