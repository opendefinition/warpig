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

from gui.preferences.WpPreferenceTree import WpPreferenceTree

class WpPreferences( wx.Dialog ):
	def __init__( self ):
		
		wx.Dialog.__init__( self, None, wx.ID_ANY, 'WarPig Preferences', size=(600, 600) )
		
		self.Setup()
		self.Center()
		
	def Setup( self ):
		##
		# Mainpanel to hold everything
		##
		sizeHeight = self.GetSize()[1]
		sizeWidth = self.GetSize()[0]

		self.mainpanel = wx.Panel( self, -1, size=( sizeHeight, sizeWidth ) )
		self.panelsizer = wx.BoxSizer( wx.VERTICAL ) 
		
		##
		# Preferencetree widget
		##
		self.preferencetree = WpPreferenceTree( self.mainpanel, -1 )
		
		##
		# Mainsizer
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Sewing it all together
		##
		##
		self.panelsizer.Add( self.preferencetree, 1, wx.EXPAND )
		self.mainsizer.Add( self.panelsizer, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer, wx.EXPAND )
		