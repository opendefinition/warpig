# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpMainPanel
# Desc: Class for managing this application mainpanel
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
import wx.py as py

from gui.WpSplitLeftPanel import WpSplitLeftPanel
from gui.WpSplitRightPanel import WpSplitRightPanel


class WpMainPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self.Setup()

	#---------------------------------------------------------------
	# Set up this panel
	#---------------------------------------------------------------
	def Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Rows, Cols
		##
		self.flexgrid = wx.FlexGridSizer( 1, 2, 0, 0 )
	
		self.splitter = wx.SplitterWindow( self, 1333, style=wx.SP_3DSASH )
		self.splitter.SetMinimumPaneSize( 1 )
		self.rightsplit = WpSplitRightPanel( self.splitter )
		self.leftsplit = WpSplitLeftPanel( self.splitter, self.rightsplit )
		self.splitter.SplitVertically( self.rightsplit, self.leftsplit )		
		self.splitter.SetSashPosition( -1, True )
		self.splitter.SetBorderSize( 0 )
		self.sashpos = None

		##
		# Binding the splitter
		##
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 )
		
		##
		# Main sizer for this panel
		## 
		mainsizer = wx.BoxSizer( wx.HORIZONTAL) 
		
		mainsizer.Add( self.splitter, 1, wx.EXPAND )
		self.SetSizer( mainsizer )		
	
	#---------------------------------------------------------------
	# Handle 'on doubleclick' on sash
	#---------------------------------------------------------------
	def _OnSplitterDblClk( self, event ):
		self.ResizeSash()
	
	#---------------------------------------------------------------
	# Handling resizing of sash
	#---------------------------------------------------------------
	def ResizeSash( self ):
		windowsize = self.splitter.GetSize()[0]
		sashpos = self.splitter.GetSashPosition()
			
		if self.sashpos == None or self.sashpos < sashpos:
			self.splitter.SetSashPosition( (windowsize-200), True )
		else:
			self.splitter.SetSashPosition( -1, True )
			
		self.sashpos = sashpos
	
	#---------------------------------------------------------------
	# Bindings
	#---------------------------------------------------------------
   	
	#---------------------------------------------------------------
	# On new page 
	#---------------------------------------------------------------
   	def _OnToolBarNewPage( self, event ):
		self.rightsplit.notebook.AddDefaultPage()
	
	#---------------------------------------------------------------
	# On save page from toolbar
	#---------------------------------------------------------------	
	def _OnToolBarSavePage( self, event ):
		focus = self.FindFocus()
		
		if( type( focus ).__name__ == 'WpTextEditor' ):
			focus.SaveFile()
	
	#---------------------------------------------------------------
	# On open page event
	#---------------------------------------------------------------
	def _OnToolBarOpenPage( self, event ):
		self.OpenPage()
	
	#---------------------------------------------------------------
	# Open Page 
	#---------------------------------------------------------------
	def OpenPage( self ):
		dialog = wx.FileDialog ( None, style = wx.OPEN )
		
		if dialog.ShowModal() == wx.ID_OK:
			self.rightsplit.notebook.AddDefaultPage( dialog.GetPath() )
			
		dialog.Destroy()
	