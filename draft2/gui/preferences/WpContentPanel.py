# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpContentPanel
# Desc: Class for handling preferences
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx

class WpContentPanel( wx.Panel ):
	def __init__( self, parent , *args, **kwargs ):
		wx.Panel.__init__( self, parent, *args, **kwargs )