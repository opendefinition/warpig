# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpSplitRightPanel
# Author: Roger C.B. Johnsen
#==================================================================================================

import os
import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

from gui.WpTextEditor import WpTextEditor 

from system.WpFileSystem import WpFileSystem

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
		# self.AddDefaultPage()
		
		return self.notebook
		
	def _AddTextEditor( self, filepath=None):
		texteditor = WpTextEditor( self.notebook )
		# Adding content
		if filepath is not None:
			texteditor.SetFilePath( filepath )
			texteditor.SetDefaultLexer()
			
		return texteditor
	
	#===============================================================================================
	# Helper functions
	#===============================================================================================
	def AddDefaultPage( self, filepath=None ):
		title = '< empty >'
		
		if filepath is None:
			filepath = None
		else:
			split = os.path.split( filepath )
			filepath = filepath
			title = split[ 1 ]
            
		self.notebook.AddPage( self._AddTextEditor( filepath ), title )

	def SaveFile( self ):
		focus = self.FindFocus()
		
		if( type( focus ).__name__ == 'WpTextEditor' ):
			# filename = self.notebook.GetPageText( self.notebook.GetSelection() )
		
			dialog = wx.FileDialog ( None, style = wx.SAVE )
			
			if( focus.GetFilePath != None ):
				path = focus.GetFilePath()
			else: 
				if dialog.ShowModal() == wx.ID_OK:
					path = dialog.GetPath()
					split = os.path.split( path )
				
					self.notebook.SetPageText( self.notebook.GetSelection(), split[ 1 ] )
			
					dialog.Destroy()		
		
			WpFileSystem.SaveToFile( focus.GetTextUTF8(), path )
			
	def FindFileName( self, filepath ):
		length = len( filepath )
		startindex = filepath.rfind( '/' )+1
		
		return filepath[startindex:length]