# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpSplitLeftPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import os
import wx

class WpTreeCtrl( wx.TreeCtrl ):
	def __init__( self, parent ):
		wx.TreeCtrl.__init__( self, parent, 9999, style=wx.ALL | wx.EXPAND )
		
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
	
		# Removing trailing file extension
		prjname = projectname[0:-4]
		treeroot = self.AddRoot( str( prjname ), 0, 1, wx.TreeItemData( projectname ) )
		self.SetItemHasChildren( treeroot, True )
	
		root = structure[ 'files' ][ 0 ][ 0 ]
		ids = {root: treeroot}
		
		for ( dirpath, dirnames, filenames ) in structure[ 'files' ]:
			for dirname in dirnames:
				fullpath = os.path.join( dirpath, dirname )
				ids[ fullpath ] =  self.AppendItem( ids[ dirpath ], dirname, 0, 1 )
				
			for filename in sorted( filenames ):
				data = {
					'path': dirpath,
					'fname': filename,
					'fullpath': os.path.join( dirpath, filename )
				}
				self.AppendItem( ids[ dirpath ], filename, 2, 2, wx.TreeItemData( data ) )
