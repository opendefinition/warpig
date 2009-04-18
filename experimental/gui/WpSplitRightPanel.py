# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpSplitRightPanel
# Desc: Class for setting up the right splitted panel
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

from gui.WpNoteBook import WpNoteBook
from system.WpFileSystem import WpFileSystem

class WpSplitRightPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self._Setup()

	#---------------------------------------------------------------
	# Set up this splitted panel
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
				( self._SetupNotebook(), 0, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )	
	
	#---------------------------------------------------------------
	# Setup notebook page 
	# @return object notebook
	#---------------------------------------------------------------
	def _SetupNotebook( self ):
		self.notebook = WpNoteBook( self )
		self.notebook.AddDefaultPage()
		
		return self.notebook
			
	#---------------------------------------------------------------
	# Find filename of current file
	# @param string filepath
	# @return string filename
	#---------------------------------------------------------------
	def FindFileName( self, filepath ):
		length = len( filepath )
		startindex = filepath.rfind( '/' )+1
		
		return filepath[startindex:length]