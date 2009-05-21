# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpPreferences
# Desc: Class for handling preferences
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx

class WpTreePanel( wx.Panel ):
	def __init__( self, parent , *args, **kwargs ):
		wx.Panel.__init__( self, parent, *args, **kwargs )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		self.treectrl = wx.TreeCtrl( self )
		
		sizer.Add( self.treectrl, 1, wx.EXPAND )
		self.SetSizer( sizer, wx.EXPAND )