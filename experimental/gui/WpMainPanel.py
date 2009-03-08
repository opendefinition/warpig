# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpMainFrame
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

#==================================================================================================
# WpSplitLeftPanel
#==================================================================================================

class WpSplitLeftPanel( wx.Panel ):
	def __init__( self, parent, rightpanel , *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.rightpanel = rightpanel
		
		self._Setup()

	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 1, 2, 0, 0 )
		
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self._SetupToolbar(), 0 ),
				( self._SetupTreeCtrl(), 1, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 1 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )

	def _SetupTreeCtrl( self ):
		self.treectrl = wx.TreeCtrl( self, -1, style=wx.ALL|wx.EXPAND )
		
		return self.treectrl
		
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( wx.ID_NEW, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( wx.ID_SAVE, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.AddLabelTool( wx.ID_OPEN, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.Realize()
		
		self.Bind( wx.EVT_MENU, self._OnToolBarNewPage, id=wx.ID_NEW )
		self.Bind( wx.EVT_MENU, self._OnToolBarSavePage, id=wx.ID_SAVE )
		self.Bind( wx.EVT_MENU, self._OnToolBarOpenPage, id=wx.ID_OPEN )
		return self.toolbar

	#==============================================================================================
	# Bindings
	#==============================================================================================
   	
   	def _OnToolBarNewPage( self, event ):
		self.rightpanel.AddDefaultPage()
		
	def _OnToolBarSavePage( self, event ):
		print "Hello"
		
	def _OnToolBarOpenPage( self, event ):
		dialog = wx.FileDialog ( None, style = wx.OPEN )
		
		if dialog.ShowModal() == wx.ID_OK:
			self.rightpanel.AddDefaultPage( dialog.GetPath() )
			
		dialog.Destroy()
		
		

#==================================================================================================
# WpSplitRightPanel
#==================================================================================================

class WpSplitRightPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self._Setup()

	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 1, 1, 0, 0 )
		
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self._SetupNotebook(), 0, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )	
	
	def _SetupNotebook( self ):
		self.notebook = fnb.FlatNotebook( self, wx.ID_ANY, style=wx.EXPAND )
		self.AddDefaultPage()
		
		return self.notebook
		
	def _AddTextEditor( self, filepath=None):
		texteditor = stc.StyledTextCtrl ( self.notebook, 1337, style=wx.TE_MULTILINE )

		# Line numbering!
		texteditor.SetMarginType( 0, stc.STC_MARGIN_NUMBER )

		# Margin for line numbering
		texteditor.SetMarginWidth( 0, 35 )
		
		font = wx.Font( 12, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.BOLD )
		texteditor.StyleSetFont( 0, font )
		
		# Adding content
		if filepath is not None:
			texteditor.LoadFile( filepath )
			
		return texteditor
	
	#===============================================================================================
	# Helper functions
	#===============================================================================================
	def AddDefaultPage( self, filepath=None ):
		title = '< empty >'
		
		if filepath is None:
			filepath = None
		else:
			length = len( filepath )
			startindex = filepath.rfind( '/' )+1
			title = filepath[startindex:length]
            
		self.notebook.AddPage( self._AddTextEditor( filepath ), title )


#==================================================================================================
# WpMainPanel
#==================================================================================================

class WpMainPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		self._Setup()
		
	def _Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		# Rows, Cols
		self.flexgrid = wx.FlexGridSizer( 1, 1, 0, 0 )
	
		self.splitter = wx.SplitterWindow( self, -1 )
		self.rightsplit = WpSplitRightPanel( self.splitter )
		self.leftsplit = WpSplitLeftPanel( self.splitter, self.rightsplit )
		self.splitter.SplitVertically( self.leftsplit, self.rightsplit )
		self.splitter.SetSashPosition( 300, True )
		self.splitter.SetBorderSize( 0 )
		#-- Main widget
		self.flexgrid.AddMany(
			[
				( self.splitter, 1, wx.EXPAND )
			]
		) 
	
		self.flexgrid.AddGrowableCol( 0 )
		self.flexgrid.AddGrowableRow( 0 )
		
		self.mainsizer.Add( self.flexgrid, 1, wx.EXPAND )
		self.SetSizer( self.mainsizer )
		
	def _SetupToolbar( self ):
		self.toolbar = wx.ToolBar( self, -1, style=wx.TB_VERTICAL )
		self.toolbar.AddLabelTool( wx.ID_NEW, '', wx.Bitmap( './gui/icons/document-new.png' ) )
		self.toolbar.AddLabelTool( wx.ID_SAVE, '', wx.Bitmap( './gui/icons/media-floppy.png' ) )
		self.toolbar.AddLabelTool( wx.ID_OPEN, '', wx.Bitmap( './gui/icons/folder.png' ) )
		self.toolbar.Realize()
		
		self.Bind( wx.EVT_MENU, self._OnNew, id=wx.ID_NEW )
		
		return self.toolbar