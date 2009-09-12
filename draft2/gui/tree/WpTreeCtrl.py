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
from gui.tree.WpProjectData import WpProjectData
from gui.tree.WpElementData import WpElementData

class WpTreeCtrl( wx.TreeCtrl ):
	def __init__( self, parent ):
		wx.TreeCtrl.__init__( self, parent, 9999, style=wx.ALL | wx.TR_DEFAULT_STYLE | wx.EXPAND )
		
	#---------------------------------------------------------------
	# Populate treecontroller
	# @param unknown structure
	# @param string projectname
	#---------------------------------------------------------------
	def PopulateTree( self, filepath ):
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
		
		## Setup project information
		projectInformation = WpProjectData()
		projectInformation.setProjectName(str(project['project']['name']))
		treeroot = self.AddRoot(
							projectInformation.getProjectName(), 
							0, 
							1, 
							wx.TreeItemData(projectInformation)
						)
						
		self.SetItemHasChildren( treeroot, True )
		
		root = treeroot
		ids = {root: treeroot}
		
		## Build projecttree by looping over current directory listing
		for dir in project[ 'dir' ]:
			dlist = WpFileSystem.ListDirectory( dir )
		
			## Prepare basic information for node
			path = os.path.split(dir)[1]
			subrootInformation = WpElementData()
			subrootInformation.setCurrentDirectory(path)
			
			subroot = self.AppendItem(treeroot, path, 0, 1, wx.TreeItemData(subrootInformation))
			self.SetItemHasChildren( subroot, True )
			
			ids = {dir: subroot}
			
			## Build directories and filenames
			for( dirpath, dirnames, filenames ) in dlist[ 'files' ]:
				for dirname in dirnames:
					directoryInformation = WpElementData()
					directoryInformation.setCurrentDirectory(os.path.join( dirpath, dirname))
					ids[directoryInformation.getCurrentDirectory()] = self.AppendItem( 
															ids[dirpath], 
															dirname, 
															0, 
															1, 
															wx.TreeItemData(directoryInformation)
														)
					
				for filename in sorted(filenames):
					fileInformation = WpElementData()
					fileInformation.setCurrentDirectory(dirpath)
					fileInformation.setCurrentFilename(filename)
					fileInformation.setCurrentFile(
											os.path.join(
												fileInformation.getCurrentDirectory(),
												fileInformation.getCurrentFilename()
											)
										)
					
					self.AppendItem(
							ids[fileInformation.getCurrentDirectory()],
							fileInformation.getCurrentFilename(),
							2,
							2,
							wx.TreeItemData(fileInformation)
						)
					
		self.Parent.Parent.Parent.ResizeSash()
		
		self.SetupBindings()
		
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
		
	#----------------------------------------------------------------
	# On selecting element (directory or file) inside treecontroller
	#----------------------------------------------------------------
	def _OnSelChanged( self, event ):
		nodedata = self.GetPyData(event.GetItem())
		
		## Can we open the file in our editor?
		if nodedata.__class__.__name__ == 'WpElementData':
			if nodedata.getCurrentFile() != None:
				## Test passed, open file
				self.Parent.rightpanel.notebook.AddDefaultPage(nodedata.getCurrentFile())