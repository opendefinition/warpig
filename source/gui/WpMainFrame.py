# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpMainFrame
# Desc: Class for managing this application mainframe
#
#---------------------------------------------------------------------------
#
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#
#---------------------------------------------------------------------------

import wx
import wx.stc as stc

from gui.WpMainPanel import WpMainPanel

# New main menu
from gui.WpMainMenu import WpMainMenu

from system.WpFileSystem import WpFileSystem

class WpMainFrame( wx.Frame ):
	def __init__( self, *args, **kwargs ):
		wx.Frame.__init__( self, *args, **kwargs )
		self.SetTitle( 'Open Definition :: Warpig Code Environment' )
		
		self._Setup()
	
	#---------------------------------------------------------------
	# Prepare mainframe
	#---------------------------------------------------------------
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Rows, Cols - gaps are left to nil
		##
		self.flexgrid = wx.FlexGridSizer( 2, 1, 0, 0 )
		
		##
		# Main widgets
		##
		self.mainpanel = WpMainPanel( self )
		
		## Menubar
		self.SetMenuBar(WpMainMenu(self))
		
		##
		# Adding it all to the mix
		##
		self.flexgrid.AddMany( 
			[
				( self.mainpanel, 1, wx.EXPAND ),
				( self._SetupStatusBar(), 1, wx.EXPAND )
			]
		)
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		
		##
		# Display
		##
		self.Centre()
		self.Maximize()
		self.Show( True )
		
	#---------------------------------------------------------------
	# Create and setup statusbar
	# @return object statusbar
	#---------------------------------------------------------------
	def _SetupStatusBar( self ):
		self.statusbar = wx.StatusBar( self, -1 )
		
		return self.statusbar
		