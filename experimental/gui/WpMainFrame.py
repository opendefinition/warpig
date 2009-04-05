# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpMainFrame
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx
import wx.stc as stc
from gui.WpMainPanel import WpMainPanel
from gui.WpNewProject import WpNewProject

from system.WpFileSystem import WpFileSystem

class WpMainFrame( wx.Frame ):
	def __init__( self, *args, **kwargs ):
		wx.Frame.__init__( self, *args, **kwargs )
		self._Setup()
		
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 2, 1, 0, 0 )
		
		#-- Menubar
		self.SetMenuBar( self._SetupMenuBar() )
		
		#-- Main widgets
		self.mainpanel = WpMainPanel( self )
		
		#-- Adding it all to the mix
		self.flexgrid.AddMany( 
			[
				( self.mainpanel, 0, wx.EXPAND ),
				( self._SetupStatusBar(), 0, wx.EXPAND )
			]
		)
		
		self.flexgrid.AddGrowableRow( 0, 0 )
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		
		#-- Display
		self.Centre()
		self.Maximize()
		self.Show( True )
		
	def _SetupMenuBar( self ):
		self.menubar = wx.MenuBar()
		
		file = wx.Menu()
		edit = wx.Menu()
		view = wx.Menu()
		plugins = wx.Menu()
		help = wx.Menu()
		
		self.menubar.Append( file, '&File' )
		self.menubar.Append( edit, '&Edit' )
		self.menubar.Append( view, '&View' )
		self.menubar.Append( plugins, '&Plugins' )
		self.menubar.Append( help, '&Help' )
		
		# File menu entries
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
		
	 	helpabout = wx.MenuItem( help, 10501, '&About', 'About WarPig'  )
		help.AppendItem( helpabout )
		
		self.Bind( wx.EVT_MENU, self._OnAbout, id=10501 )
		self.Bind( wx.EVT_MENU, self._OnExit, id=10107 )
		self.Bind( wx.EVT_MENU, self._OnNewProject, id=10101 )
		self.Bind( wx.EVT_MENU, self._OnOpenProject, id=10102 )
		
		return self.menubar
		
	def _SetupStatusBar( self ):
		self.statusbar = wx.StatusBar( self, -1 )
		
		return self.statusbar
		
	#===============================================================================================
	# Bindings
	#===============================================================================================
	
	def _OnAbout( self, event ):
		information = wx.AboutDialogInfo()
 		information.SetName( 'WarPig Code Editor' )
 		information.SetVersion( '0.01' )
  		information.SetDescription( 'WarPig is a simple but yet useful code editor written in Python.' )
  		information.SetCopyright('(C) 2009 Open Definition' )
  		information.SetWebSite( 'http://www.opendefinition.com' )
  		information.AddDeveloper( 'Roger Johnsen' )
  		
  		# wx.AboutBox( information )
  		
  	def _OnExit( self, event ):
  		self.Close()
  		
  	def _OnNewProject( self, event ):
  		window = WpNewProject( self.mainpanel.leftsplit )
		window.ShowModal()
		window.Destroy()
        
        """
  		filters = 'WarPig Project File (*.wpf)|*.wpf'
  		dialog = wx.FileDialog ( None, 'New Project', wildcard=filters, style = wx.SAVE )
  		
  		if dialog.ShowModal() == wx.ID_OK:
			path = dialog.GetPath()
			
			info = WpFileSystem.SaveProjectFile( path )
			self.mainpanel.leftsplit.PopulateTreeCtrl( info[ 'dirlist' ], info[ 'fname' ] )
			
			dialog.Destroy()		
		"""
	
	def _OnOpenProject( self, event ):
		filter = 'WarPig Project File (*.wpf)|*.wpf'
		dialog = wx.FileDialog( None, 'Open Project', wildcard=filter, style=wx.OPEN )
		
		if( dialog.ShowModal() == wx.ID_OK ):
			dialog.Destroy()
		