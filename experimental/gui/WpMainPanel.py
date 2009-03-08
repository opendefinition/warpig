import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

class WpSplitLeftPanel( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
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
		
		self.Bind( wx.EVT_MENU, self._OnNew, id=wx.ID_NEW )
		
		return self.toolbar

	#==============================================================================================
	# Bindings
	#==============================================================================================
   	
   	def _OnNew( self, event ):
		self.notebook.AddPage( self._AddTextEditor(), '<empty>' )

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
		self.notebook.AddPage( self._AddTextEditor(), '<empty>' )
		
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
			texteditor.LoadFile( filePath )
			
		return texteditor


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
		self.leftsplit = WpSplitLeftPanel( self.splitter )
		self.rightsplit = WpSplitRightPanel( self.splitter )
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