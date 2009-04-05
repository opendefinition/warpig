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
		self.StyleSetFont( 0, font )
		
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
		self.SetLexer( wx.stc.STC_LEX_PYTHON )
	
		keys = keyword.kwlist[ : ]
		keys.append( "zzzzzz?2" )
		keys.append( "aaaaa?2" )
		keys.append( "__init__?3" )
		keys.append( "zzaaaaa?2" )
		keys.append( "zzbaaaa?2" )
		keys.append( "this_is_a_longer_value" )
		
		#== Setup lexer styles ==#
		
		# Global default styles for all languages
		self.StyleClearAll()  # Reset all to be like the default
		
		# Global default styles for all languages
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACELIGHT, "fore: #FFFFFF, back: #0000FF, bold" )
		self.StyleSetSpec( wx.stc.STC_STYLE_BRACEBAD, "fore: #000000, back: #FF0000, bold" )
		
		#== Python styles ==#
		
		# Default
		self.StyleSetSpec( wx.stc.STC_P_DEFAULT, "fore:#000000" )
	
		# Comments
		self.StyleSetSpec( wx.stc.STC_P_COMMENTLINE, "fore: #99CC00, bold" )
		
		# Number
		self.StyleSetSpec( wx.stc.STC_P_NUMBER, "fore:#007F7F" )
		
		# String
		self.StyleSetSpec( wx.stc.STC_P_STRING, "fore:#7F007F" )
		
		# Single quoted string
		self.StyleSetSpec( wx.stc.STC_P_CHARACTER, "fore:#7F007F" )  
		
		# Keyword
		self.StyleSetSpec( wx.stc.STC_P_WORD, "fore: #99CC00, bold" )
		
		# Triple quotes
		self.StyleSetSpec( wx.stc.STC_P_TRIPLE, "fore:#99CC00" ) 
		
		# Triple double quotes
		self.StyleSetSpec( wx.stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000" )
		
		# Class name definition
		self.StyleSetSpec( wx.stc.STC_P_CLASSNAME, "fore:#336699,bold" )
		
		# Function or method name definition
		self.StyleSetSpec( wx.stc.STC_P_DEFNAME, "fore:#007F7F,bold" )
		
		# Operators
		self.StyleSetSpec( wx.stc.STC_P_OPERATOR, "bold" )
		
		# Identifiers
		self.StyleSetSpec( wx.stc.STC_P_IDENTIFIER, "fore:#000000" )
		
		# Comment-blocks
		self.StyleSetSpec( wx.stc.STC_P_COMMENTBLOCK, "fore: #99CC00, bold" )
		
		# End of line where string is not closed
		self.StyleSetSpec( wx.stc.STC_P_STRINGEOL, "fore:#000000" )
		
		self.SetCaretForeground( 'BLACK' )
		self.SetKeyWords( 0, " ".join( keyword.kwlist ) )