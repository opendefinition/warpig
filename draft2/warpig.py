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

import sys
import wx


from gui.WpMainFrame import WpMainFrame

class WpWarPig( wx.App ):
	"""
	Main class for creating frame
	"""
	
	def OnInit(self):
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
	else:
		# Boot
		app = WpWarPig( 0 )
		app.MainLoop()
        
if __name__ == "__main__":
	sys.exit( main( sys.argv ) )