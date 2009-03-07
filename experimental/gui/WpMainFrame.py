# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpMainFrame
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

class WpMainFrame( wx.Frame ):
	def __init__( self, *args, **kwargs ):
		wx.Frame.__init__( self, *args, **kwargs )
		self._Setup()
		
	def _Setup( self ):
		self.sizer = wx.BoxSizer( wx.VERTICAL )
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 2, 3, 0, 0 )
		
		#-- Menubar
		self.SetMenuBar( self._SetupMenuBar() )
		
		#-- Main widgets
		self.flexgrid.Add( self._SetupToolbar() )
		self.flexgrid.Add( self._SetupTreeCtrl() )
		self.flexgrid.Add( self._SetupNotebook(), 1, wx.EXPAND )
		# self.flexgrid.Add( self._SetupStatusBar() )
		
		"""
		self.flexgrid.AddMany(
			[
				# ( self._SetupToolbar(), 0 ),
				( self._SetupTreeCtrl(), 0 ),
				( self._SetupNotebook(), 0 ),
				( self._SetupStatusBar(), 0 )
			]
		) 
		"""
		
		self.flexgrid.AddGrowableRow( 1, 0 )
		
		self.sizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.sizer )
		
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
		self.statusbar.SetStatusText( 'I h8 u' )
		
		return self.statusbar
		
	def _SetupNotebook( self ):
		self.notebook = fnb.FlatNotebook( self, wx.ID_ANY )
		self.notebook.AddPage( wx.Button ( self.notebook, 123, "Test" ), 'Test' )
		
		return self.notebook
		
	def _SetupTreeCtrl( self ):
		self.treectrl = wx.TreeCtrl( self, -1, size=(280, 600) )
		
		return self.treectrl
		
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( 101, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( 103, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.AddLabelTool( 102, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.Realize()
		
		return self.toolbar