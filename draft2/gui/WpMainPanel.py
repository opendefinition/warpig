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
import wx.lib.colourselect as csel
import os
import wx
from wx.lib.agw import labelbook as LB
from wx.lib.agw.fmresources import *

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
		# Main widget
		##
		"""
		self.flexgrid.AddMany(
			[
				( self._SetupToolbar(), 0 ),
				( self.splitter, 1, wx.EXPAND )
			]
		) 
		"""
		"""
		##
		# Binding the splitter
		##
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 ) 
	
		self.flexgrid.AddGrowableCol( 1 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		"""
		##
		# Binding the splitter
		##
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 )
		
		## Main sizer for this panel
		mainsizer = wx.BoxSizer( wx.HORIZONTAL)
		
		## Adding images to the book
		imagelist = wx.ImageList( 32, 32 )
		pageIcons = [ 
						"internet-web-browser.png",
						"accessories-text-editor.png", 
						"utilities-terminal.png"
					]
		
		for img in pageIcons:
			image = os.path.join( "./gui/icons/modebar", img )
			bmp = wx.Bitmap( image, wx.BITMAP_TYPE_PNG )
			imagelist.Add( bmp )
		
		## Labelbook that holds the main navigation feature of this application
		labelbook = LB.LabelBook( self, -1 )

		## Styling
		labelbook.AssignImageList( imagelist )
		
		labelbook.SetColour( INB_TAB_AREA_BACKGROUND_COLOR, "#505151" )
		labelbook.SetColour( INB_ACTIVE_TAB_COLOR, "#eeeeee" )
		labelbook.SetColour( INB_TABS_BORDER_COLOR, "#e0e0e0" )
		labelbook.SetColour( INB_TEXT_COLOR, "#c0c0c0" )
		labelbook.SetColour( INB_ACTIVE_TEXT_COLOR, "#505151" )
		labelbook.SetColour( INB_HILITE_TAB_COLOR, "#99c00" )

		labelbook.AddPage( wx.Button( labelbook, wx.ID_ANY, "Test1" ) , "Info", True, 0 )
		labelbook.AddPage( self.splitter, "Editor", True, 1 )
		labelbook.AddPage( wx.Button( labelbook, wx.ID_ANY, "Test3" ) , "Terminal", True, 2 )
		labelbook.SetSelection(0)  
		
		mainsizer.Add( labelbook, 1, wx.EXPAND )
		self.SetSizer( mainsizer )		
		
	"""
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Rows, Cols
		##
		self.flexgrid = wx.FlexGridSizer( 1, 2, 0, 0 )
	
		self.splitter = wx.SplitterWindow( self, 1333, style=wx.SP_NO_XP_THEME | wx.SP_3DSASH )
		self.splitter.SetMinimumPaneSize( 1 )
		self.rightsplit = WpSplitRightPanel( self.splitter )
		self.leftsplit = WpSplitLeftPanel( self.splitter, self.rightsplit )
		self.splitter.SplitVertically( self.leftsplit, self.rightsplit )
		self.splitter.SetSashPosition( 1, True )
		self.splitter.SetBorderSize( 0 )

		##
		# Main widget
		##
		self.flexgrid.AddMany(
			[
				( self._SetupToolbar(), 0 ),
				( self.splitter, 1, wx.EXPAND )
			]
		) 
	
		##
		# Binding the splitter
		##
		self.Bind( wx.EVT_SPLITTER_DCLICK, self._OnSplitterDblClk, id=1333 ) 
	
		self.flexgrid.AddGrowableCol( 1 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
	"""
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
	