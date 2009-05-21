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

from gui.preferences.WpTreePanel import WpTreePanel
from gui.preferences.WpContentPanel import WpContentPanel

class WpPreferences( wx.Dialog ):
	def __init__( self ):
		
		wx.Dialog.__init__( self, None, wx.ID_ANY, 'WarPig Preferences', size=(600, 600) )
		
		self.splitter = wx.SplitterWindow( self, wx.ID_ANY )
						self.treepanel = WpTreePanel( self.splitter )
		self.contentpanel = WpContentPanel( self.splitter )
		
		self.splitter.SetSashPosition( 200, True )
		self.splitter.SplitVertically( self.treepanel, self.contentpanel )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		sizer.Add( self.splitter, 1, wx.EXPAND )
		self.SetSizer( sizer, wx.EXPAND )
	
		self.Center()