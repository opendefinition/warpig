# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpNewProject
# Desc: Class for handling operations regarding a project
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import re
import wx
import wx.lib.buttons as buttons

from wx.lib.agw.multidirdialog import MultiDirDialog
from system.WpFileSystem import WpFileSystem

class WpNewProject( wx.Dialog ):
	def __init__( self, treectrl ):
		self._treectrl = treectrl
		
		wx.Dialog.__init__( self, None, 6666, 'New Project', size=(500, 300) )
		
		##
		# Main Panel
		##
		mainpanel = wx.Panel(self, -1, size=(500,500), style=wx.EXPAND )
		mainsizer = wx.BoxSizer( wx.VERTICAL )
		panelsizer = wx.FlexGridSizer( 3, 1, 0, 0 )
		
		##
		# Projectname
		##
		prjnamesizer = wx.BoxSizer( wx.HORIZONTAL )
		prjnamelabel = wx.StaticText( mainpanel, -1, 'Name' )
		self.prjnameinput = wx.TextCtrl( mainpanel, -1 )
		
		prjnamesizer.Add( prjnamelabel, 0, wx.EXPAND | wx.ALL, 5 )
		prjnamesizer.Add( self.prjnameinput , 1, wx.EXPAND | wx.ALL, 5 )
		
		##
		# Controls for adding files to project
		##
		prjfilesizer =wx.BoxSizer( wx.HORIZONTAL )
		
		self.filelist = wx.ListCtrl( mainpanel, 
								-1,
								style=wx.BORDER_SUNKEN 
									| wx.LC_REPORT
									| wx.LC_VRULES
									| wx.LC_HRULES
								)
		
		self.filelist.InsertColumn( 0, 'Path' )
		self.filelist.SetColumnWidth( 0, 1000 )

		fileactionsizer = wx.BoxSizer( wx.VERTICAL )

		imageadd = wx.Image( "./gui/icons/list-add.png", wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		imagerem = wx.Image( "./gui/icons/list-remove.png", wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
		
		addfilebutton = wx.BitmapButton( mainpanel,
										11, 
										bitmap=imageadd, 
										pos=(10,20), 
										size=(imageadd.GetWidth(), imageadd.GetHeight() ),
										style=wx.NO_BORDER
										)
		remfilebutton = wx.BitmapButton( mainpanel,
										12, 
										bitmap=imagerem, 
										pos=(10,20), 
										size=(imagerem.GetWidth(), imagerem.GetHeight() ),
										style=wx.NO_BORDER
										)
		
		fileactionsizer.Add( addfilebutton )
		fileactionsizer.Add( remfilebutton )
	
		prjfilesizer.Add( self.filelist, 1, wx.EXPAND | wx.ALL, 5 )
		prjfilesizer.Add( fileactionsizer )
		
		##
		# Save and cancel buttons
		##
		buttonsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		savebutton = buttons.ThemedGenButton( mainpanel, 13, 'Save' ) 
		cancelbutton = buttons.ThemedGenButton( mainpanel, 14, 'Cancel' )
		
		buttonsizer.Add( cancelbutton, 0, wx.EXPAND | wx.ALL, 5 )
		buttonsizer.Add( savebutton, 1, wx.EXPAND | wx.ALL, 5 )
		
		##
		# Sewing things together
		##
		panelsizer.AddMany(
			[
				( prjnamesizer, 1, wx.EXPAND ),
				( prjfilesizer, 1, wx.EXPAND ),
				( buttonsizer, 1, wx.EXPAND )
			]
		)
		
		panelsizer.AddGrowableRow( 1 )
		panelsizer.AddGrowableCol( 0 )
	
		##
		# Set the main sizer to panel
		##
		mainsizer.Add( panelsizer, 1, wx.EXPAND )
		
		self.SetSizer( mainsizer )
		
		##
		# Bindings
		##
		self.Bind( wx.EVT_BUTTON, self._onAssociateFiles, id=11)
		self.Bind( wx.EVT_BUTTON, self._onRemovingFilesFromProject, id=12)
		self.Bind( wx.EVT_BUTTON, self._onSave, id=13 )
		self.Bind( wx.EVT_BUTTON, self._onCancel, id=14 )

		self.Center()
	
	#---------------------------------------------------------------
	# On adding files to project
	#---------------------------------------------------------------
	def _onAssociateFiles( self, event ):
  		dialog = wx.lib.agw.multidirdialog.MultiDirDialog( None, 'New Project', 'Associate folders', defaultPath='/Users' )
  		
  		if dialog.ShowModal() == wx.ID_OK:
			paths = dialog.GetPaths()
			
			count = self.filelist.GetItemCount()+1
			for path in paths:
				# If on Mac, remove "Macintosh HD"
				macfilter = re.compile( "Macintosh HD" )
			
				if( macfilter.search( path ) != None ):
					path = path[12:len(path)]
			
				self.filelist.InsertStringItem( count, path )
				count += 1
		
		dialog.Destroy()
		
	def _onRemovingFilesFromProject( self, event ):
		pos = self.filelist.GetFirstSelected()
		tmp = []
		
		while pos != -1:
			tmp.append( pos )
			pos = self.filelist.GetNextSelected( pos )
			
		tmp.sort()
		tmp.reverse()
		
		for thingy in tmp:
			self.filelist.DeleteItem( thingy ) 

	#---------------------------------------------------------------
	# Cancel inside project dialog
	#---------------------------------------------------------------
	def _onCancel( self, event ):
		self.Close()
		
	#---------------------------------------------------------------
	# On saving project
	#---------------------------------------------------------------
	def _onSave( self, event ):
		self.Close()
		path = './projects/' + "/" + self.prjnameinput .GetValue() + ".wpf"
		
		##
		# Get all paths that belongs to this project
		##
		dir = []
		numpaths = self.filelist.GetItemCount()
		
		for index in range( 0, numpaths ):
			dir.append( self.filelist.GetItem( index, 0 ).GetText() )
		
		projectfile = WpFileSystem.SaveProjectFile( path, dir )
		self._treectrl.treectrl.PopulateTree( projectfile )