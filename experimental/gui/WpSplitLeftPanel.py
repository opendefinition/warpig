# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpSplitLeftPanel
# Desc: Class for setting up the left splitted panel
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx

from gui.WpTreeCtrl import WpTreeCtrl

class WpSplitLeftPanel( wx.Panel ):
	def __init__( self, parent, rightpanel , *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.rightpanel = rightpanel
		
		self._Setup()

	#---------------------------------------------------------------
	# Setup this splitted panel
	#---------------------------------------------------------------
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Rows, Cols
		##
		self.flexgrid = wx.FlexGridSizer( 1, 1, 0, 0 )
		
		## 
		# Main widget
		##
		self.flexgrid.AddMany(
			[
				( self._SetupTreeCtrl(), 1, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )

	#---------------------------------------------------------------
	# Set up treecontroller (directory listing)
	# @return object treectrl
	#---------------------------------------------------------------
	def _SetupTreeCtrl( self ):
		self.treectrl = WpTreeCtrl( self )
		return self.treectrl