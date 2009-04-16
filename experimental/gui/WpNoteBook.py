import os
import wx
import wx.lib.flatnotebook as fnb

from gui.WpTextEditor import WpTextEditor 

class WpNoteBook( fnb.FlatNotebook ):
	def __init__( self, parent ):
		self.parent = parent
		##
		# We always construct parent with wx.TE_MULTILINE
		##
		fnb.FlatNotebook.__init__( self, parent, wx.ID_ANY, style=wx.EXPAND )

	#---------------------------------------------------------------
	# Add text editor to page
	# @param string filepath <conditional>
	# @return object texteditor
	#---------------------------------------------------------------
	def _AddTextEditor( self, filepath=None):
		texteditor = WpTextEditor( self )
		# Adding content
		if filepath is not None:
			texteditor.SetFilePath( filepath )
			texteditor.SetDefaultLexer()
			
		return texteditor
	
	#---------------------------------------------------------------
	# Add defualt page
	# @param string filepath <conditional>
	#---------------------------------------------------------------
	def AddDefaultPage( self, filepath=None ):
		title = '< empty >'
		
		if filepath is None:
			filepath = None
		else:
			split = os.path.split( filepath )
			filepath = filepath
			title = split[ 1 ]
            
		self.AddPage( self._AddTextEditor( filepath ), title, True )
		
