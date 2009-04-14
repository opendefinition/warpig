# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpTextEditor
# Author: Roger C.B. Johnsen
#==================================================================================================

import keyword
import wx

from system.WpFileSystem import WpFileSystem

class WpTextEditor( wx.stc.StyledTextCtrl ):
	_curr_file_path = None
	
	def __init__( self, parent ):
		# We always construct parent with wx.TE_MULTILINE
		wx.stc.StyledTextCtrl.__init__( self, parent, style=wx.TE_MULTILINE )
		
		# Setup default styles
		self.SetMarginType( 0, wx.stc.STC_MARGIN_NUMBER ) 	# Line numbering
		self.SetMarginWidth( 0, 35 ) 						# Margin for line numbering
		
		# Fonts
		font = wx.Font(
				11,						# Pointsize
				wx.FONTFAMILY_SWISS,	# Family
				wx.NORMAL,				# Style
				wx.NORMAL,				# Weight
				0,						# Underline
				'verdana',				# Face
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
		
	def GetFilePath( self ):
		"""
		Get filepath defined for this instance of WpTextEditor
		@return self
		"""
		return self._curr_file_path
		
	def SetFilePath( self, filepath ):
		"""
		Set filepath defined for this instance of WpTextEditor. 
		Will autoload content into current editor instance.
		
		@param string filepath
		@return self
		"""
		self._curr_file_path = filepath
		
		self.SetTextUTF8(
				WpFileSystem.ReadFromFile( self._curr_file_path )
			)
		
		return self
		
	def SetDefaultLexer( self ):
		# self.SetLexer( wx.stc.STC_LEX_PYTHON )
		# self.SetLexerLanguage( 'php' )
		self.SetLexerLanguage( 'python' )
	
		keys = keyword.kwlist[ : ]
		
		#== Setup lexer styles ==#
		
		# Global default styles for all languages
		self.StyleClearAll()  # Reset all to be like the default
		
		# Global default styles for all languages
		self.StyleSetSpec( 0, "back:#00008B,fore:#FFFFFF")
		self.StyleSetSpec( wx.stc.STC_STYLE_DEFAULT, "back:#00008B,fore:#505151")	
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACELIGHT, "fore:#00FF00,back:#00008B,bold" )
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACEBAD, "fore:#00FF00,back:#00008B,bold" )
		
		#== Python styles ==#
		
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
		
		self.StyleSetSpec( wx.stc.STC_STYLE_LINENUMBER, "fore:yellow,back:#00008B" )
		
		
		# Default
		self.StyleSetSpec( wx.stc.STC_P_DEFAULT, "fore:#00FF00,back:#00008B" )
	
		# Comments
		self.StyleSetSpec( wx.stc.STC_P_COMMENTLINE, "fore:#00FF00,back:#00008B" )
		
		# Number
		self.StyleSetSpec( wx.stc.STC_P_NUMBER, "fore:#FFFF00,back:#00008B" )
		
		# String
		self.StyleSetSpec( wx.stc.STC_P_STRING, "fore:orange,back:#00008B" )
		
		# Single quoted string
		self.StyleSetSpec( wx.stc.STC_P_CHARACTER, "fore:orange,back:#00008B" )  
		
		# Keyword
		self.StyleSetSpec( wx.stc.STC_P_WORD, "fore:magenta,bold,back:#00008B" )
		
		# Triple quotes
		self.StyleSetSpec( wx.stc.STC_P_TRIPLE, "fore:#00FF00,back:#00008B" ) 
		
		# Triple double quotes
		self.StyleSetSpec( wx.stc.STC_P_TRIPLEDOUBLE, "fore:#00FF00,back:#00008B" )
		
		# Class name definition
		self.StyleSetSpec( wx.stc.STC_P_CLASSNAME, "fore:cyan,back:#00008B" )
		
		# Function or method name definition
		self.StyleSetSpec( wx.stc.STC_P_DEFNAME, "fore:cyan,back:#00008B" )
		
		# Operators
		self.StyleSetSpec( wx.stc.STC_P_OPERATOR, "fore:#00FF00,back:#00008B" )
		
		# Identifiers
		self.StyleSetSpec( wx.stc.STC_P_IDENTIFIER, "fore:#FFFF00,back:#00008B" )
		
		# Comment-blocks
		self.StyleSetSpec( wx.stc.STC_P_COMMENTBLOCK, "fore:#336699,back:#00008B" )
		
		# End of line where string is not closed
		self.StyleSetSpec( wx.stc.STC_P_STRINGEOL, "fore:#FFFF00,back:#00008B" )
		
		self.SetCaretForeground( '#00FF00' )
		self.SetCaretWidth( 2 )
		self.SetKeyWords( 0, " ".join( keyword.kwlist ) )