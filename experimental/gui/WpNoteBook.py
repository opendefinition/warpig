# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpNoteBook
# Desc: Class for setting up main notebook interface
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import wx
import wx.lib.flatnotebook as fnb

from gui.WpTextEditor import WpTextEditor 

class WpNoteBook( fnb.FlatNotebook ):
	def __init__( self, parent ):
		self.parent = parent
		fnb.FlatNotebook.__init__( self, parent, wx.ID_ANY, style=wx.EXPAND )

	#---------------------------------------------------------------
	# Add text editor to page
	# @param string filepath <conditional>
	# @return object texteditor
	#---------------------------------------------------------------
	def _AddTextEditor( self, filepath=None):
		texteditor = WpTextEditor( self )
		# Adding content
		if filepath is not None:
			texteditor.SetFilePath( filepath )
			texteditor.SetDefaultLexer()
		
		texteditor.SetSavePoint()
		return texteditor
	
	#---------------------------------------------------------------
	# Add default page
	# @param string filepath <conditional>
	#---------------------------------------------------------------
	def AddDefaultPage( self, filepath=None ):
		title = '< empty >'
		
		if filepath is None:
			filepath = None
		else:
			split = os.path.split( filepath )
			filepath = filepath
			title = split[ 1 ]
		
		##
		# Keeps notebook from flickering when adding pages. See Thaw later in this function.
		##
		self.Freeze()
		self.AddPage( self._AddTextEditor( filepath ), title, True )
		
		##
		# Thawing
		##
		self.Thaw()
