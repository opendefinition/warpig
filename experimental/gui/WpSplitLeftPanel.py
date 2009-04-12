# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpSplitLeftPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx

from gui.WpTreeCtrl import WpTreeCtrl

class WpSplitLeftPanel( wx.Panel ):
	def __init__( self, parent, rightpanel , *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.rightpanel = rightpanel
		
		self._Setup()

	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 1, 2, 0, 0 )
		
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self._SetupToolbar(), 0 ),
				( self._SetupTreeCtrl(), 1, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 1 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )

	def _SetupTreeCtrl( self ):
		self.treectrl = WpTreeCtrl( self ) # wx.TreeCtrl( self, 9999, style=wx.ALL|wx.EXPAND )	
		
		self.Bind( wx.EVT_TREE_SEL_CHANGED, self._OnSelChanged, id=9999 )

		return self.treectrl
		
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( wx.ID_NEW, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( wx.ID_OPEN, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.AddLabelTool( wx.ID_SAVE, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.Realize()
		
		self.Bind( wx.EVT_MENU, self._OnToolBarNewPage, id=wx.ID_NEW )
		self.Bind( wx.EVT_MENU, self._OnToolBarSavePage, id=wx.ID_SAVE )
		self.Bind( wx.EVT_MENU, self._OnToolBarOpenPage, id=wx.ID_OPEN )
		return self.toolbar

	#==============================================================================================
	# Bindings
	#==============================================================================================
   	
   	def _OnToolBarNewPage( self, event ):
		self.rightpanel.AddDefaultPage()
		
	def _OnToolBarSavePage( self, event ):
		self.rightpanel.SaveFile()
		
	def _OnToolBarOpenPage( self, event ):
		dialog = wx.FileDialog ( None, style = wx.OPEN )
		
		if dialog.ShowModal() == wx.ID_OK:
			self.rightpanel.AddDefaultPage( dialog.GetPath() )
			
		dialog.Destroy()		
		
	def _OnSelChanged( self, event ):
		filedata = self.treectrl.GetPyData( event.GetItem() )
		
		try:
			self.rightpanel.AddDefaultPage( filedata[ 'fullpath' ] )
		except:
			None
