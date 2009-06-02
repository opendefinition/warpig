# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpTreeCtrl
# Desc: Class for managing file tree controll
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import wx

from system.WpFileSystem import WpFileSystem
from gui.WpProgressDialog import WpProgressDialog

class WpTreeCtrl( wx.TreeCtrl ):
	def __init__( self, parent ):
		wx.TreeCtrl.__init__( self, parent, 9999, style=wx.ALL | wx.TR_DEFAULT_STYLE | wx.EXPAND )
		
	#---------------------------------------------------------------
	# Populate treecontroller
	# @param unknown structure
	# @param string projectname
	#---------------------------------------------------------------
	def PopulateTree( self, filepath ):
	
		##
		# Testing
		##
		"""
		progress = WpProgressDialog( "Opening project files" )
		progress.AppendStatusText( "Something" )
		progress.Show()
		"""
		self.SetIndent( 5 )
		project = WpFileSystem.LoadProjectFile( filepath )
	
		# Destroying all content if content is present
		if( self.IsEmpty() == False ):
			self.DeleteAllItems()
		
		ArtIDs = [ 'wx.ART_FOLDER', 'wx.ART_FOLDER_OPEN', 'wx.ART_NORMAL_FILE' ]
		
		il = wx.ImageList( 16, 16 )
		for items in ArtIDs:
			pic = wx.ArtProvider_GetBitmap(eval(items), wx.ART_TOOLBAR, ( 16, 16 ) )
			il.Add( pic )
		
		self.AssignImageList( il )
		
		prjname = project[ 'project' ][ 'name' ]
		treeroot = self.AddRoot( str( prjname ), 0, 1, wx.TreeItemData( prjname ) )
		self.SetItemHasChildren( treeroot, True )
		
		root = treeroot
		ids = {root: treeroot}
		
		for dir in project[ 'dir' ]:
			dlist = WpFileSystem.ListDirectory( dir )
			
			subroot = self.AppendItem( treeroot, os.path.split(dir)[1], 0, 1, wx.TreeItemData( None ) )
			self.SetItemHasChildren( subroot, True )
			
			ids = {dir: subroot}
			
			for( dirpath, dirnames, filenames ) in dlist[ 'files' ]:
				for dirname in dirnames:
					fullpath = os.path.join( dirpath, dirname )
					ids[ fullpath ] = self.AppendItem( ids[ dirpath ], dirname, 0, 1, wx.TreeItemData( None ) )
					
				for filename in sorted( filenames ):
					data = {
							'path': dirpath,
							'fname': filename,
							'fullpath': os.path.join( dirpath, filename )
						}
					self.AppendItem( ids[ dirpath ], filename, 2, 2, wx.TreeItemData( data ) )
					
		self.Parent.Parent.Parent.Parent.ResizeSash()
		
		self.SetupBindings()
		
		# progress.Close()
		
	def SetupBindings( self ):
		self.Bind( wx.EVT_TREE_SEL_CHANGED, self._OnSelChanged, id=9999 )
		self.Bind( wx.EVT_TREE_ITEM_MENU, self._OnTreeRightClick, id=wx.ID_ANY )
		
	##
	# Bindings
	##
	def _OnTreeRightClick( self, event ):
		menu = wx.Menu()
		
		newmenu = wx.Menu()
		newfile = wx.MenuItem( newmenu, wx.ID_ANY,"New file" )
		newfolder = wx.MenuItem( newmenu, wx.ID_ANY,"New folder" )
		newmenu.AppendItem( newfile )
		newmenu.AppendItem( newfolder )
		
		delete = wx.MenuItem( menu, wx.ID_ANY,"Delete" )
		refreshtree = wx.MenuItem( menu, wx.ID_ANY,"Refresh tree" )
		
		menu.AppendMenu( wx.ID_ANY, 'New', newmenu )
		menu.AppendItem( delete )
		menu.AppendSeparator()
		menu.AppendItem( refreshtree )
		
		self.PopupMenu(menu)
		menu.Destroy()
		
	#---------------------------------------------------------------
	# On selecting file inside treecontroller
	#---------------------------------------------------------------
	def _OnSelChanged( self, event ):
		filedata = self.GetPyData( event.GetItem() )
		
		try:
			self.Parent.rightpanel.notebook.AddDefaultPage( filedata[ 'fullpath' ] )
		except TypeError:
			##
			# When this occur we are double clicking on a node
			# without a path set. E.g. projectnode.
			##
			pass
