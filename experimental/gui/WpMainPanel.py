# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpMainPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx

from gui.WpSplitLeftPanel import WpSplitLeftPanel
from gui.WpSplitRightPanel import WpSplitRightPanel

class WpMainPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self._Setup()
		
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 1, 1, 0, 0 )
	
		self.splitter = wx.SplitterWindow( self, 1333 )
		self.splitter.SetMinimumPaneSize( 20 )
		self.rightsplit = WpSplitRightPanel( self.splitter )
		self.leftsplit = WpSplitLeftPanel( self.splitter, self.rightsplit )
		self.splitter.SplitVertically( self.leftsplit, self.rightsplit )
		self.splitter.SetSashPosition( 300, True )
		self.splitter.SetBorderSize( 0 )
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self.splitter, 1, wx.EXPAND )
			]
		) 
	
		# Binding the splitter
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 ) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( wx.ID_NEW, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( wx.ID_SAVE, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.AddLabelTool( wx.ID_OPEN, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.Realize()
		
		self.Bind( wx.EVT_MENU, self._OnNew, id=wx.ID_NEW )
		
		return self.toolbar
		
	def _OnSplitterDblClk( self, event ):
		if( self.splitter.GetSashPosition() == 300 ):
			self.splitter.SetSashPosition( 20, True )
		else:
			self.splitter.SetSashPosition( 300, True )