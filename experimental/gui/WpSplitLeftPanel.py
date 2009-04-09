# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpSplitLeftPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx

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
		self.treectrl = wx.TreeCtrl( self, 9999, style=wx.ALL|wx.EXPAND )	
		
		self.Bind( wx.EVT_TREE_SEL_CHANGED, self._OnSelChanged, id=9999 )

		return self.treectrl
		
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

	#==============================================================================================
	# Bindings
	#==============================================================================================
   	
   	def _OnToolBarNewPage( self, event ):
		self.rightpanel.AddDefaultPage()
		
	def _OnToolBarSavePage( self, event ):
		self.rightpanel.SaveFile()
		
	def _OnToolBarOpenPage( self, event ):
		dialog = wx.FileDialog ( None, style = wx.OPEN )
		
		if dialog.ShowModal() == wx.ID_OK:
			self.rightpanel.AddDefaultPage( dialog.GetPath() )
			
		dialog.Destroy()
		
	def PopulateTreeCtrl( self, structure, projectname):
		# Destroying all content is content is present
		if( self.treectrl.IsEmpty() == False ):
			self.treectrl.DeleteAllItems()
		
		ArtIDs = [ 'wx.ART_FOLDER', 'wx.ART_FOLDER_OPEN', 'wx.ART_NORMAL_FILE' ]
		
		il = wx.ImageList( 16, 16 )
		for items in ArtIDs:
			pic = wx.ArtProvider_GetBitmap(eval(items), wx.ART_TOOLBAR, ( 16, 16 ) )
			il.Add( pic )
		
		self.treectrl.AssignImageList( il )
	
		prjname = projectname[0:-4]
		treeroot = self.treectrl.AddRoot( str( prjname ), 1, 0, wx.TreeItemData( projectname ) )
		self.treectrl.SetItemHasChildren( treeroot, True )
	
		for item in structure[ 'files' ]:
			# split = WpFileSystem.SplitFilepath( item )
			data = {
				'path': structure[ 'path' ],
				'fname': item,
				'fullpath': structure[ 'path' ]+item
			}
			self.treectrl.AppendItem( treeroot, item, 2, 2, wx.TreeItemData( data ) )
			
		self.treectrl.Expand( treeroot )
		
		
		
	def _OnSelChanged( self, event ):
		filedata = self.treectrl.GetPyData( event.GetItem() )
		 
		if filedata[ 'fname' ] not in self.rightpanel.files:
			self.rightpanel.AddDefaultPage( filedata[ 'fullpath' ] )
