# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpSplitLeftPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import wx

class WpTreeCtrl( wx.TreeCtrl ):
	def __init__( self, parent ):
		wx.TreeCtrl.__init__( self, parent, 9999, style=wx.ALL|wx.EXPAND )
		
	def PopulateTree( self, structure, projectname):
		# Destroying all content is content is present
		if( self.IsEmpty() == False ):
			self.DeleteAllItems()
		
		ArtIDs = [ 'wx.ART_FOLDER', 'wx.ART_FOLDER_OPEN', 'wx.ART_NORMAL_FILE' ]
		
		il = wx.ImageList( 16, 16 )
		for items in ArtIDs:
			pic = wx.ArtProvider_GetBitmap(eval(items), wx.ART_TOOLBAR, ( 16, 16 ) )
			il.Add( pic )
		
		self.AssignImageList( il )
	
		prjname = projectname[0:-4]
		treeroot = self.AddRoot( str( prjname ), 1, 0, wx.TreeItemData( projectname ) )
		self.SetItemHasChildren( treeroot, True )
	
		for item in structure[ 'files' ]:
			# split = WpFileSystem.SplitFilepath( item )
			data = {
				'path': structure[ 'path' ],
				'fname': item,
				'fullpath': structure[ 'path' ]+item
			}
			self.AppendItem( treeroot, item, 2, 2, wx.TreeItemData( data ) )
			
		self.Expand( treeroot )
