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

from system.WpFileSystem import WpFileSystem

class WpPreferences( wx.Dialog ):
	def __init__( self ):
		
		wx.Dialog.__init__( self, None, 6666, 'WarPig Preferences', size=(600, 600) )
		self.Center()