# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpMainFrame
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx
import wx.stc as stc
from gui.WpMainPanel import WpMainPanel

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
		
	 	helpabout = wx.MenuItem( help, 10501, '&About', 'About WarPig'  )
		help.AppendItem( helpabout )
		
		self.Bind( wx.EVT_MENU, self._OnAbout, id=10501 )
		
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
  		
  		wx.AboutBox( information )