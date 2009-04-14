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
		self.flexgrid = wx.FlexGridSizer( 1, 1, 0, 0 )
		
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self._SetupTreeCtrl(), 1, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )

	def _SetupTreeCtrl( self ):
		self.treectrl = WpTreeCtrl( self )
		
		self.Bind( wx.EVT_TREE_SEL_CHANGED, self._OnSelChanged, id=9999 )

		return self.treectrl	
		
	def _OnSelChanged( self, event ):
		try:
			filedata = self.treectrl.GetPyData( event.GetItem() )
			self.rightpanel.AddDefaultPage( filedata[ 'fullpath' ] )
		except:
			None
