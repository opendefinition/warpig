# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpTextEditor
# Desc: Class for managing texteditor found in a tab
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import keyword
import os
import wx

from system.WpFileSystem import WpFileSystem

class WpTextEditor( wx.stc.StyledTextCtrl ):
	_curr_file_path = None
	
	def __init__( self, parent ):
		self.parent = parent
		##
		# We always construct parent with wx.TE_MULTILINE
		##
		wx.stc.StyledTextCtrl.__init__( self, parent, style=wx.TE_MULTILINE )
		
		##
		# Setup default styles
		##
		self.SetMarginType( 0, wx.stc.STC_MARGIN_NUMBER ) 	# Line numbering
		self.SetMarginWidth( 0, 35 ) 						# Margin for line numbering
		self.SetEdgeColour( "#555753" )
		self.SetEdgeColumn( 200 )
		self.SetEdgeMode( wx.stc.STC_EDGE_LINE )
		
		##
		# Fonts
		##
		font = wx.Font(
				11,						# Pointsize
				wx.FONTFAMILY_SWISS,	# Family
				wx.NORMAL,				# Style
				wx.NORMAL,				# Weight
				0,						# Underline
				'Verdana',				# Face
				wx.FONTENCODING_UTF8	# ENCODING
			)
		
		##
		# Code folding
		# see: http://www.python-forum.org/pythonforum/viewtopic.php?f=2&t=10065
		##
		"""
		self.SetProperty("fold", "1")
		self.SetMargins(0, 0)
		self.SetViewWhiteSpace(False)
		self.SetEdgeMode(wx.stc.STC_EDGE_BACKGROUND)
		self.SetEdgeColumn(78)
		
		# setup a margin to hold the fold markers
		self.SetMarginType(2, wx.stc.STC_MARGIN_SYMBOL)
		self.SetMarginMask(2, wx.stc.STC_MASK_FOLDERS)
		self.SetMarginSensitive(2, True)
		self.SetMarginWidth(2, 12)
		
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_VLINE, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_LCORNER, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUSCONNECTED, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUSCONNECTED, "white", "#808080")
		self.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_TCORNER, "white", "#808080")	
		"""
		
		self.StyleSetFont( 0, font )
		self.SetDefaultLexer()
		self.SetFocus()
		
		self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		
		
	#---------------------------------------------------------------
	# Get filepath defined for this instance of WpTextEditor
	# @return self
	#---------------------------------------------------------------
	def GetFilePath( self ):
		return self._curr_file_path
	
	#---------------------------------------------------------------
	# Get filepath defined for this instance of WpTextEditor
	# @return self
	#---------------------------------------------------------------	
	def SetFilePath( self, filepath ):
		self._curr_file_path = filepath
		
		self.SetTextUTF8(
				WpFileSystem.ReadFromFile( self._curr_file_path )
			)
		
		return self
	
	#---------------------------------------------------------------
	# Set lexer for this editor instance
	#---------------------------------------------------------------	
	def SetDefaultLexer( self ):
		# self.SetLexer( wx.stc.STC_LEX_PYTHON )
		self.SetLexerLanguage( 'python' )
	
		keys = keyword.kwlist[ : ]
		
		##
		# Global default styles for all languages
		##
		self.StyleClearAll()  # Reset all to be like the default
		
		##
		# Global default styles for all languages
		##
		self.StyleSetSpec( 0, "back:#232323,fore:#FFFFFF")
		self.StyleSetSpec( wx.stc.STC_STYLE_DEFAULT, "back:#232323,fore:#505151")	
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACELIGHT, "fore:#00FF00,back:#232323,bold" )
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACEBAD, "fore:#00FF00,back:#232323,bold" )
		
		##
		# Python styles
		##
		
		"""
		bold                    turns on bold
		italic                  turns on italics
		fore:[name or #RRGGBB]  sets the foreground colour
		back:[name or #RRGGBB]  sets the background colour
		face:[facename]         sets the font face name to use
		size:[num]              sets the font size in points
		eol                     turns on eol filling
		underline               turns on underlining

		"""
		
		##
		# Default
		##
		self.StyleSetSpec( wx.stc.STC_P_DEFAULT, "fore:#000000,back:#232323" )
	
		##
		# Linenumbers
		##
		self.StyleSetSpec( wx.stc.STC_STYLE_LINENUMBER, "fore:#555753,back:#232323" )
		
		##
		# Comments
		##
		self.StyleSetSpec( wx.stc.STC_P_COMMENTLINE, "fore:#00FF00,back:#232323" )
		
		##
		# Comment-blocks
		##
		self.StyleSetSpec( wx.stc.STC_P_COMMENTBLOCK, "fore:#00FF00,back:#232323" )
		
		##
		# Number
		##
		self.StyleSetSpec( wx.stc.STC_P_NUMBER, "fore:#D42C5C,back:#232323" )
		
		##
		# String
		##
		self.StyleSetSpec( wx.stc.STC_P_STRING, "fore:#C83430,back:#232323" )
	
		##
		# Single quoted string
		##
		self.StyleSetSpec( wx.stc.STC_P_CHARACTER, "fore:#C83430,back:#232323" )  
		
		##
		# Keyword
		##
		self.StyleSetSpec( wx.stc.STC_P_WORD, "fore:#097AC2,bold,back:#232323" )
		
		##
		# Triple quotes
		##
		self.StyleSetSpec( wx.stc.STC_P_TRIPLE, "fore:#C83430back:#232323" ) 
		
		##
		# Triple double quotes
		##
		self.StyleSetSpec( wx.stc.STC_P_TRIPLEDOUBLE, "fore:#C83430,back:#232323" )
		
		##
		# Class name definition
		##
		self.StyleSetSpec( wx.stc.STC_P_CLASSNAME, "fore:#E78B0B,back:#232323" )
		
		##
		# Function or method name definition
		##
		self.StyleSetSpec( wx.stc.STC_P_DEFNAME, "fore:#E78B0B,back:#232323" )
		
		##
		# Operators
		##
		self.StyleSetSpec( wx.stc.STC_P_OPERATOR, "fore:#00FF00,back:#232323" )
		
		##
		# Identifiers
		##
		self.StyleSetSpec( wx.stc.STC_P_IDENTIFIER, "fore:#E5E5E5,back:#232323" )
		
		##
		# End of line where string is not closed
		##
		self.StyleSetSpec( wx.stc.STC_P_STRINGEOL, "fore:#55FF55,back:#232323" )
		
		##
		# Caret
		##
		self.SetCaretForeground( '#0A75B9' )
		self.SetCaretWidth( 2 )
		
		##
		# Keywords
		##
		self.SetKeyWords( 0, " ".join( keyword.kwlist ) )
		
	def OnKeyDown( self, event ):
		print event.GetUniChar()
		
		if( event.CmdDown() == True ):
			if( event.GetUniChar() == 83 ):
				print "We are trying to save"
				self.SaveFile()
			
			##
			# Add new page with editor to current notebook instance
			##
			if( event.GetUniChar() == 78 ):
				self.parent.AddDefaultPage()
				
			if( event.GetUniChar() == 79 ):
				print "We are trying to open a file"
				
			##
			# Close current tab where this instance of the editor resides
			#
			if( event.GetUniChar() == 87 ):
				page = self.parent.GetSelection()
				self.Parent.DeletePage( page )
		
				if( self.Parent.GetPageCount() ):
					select = self.Parent.GetSelection()
					self.Parent.SetSelection( 0 )
					self.Parent.SetSelection( select )

				self.Destroy()
				
			if( event.GetUniChar() == 81 ):
				print "We are trying to close this application"
				self.Close()
			
		event.Skip()
		
	#---------------------------------------------------------------
	# Handling saving of file
	#---------------------------------------------------------------
	def SaveFile( self ):
		path = self.GetFilePath()
		
		if( path == None ): 
			dialog = wx.FileDialog ( self, style = wx.SAVE )
			response = dialog.ShowModal()
			
			if( response == wx.ID_OK ):
				path = dialog.GetPath()
				split = os.path.split( path )
				self.parent.SetPageText( self.parent.GetSelection(), split[ 1 ] )
				dialog.Destroy()
	
		WpFileSystem.SaveToFile( self.GetTextUTF8(), path )
		
		##
		# Make sure the editor got the filepath set
		##
		self.SetFilePath( path )