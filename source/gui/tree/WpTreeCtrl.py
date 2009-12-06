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
import re

from system.WpFileSystem import WpFileSystem
from gui.tree.WpProjectData import WpProjectData
from gui.tree.WpElementData import WpElementData
from system.WpProject import WpProject
from gui.guid.guid import *

from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpConfigSystem import WpConfigSystem

# Interprocess communications
from wx.lib.pubsub import Publisher as pub

class WpTreeCtrl( wx.TreeCtrl ):
	def __init__( self, parent ):
		wx.TreeCtrl.__init__( self, parent, CONST_WIDGET_PROJECT_TREE, style=wx.ALL | wx.TR_DEFAULT_STYLE | wx.EXPAND | wx.TR_HIDE_ROOT )
                self.configobj = WpConfigSystem()
                self.project = None
                pub.subscribe(self.populateSubscriber, 'projecttree.populate')

        def populateSubscriber(self, message):
            self.PopulateTree(message.data)
		
	def PopulateTree( self, projectobj ):
		"""
		Build and populate this instance of the projecttree
		@param Object WpProject
		"""

                self.project = projectobj

                ## Get configuration for this tree
                self.excludeprefix = self.configobj.settings['projecttree-prefixexclude']
                self.excludesuffix = self.configobj.settings['projecttree-suffixexclude']

                ## File and folder exclusions
                criteriasuffix = re.compile(self.excludesuffix)
                criteriaprefix = re.compile(self.excludeprefix)

		self.SetIndent(10)

		# Destroying all content if content is present
		alreadyopened = False
		if( self.IsEmpty() == False ):
			self.DeleteAllItems()
			alreadyopened = True
		
		ArtIDs = [ 'wx.ART_FOLDER', 'wx.ART_FOLDER_OPEN', 'wx.ART_NORMAL_FILE', 'wx.ART_HELP_FOLDER' ]
		
		il = wx.ImageList( 16, 16 )
		for items in ArtIDs:
			pic = wx.ArtProvider_GetBitmap(eval(items), wx.ART_TOOLBAR, ( 16, 16 ) )
			il.Add( pic )
		
		self.AssignImageList( il )
		
		## Setup project information
		projectInformation = WpProjectData()
		projectInformation.setProjectName(self.project.GetTitle())

                treeroot = self.AddRoot(
                                    projectInformation.getProjectName(),
                                    3,
                                    3,
                                    wx.TreeItemData(projectInformation)
				)

                ## Set project tree pane text to project name
                pub.sendMessage('mainframe.setpanetitle', {'pane': 'project', 'caption': projectInformation.getProjectName()})
	
		self.SetItemHasChildren(treeroot,True)
		self.SetItemBold(treeroot)
		self.SetItemBackgroundColour(treeroot, wx.Colour(162,181,205))

		root = treeroot
		ids = {root: treeroot}
		
		## Build projecttree by looping over current directory listing
		for dir in self.project.GetPaths():
			dlist = WpFileSystem.ListDirectory( dir )
		
			## Prepare basic information for node
			pathTitle = os.path.split(dir)[1]
			subrootInformation = WpElementData()
			subrootInformation.setCurrentDirectory(dir)
			
			subroot = self.AppendItem(treeroot, pathTitle, 0, 1, wx.TreeItemData(subrootInformation))
			self.SetItemHasChildren( subroot, True )
			
			ids = {dir: subroot}
			## Build directories and filenames
			for( dirpath, dirnames, filenames ) in dlist[ 'files' ]:
                            for dirname in dirnames:
                                directoryInformation = WpElementData()
                                directoryInformation.setCurrentDirectory(os.path.join( dirpath, dirname))
                                directoryInformation.setCurrentFile(
                                                        os.path.join(
                                                                subrootInformation.getCurrentDirectory(),
                                                                directoryInformation.getCurrentDirectory()
                                                            )
                                                    )

                                ids[directoryInformation.getCurrentDirectory()] = self.AppendItem(
                                                                                        ids[dirpath],
                                                                                        dirname,
                                                                                        0,
                                                                                        1,
                                                                                        wx.TreeItemData(directoryInformation)
                                                                                    )

                            for filename in sorted(filenames):
                                ## Exclude files
                                if re.search(criteriasuffix, filename) or re.search(criteriaprefix, filename):
                                    continue

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
		
		self.SetupBindings()

                ## Show the project tree
                pub.sendMessage('mainframe.showpane', 'project')
		
	def SetupBindings( self ):
		"""
		Setup the various bindings for this instance of the projecttree
		"""
		self.Bind( wx.EVT_TREE_SEL_CHANGED, self._OnSelChanged, id=CONST_WIDGET_PROJECT_TREE )
		self.Bind( wx.EVT_TREE_ITEM_MENU, self._OnTreeRightClick, id=wx.ID_ANY )
		self.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self._OnDoubleClick, id=wx.ID_ANY )
		
	#------------------------------------------------------------------
	# Bindings
	#------------------------------------------------------------------
	
	def _OnTreeRightClick( self, event ):
		"""
		Popup event handler for contect menu on right click
		inside the projecttree.
		"""
		mainMenu = wx.Menu()
		
		newMenu = wx.Menu()
		newFile = wx.MenuItem(newMenu, wx.ID_ANY,"New file")
		newFolder = wx.MenuItem(newMenu, wx.ID_ANY,"New folder")
		newMenu.AppendItem(newFile)
		newMenu.AppendItem(newFolder)
		
		delete = wx.MenuItem(mainMenu, wx.ID_ANY,"Delete")
		refreshTree = wx.MenuItem(mainMenu, wx.ID_ANY,"Refresh tree")
		
		mainMenu.AppendMenu(wx.ID_ANY, 'New', newMenu)
		mainMenu.AppendItem(delete)
		mainMenu.AppendSeparator()
		mainMenu.AppendItem(refreshTree)
		
		## Binding menu elements
		self.Bind(wx.EVT_MENU, self._OnPopupNewFile, id=newFile.GetId())
		self.Bind(wx.EVT_MENU, self._OnPopupNewFolder, id=newFolder.GetId())
                self.Bind(wx.EVT_MENU, self._OnPopupDelete, id=delete.GetId())
                self.Bind(wx.EVT_MENU, self._OnPopupRefreshTree, id=refreshTree.GetId())
		
		self.PopupMenu(mainMenu)
		mainMenu.Destroy()
		
	def _OnPopupNewFile(self, event):
		"""
		Popup event handler for creating new files by rightclicking 
		inside the projectree.
		"""
		selections = self.GetSelections()
		
		if len(selections) == 1:
			selected = selections[0]
			currentElementData = self.GetPyData(selected)
		
			dialog = wx.TextEntryDialog(self, '', 'Filename', '')
			
			if dialog.ShowModal() == wx.ID_OK:
				fileName = dialog.GetValue()
				newFilePath = os.path.join(currentElementData.getCurrentDirectory(), fileName)
				
				if os.path.isfile(newFilePath) == False:
					WpFileSystem.SaveToFile( '', newFilePath )
					
					## Adding new file to project tree
					nodedata = WpElementData()
					nodedata.setCurrentDirectory(currentElementData.getCurrentDirectory())
					nodedata.setCurrentFilename(fileName)
					nodedata.setCurrentFile(
									os.path.join(nodedata.getCurrentDirectory(),fileName)
								)
					
					if currentElementData.getCurrentFilename()  != None:
						selected = self.GetItemParent(selected)
								
					newFileItem = self.AppendItem(
									selected,
									fileName,
									2,
									2,
									wx.TreeItemData(nodedata)
								)
								
					self.EnsureVisible(newFileItem)
				else:
                                        dialog = wx.MessageDialog(None, 'File already exists', 'Warning', wx.OK | wx.ICON_QUESTION)
                                        if dialog.ShowModal() == wx.ID_OK:
                                                dialog.Destroy()
		
	def _OnPopupNewFolder(self, event):
		"""
		Popup event handler for creating new folders by rightclicking 
		inside the projectree.
		"""
		selections = self.GetSelections()
		
		if len(selections) == 1:
			selected = selections[0]
			currentElementData = self.GetPyData(selected)

			if currentElementData.__class__.__name__ != 'WpProjectData':
				dialog = wx.TextEntryDialog(self,'', 'Foldername', '')
		
				if dialog.ShowModal() == wx.ID_OK:
					folderName = dialog.GetValue()
					newFolderPath = os.path.join(currentElementData.getCurrentDirectory(), folderName)
			
					## Does this folder already exist?
					if os.path.isdir(newFolderPath) == False:
						os.mkdir(newFolderPath)
					
						## Append folder to tree
						nodeData = WpElementData()
						nodeData.setCurrentDirectory(currentElementData.getCurrentDirectory())
						nodeData.setCurrentFile(newFolderPath)
					
						if currentElementData.getCurrentFilename() != None:
							selected = self.GetItemParent(selected)
					
						newItem = self.PrependItem(
									selected,
									folderName,
									0,
									1,
									wx.TreeItemData(nodeData)
								)
						self.EnsureVisible(newItem)
					else:
						dialog = wx.MessageDialog(None, 'Folder already exists', 'Warning', wx.OK | wx.ICON_QUESTION)
                                                if dialog.ShowModal() == wx.ID_OK:
                                                    dialog.Destroy()
			
	def _OnPopupDelete(self, event):
            """
            Delete selected file or folder
            """
            selection = self.GetSelections()
            
            dialog = wx.MessageDialog(None, 'Are you sure?', 'Delete', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_ERROR)
            result = dialog.ShowModal()

            if result == wx.ID_YES:
                deletion_list = []

                for item in selection:
                    itemdata = self.GetPyData(item)
                    deletion_list.append(itemdata.getCurrentFile())
                    self.Delete(item)

                for item in deletion_list:
                    WpFileSystem.DeleteFromDisk(item)

        def _OnPopupRefreshTree(self, event):
            """
            Refresh/reload the project tree
            """
            self.PopulateTree(self.project)

        def _OnSelChanged(self, event):
		"""
		On selection change event handler. Occurs when we have clicked on
		a node inside the treecontroller.
		
		Note: For now this event handler will only make sure that the selected 
		node will be expanded.
		"""
		node = event.GetItem()
		self.Expand(node)
		
	def _OnDoubleClick(self,event):
            """
            On double click event handler.

            Note: This function will open a text file in the editor, if the tests below
            passes.
            """
            nodedata = self.GetPyData(event.GetItem())

            ## Can we open the file in our editor?
            if nodedata.__class__.__name__ == 'WpElementData':
                if nodedata.getCurrentFile() != None:
                    ## Is this a hidden folder? If so ,skip
                    if os.path.isdir(nodedata.getCurrentFile()) == False:
                        ## Test passed, open file
                        pub.sendMessage('notebook.addpage', nodedata.getCurrentFile())