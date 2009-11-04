# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpWarPig
# Desc: This application
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import sqlite3
import sys
import wx

from gui.WpMainFrame import WpMainFrame
from system.setup import RunSetup
from system.WpConfigLoader import WpConfigLoader

class WpWarPig( wx.App ):
	"""
	Main class for creating frame
	"""
	
	def OnInit(self):
		configloaded = False
		try:
			configuration = WpConfigLoader()
			configuration.LoadConfig()
			configloaded = True
		except sqlite3.OperationalError:
			print "Warpig System Error: missing configuration database\nplease run 'warpig.py --setup'"

		if configloaded:
			frame = WpMainFrame( None )
			frame.Show()
			self.SetTopWindow(frame)
		
		return True

def main(argv):
	"""
	Warpig booter
	"""
	if len( argv ) > 1:
		if argv[1] == '--update':
			# Update engine
			print 'Running update engine (not implemented)'
		if argv[1] == '--setup':
			RunSetup() # a setup is basically a full reset
		if argv[1] == '--reset':
			RunSetup() # a reset is basically a new installation			
	else:
		# Boot
		app = WpWarPig( 0 )
		app.MainLoop()
        
if __name__ == "__main__":
	sys.exit( main( sys.argv ) )