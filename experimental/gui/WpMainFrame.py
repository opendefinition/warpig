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
		
		self.flexgrid.AddGrowableRow( 1, 1 )
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
		
		return self.menubar
		
	def _SetupStatusBar( self ):
		self.statusbar = wx.StatusBar( self, -1 )
		self.statusbar.SetStatusText( '123' )
		
		return self.statusbar