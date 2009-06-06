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

from wx.html import HtmlWindow

from gui.WpModeBar import WpModeBar
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
	
		self.splitter = wx.SplitterWindow( self, 1333, style=wx.SP_NO_XP_THEME | wx.SP_3DSASH )
		self.splitter.SetMinimumPaneSize( 1 )
		self.rightsplit = WpSplitRightPanel( self.splitter )
		self.leftsplit = WpSplitLeftPanel( self.splitter, self.rightsplit )
		# self.splitter.SplitVertically( self.leftsplit, self.rightsplit )
		self.splitter.SplitVertically( self.rightsplit, self.leftsplit )
		self.splitter.SetSashPosition( -1, True )
		self.splitter.SetBorderSize( 0 )

		##
		# Binding the splitter
		##
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 )
		
		##
		# Main sizer for this panel
		## 
		mainsizer = wx.BoxSizer( wx.HORIZONTAL) 
		
		##
		# Mode Bar
		##
		modebar = WpModeBar( self )
	
		# Adding icons
		modebar.SetIconPath( "./gui/icons/modebar" )
		modebar.AddIcon( "internet-web-browser.png" )
		modebar.AddIcon( "accessories-text-editor.png" ) 
		modebar.AddIcon( "utilities-terminal.png" )
		
		# Channel browser component
		html =  HtmlWindow( self, wx.ID_ANY )
		html.LoadFile( "./infochannel.html" )
		
		# Add modes to modebar
		modebar.AddModePage( html, "Info", True, 0 )
		modebar.AddModePage( self.splitter, "Editor", True, 1 )
		modebar.AddModePage( py.crust.Crust( self, -1 ) , "Terminal", True, 2 )
    
    	# Run/Render/Populate modebar
		modebar.Run()
		
		mainsizer.Add( modebar, 1, wx.EXPAND )
		
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
		if( self.splitter.GetSashPosition() == 1 ):
			self.splitter.SetSashPosition( -200, True )
		else:
			self.splitter.SetSashPosition( -1, True )
	
	#---------------------------------------------------------------
	# Set up toolbar
	#---------------------------------------------------------------
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( wx.ID_NEW, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( wx.ID_OPEN, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.AddLabelTool( wx.ID_SAVE, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.Realize()
		
		self.Bind( wx.EVT_MENU, self._OnToolBarNewPage, id=wx.ID_NEW )
		self.Bind( wx.EVT_MENU, self._OnToolBarSavePage, id=wx.ID_SAVE )
		self.Bind( wx.EVT_MENU, self._OnToolBarOpenPage, id=wx.ID_OPEN )
		return self.toolbar
		
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
	