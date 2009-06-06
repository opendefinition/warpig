# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpModeBar
# Desc: Generic implementation class of Labelbook with handy helperfunctions
#
#---------------------------------------------------------------------------
#
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#
#---------------------------------------------------------------------------

import os
import wx 
import wx.lib.colourselect as csel

from wx.lib.agw import labelbook as LB
from wx.lib.agw.fmresources import *

class WpModeBar( wx.lib.agw.labelbook.LabelBook ):
	_iconpath = ""
	_icons = []

	def __init__( self, parent, *args, **kwargs ):
		wx.lib.agw.labelbook.LabelBook.__init__(self, parent, *args, **kwargs)
	
	#---------------------------------------------------------------
	# Run modebar assembler
	#---------------------------------------------------------------
	def Run( self ):
		## Adding images to the book
		self._SetupIcons()
		
		## Styling
		self.AssignImageList( self._imagelist )
		
		self.SetColour( INB_TAB_AREA_BACKGROUND_COLOR, "#505151" )
		self.SetColour( INB_ACTIVE_TAB_COLOR, "#eeeeee" )
		self.SetColour( INB_TABS_BORDER_COLOR, "#e0e0e0" )
		self.SetColour( INB_TEXT_COLOR, "#c0c0c0" )
		self.SetColour( INB_ACTIVE_TEXT_COLOR, "#505151" )
		self.SetColour( INB_HILITE_TAB_COLOR, "#99c00" )
		self.SetSelection(0)  
	
	#---------------------------------------------------------------
	# Populate icon list (helperfunction)
	#---------------------------------------------------------------
	def _SetupIcons( self ):
		self._imagelist = wx.ImageList( 32, 32 )
		
		for img in self._icons:
			image = os.path.join( self._iconpath, img )
			png = wx.Bitmap( image, wx.BITMAP_TYPE_PNG )
			self._imagelist.Add( png )
	
	#---------------------------------------------------------------
	# Add new modepage to modebar
	# @param object module
	# @param string text 
	# @param boolean selected
	# @param integer image
	#---------------------------------------------------------------
	def AddModePage( self, module, text, selected=False, image=0 ):
		self.AddPage( module, text, selected, image )
	
	#---------------------------------------------------------------
	# Add icon to icon list
	# @param string iconfile
	#---------------------------------------------------------------
	def AddIcon( self, iconfile ):
		self._icons.append( iconfile )
		
	#---------------------------------------------------------------
	# Set path to where the icons is situated
	# @param string iconpath 
	#---------------------------------------------------------------
	def SetIconPath( self, iconpath ):
		self._iconpath = iconpath