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

import wx

from system.WpFileSystem import WpFileSystem

class WpNewProject( wx.Dialog ):
	_projectpath = None

	def __init__( self, treectrl ):
		self._treectrl = treectrl
		
		wx.Dialog.__init__( self, None, 6666, 'New Project', size=(500, 300) )
		
		##
		# Main Panel
		##
		mainpanel = wx.Panel(self, -1, size=(500,500), style=wx.EXPAND )
		mainsizer = wx.BoxSizer( wx.VERTICAL )
		panelsizer = wx.BoxSizer( wx.VERTICAL )
		panelsizer = wx.FlexGridSizer( 3, 1, 0, 0 )
		
		##
		# Projectname
		##
		namesizer = wx.BoxSizer( wx.HORIZONTAL )
		
		projectnamelabel = wx.StaticText( mainpanel, -1, 'Projectname' )
		self.projectnamefield = wx.TextCtrl( mainpanel, -1 )
		
		namesizer.Add( projectnamelabel, 0, wx.EXPAND | wx.ALL, 5 )
		namesizer.Add( self.projectnamefield, 1, wx.EXPAND | wx.ALL, 5 )
		
		##
		# Button for adding files to project
		##
		filesizer = wx.BoxSizer( wx.VERTICAL )
		filebuttonsizer = wx.BoxSizer( wx.HORIZONTAL )
		filefoldersizer = wx.BoxSizer( wx.VERTICAL )
		
		filebutton = wx.Button( mainpanel, 12, 'Associate Files To Project' )
		self.chosenfolderlabel = wx.StaticText( mainpanel, -1, '' )
		self.chosenfolderpath  = wx.StaticText( mainpanel, -1, '' )
		
		filebuttonsizer.Add( filebutton, 1, wx.EXPAND | wx.ALL, 30 )
		filefoldersizer.Add( self.chosenfolderlabel, 0, wx.EXPAND | wx.ALL, 5 )
		filefoldersizer.Add( self.chosenfolderpath, 1, wx.EXPAND | wx.ALL, 5 )
		
		filesizer.Add( filebuttonsizer, 1, wx.EXPAND )
		filesizer.Add( filefoldersizer, 1, wx.EXPAND )
		
		##
		# Save and cancel buttons
		##
		buttonsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		savebutton = wx.Button( mainpanel, 13, 'Save' ) 
		cancelbutton = wx.Button( mainpanel, 14, 'Cancel' )
		
		buttonsizer.Add( cancelbutton, 0, wx.EXPAND | wx.ALL, 5 )
		buttonsizer.Add( savebutton, 1, wx.EXPAND | wx.ALL, 5 )
	
		##
		# Sewing things together
		##
		panelsizer.AddMany(
			[
				( namesizer, 1, wx.EXPAND ),
				( filesizer, 1, wx.EXPAND ),
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
		self.Bind( wx.EVT_BUTTON, self._onAssociateFiles, id=12)
		self.Bind( wx.EVT_BUTTON, self._onSave, id=13 )
		self.Bind( wx.EVT_BUTTON, self._onCancel, id=14 )

		self.Center()
	
	#---------------------------------------------------------------
	# On adding files to project
	#---------------------------------------------------------------
	def _onAssociateFiles( self, event ):
		filters = 'WarPig Project File (*.wpf)|*.wpf'
  		dialog = wx.DirDialog ( None, 'New Project', style = wx.OPEN )
  		
  		if dialog.ShowModal() == wx.ID_OK:
			path = dialog.GetPath()
			self._projectpath = path
			
			self.chosenfolderlabel.SetLabel( "Folder: " )
			self.chosenfolderpath.SetLabel( path )
		
		dialog.Destroy()
	
	#---------------------------------------------------------------
	# Cancel inside project dialog
	#---------------------------------------------------------------
	def _onCancel( self, event ):
		self.Close()
		
	#---------------------------------------------------------------
	# On saving project
	#---------------------------------------------------------------
	def _onSave( self, event ):
		path = './projects/' + "/" + self.projectnamefield.GetValue() + ".wpf"
		information = WpFileSystem.SaveProjectFile( path, (self._projectpath+"/")  )
		self._treectrl.treectrl.PopulateTree( information[ 'dirlist' ], information[ 'fname' ] )

		self.Close()