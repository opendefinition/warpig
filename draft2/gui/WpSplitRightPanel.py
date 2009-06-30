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

from wx.lib.agw import buttonpanel as bp

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
		# Button panel
		##
		self.alignment = bp.BP_ALIGN_LEFT
		self.style = bp.BP_USE_GRADIENT
		self.buttonpanel = bp.ButtonPanel(self, -1, "", style=self.style, alignment=self.alignment)
	
		btn1 = bp.ButtonInfo( self.buttonpanel, 
								wx.ID_NEW, 
								wx.Bitmap("./gui/icons/document-new.png", wx.BITMAP_TYPE_PNG)
								)
		self.buttonpanel.AddButton(btn1)
		 
		btn2 = bp.ButtonInfo( self.buttonpanel, 
								wx.ID_OPEN, 
								wx.Bitmap("./gui/icons/folder.png", wx.BITMAP_TYPE_PNG)
								)
		self.buttonpanel.AddButton(btn2)
		
		btn3 = bp.ButtonInfo( self.buttonpanel, 
								wx.ID_SAVE, 
								wx.Bitmap("./gui/icons/media-floppy.png", wx.BITMAP_TYPE_PNG)
								)
		self.buttonpanel.AddButton(btn3)
		
		self.buttonpanel.DoLayout()
		
		self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarNewPage, id=btn1.GetId() )
		self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarOpenPage, id=btn2.GetId() )
		self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarSavePage, id=btn3.GetId() )
		
		self.somesizer = wx.BoxSizer( wx.VERTICAL )
		self.somesizer.Add( self.buttonpanel, 0, wx.EXPAND )
		self.somesizer.Add( self._SetupNotebook(), 1, wx.EXPAND )
		
		##
		# Main widget
		##
		self.flexgrid.AddMany(
			[
				( self.somesizer, 0, wx.EXPAND )
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