# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpNoteBook
# Desc: Class for setting up main notebook interface
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import wx
import wx.lib.flatnotebook as fnb

from gui.WpTextEditor import WpTextEditor
from wx.lib.pubsub import Publisher as pub

class WpNoteBook( fnb.FlatNotebook ):
	def __init__( self, parent ):
		self.parent = parent
		fnb.FlatNotebook.__init__( self, parent, wx.ID_ANY, style=wx.EXPAND )
                self.Setup()
                pub.subscribe(self.addPageSubscriber, 'notebook.addpage')

        def addPageSubscriber(self, message):
            self.AddDefaultPage(message.data)

        def Setup(self):
                ## Active tab color
                self.SetActiveTabColour('#99CC00')

                ## Image list for this notebook
                imagelist = wx.ImageList(16,16)
		imagelist.Add(wx.Bitmap("./gui/icons/emblem-system.png", wx.BITMAP_TYPE_PNG))
                imagelist.Add(wx.Bitmap("./gui/icons/text-x-generic.png", wx.BITMAP_TYPE_PNG))

                self.SetImageList(imagelist)

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
	# Add default page
	# @param string filepath <conditional>
	#---------------------------------------------------------------
	def AddDefaultPage( self, filepath=None ):
		title = ' : empty'
		
		##
		# Testing if the file is already open
		##
		numpages = self.GetPageCount()
		dontreload = False

		for index in range( 0, numpages ):
			pagepath = self.GetPage( index ).GetFilePath()
			
			if( pagepath is None ):
				continue
			elif( pagepath == filepath ):
				dontreload = True
				foundindex = index
			
		##
		# Don't let the users open the same file multiple times
		##
		if( dontreload == False ):
			if filepath is None:
				filepath = None
			else:
				split = os.path.split( filepath )
				filepath = filepath
				title = split[ 1 ]
				
			##
			# Keeps notebook from flickering when adding pages. See Thaw later in this function.
			##
			self.Freeze()
			
			##
			# Make use of the very first page that is empty
			##
			
			
			### TODO: REWRITE THIS IF TEST
			"""
			if( numpages == 0 ):
				self.AddPage( self._AddTextEditor( None ), title, True )
			else:
				if( self.GetPage( 0 ).GetFilePath() == None and len( self.GetPage( 0 ).GetText() ) == 0 ):
					self.DeletePage( 0 )
				
				if( title == '< empty >' ):
					filepath = None
				
				self.AddPage( self._AddTextEditor( filepath ), title, True )
			
			"""
			if( numpages > 0 and self.GetPage( 0 ).GetFilePath() == None and len( self.GetPage( 0 ).GetText() ) == 0 and filepath != None):
				title = os.path.split( filepath )[ 1 ]
				self.SetPageText( 0, title )
				self.GetPage( 0 ).SetFilePath( filepath )
				print "We should not be in here right now"
				# self.GetPage( 0 ).EmptyUndoBuffer()
			else:
				self.AddPage( self._AddTextEditor( filepath ), title, True, 1 )
	
			##
			# Thawing
			##
			self.Thaw()
		else:
			##
			# File is already opened, focus it
			##
			self.SetSelection( foundindex )
