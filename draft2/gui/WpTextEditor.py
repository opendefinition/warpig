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
import re 
import wx
import wx.stc as stc

from system.WpFileSystem import WpFileSystem
from system.WpConfigSystem import WpConfigSystem

class WpTextEditor( wx.stc.StyledTextCtrl ):
	_curr_file_path = None

        def applySettings(self):
            """
            Apply editor settings
            """
            self.editorFontFace         = self.configobj.settings['editor-fontface']
            self.editorFontSize         = int(self.configobj.settings['editor-fontsize'])
            self.editorTextMarginWidth  = int(self.configobj.settings['editor-textmargin'])
            self.editorTabSize          = int(self.configobj.settings['editor-tabsize'])
            self.editorUseTab           = int(self.configobj.settings['editor-usetab'])
            self.editorCodeFold         = int(self.configobj.settings['editor-foldcode'])
            self.editorCodeFoldStyle    = int(self.configobj.settings['editor-foldcodestyle'])

        def setTabAndIndents(self):
            """
            Setup tabulator handling
            """
            if self.editorUseTab == True:
                self.SetBackSpaceUnIndents(True)
                self.SetTabIndents(True)
                self.SetUseTabs(True)
            else:
                self.SetBackSpaceUnIndents(True)
                self.SetIndent(self.editorTabSize)		
                self.SetTabIndents(False)
                self.SetTabWidth(self.editorTabSize)
                self.SetUseTabs(False)

        def setCodeFolding(self):
                """
                Setup code folding
                """
                if self.editorCodeFold == True:
                    self.fold_symbols = self.editorCodeFoldStyle
                    self.SetProperty("fold", "1") ## What is this???
                    self.SetMarginType(2, stc.STC_MARGIN_SYMBOL)
                    self.SetMarginMask(2, stc.STC_MASK_FOLDERS)

                    self.SetMarginSensitive(2, True)
                    self.SetMarginWidth(2, 12)
                    self.SetFoldMarginHiColour(True, "#232323")
                    self.SetFoldMarginColour(True, "#232323")


                    if self.fold_symbols == 0:
                        # Arrow pointing right for contracted folders, arrow pointing down for expanded
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_ARROWDOWN,    "black", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_ARROW,        "black", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY,        "black", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY,        "black", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY,        "white", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY,        "white", "black" )
                        self.MarkerDefine( stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY,        "white", "black" )
                    elif self.fold_symbols == 1:
                        # Plus for contracted folders, minus for expanded
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_MINUS, "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_PLUS,  "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY, "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY, "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY, "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY, "white", "black")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY, "white", "black")

                    elif self.fold_symbols == 2:
                        # Like a flattened tree control using circular headers and curved joins
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_CIRCLEMINUS,          "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_CIRCLEPLUS,           "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,                "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNERCURVE,         "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_CIRCLEPLUSCONNECTED,  "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_CIRCLEMINUSCONNECTED, "white", "#404040")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNERCURVE,         "white", "#404040")

                    elif self.fold_symbols == 3:
                        # Like a flattened tree control using square headers
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS,          "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,           "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,             "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,           "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "#808080")
                        self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,           "white", "#808080")

                    self.Bind(stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
                    self.Bind(stc.EVT_STC_MARGINCLICK, self.OnMarginClick)
        
        def OnUpdateUI(self, evt):
            # check for matching braces
            braceAtCaret = -1
            braceOpposite = -1
            charBefore = None
            caretPos = self.GetCurrentPos()

            if caretPos > 0:
                charBefore = self.GetCharAt(caretPos - 1)
                styleBefore = self.GetStyleAt(caretPos - 1)

            # check before
            if charBefore and chr(charBefore) in "[]{}()" and styleBefore == stc.STC_P_OPERATOR:
                braceAtCaret = caretPos - 1

            # check after
            if braceAtCaret < 0:
                charAfter = self.GetCharAt(caretPos)
                styleAfter = self.GetStyleAt(caretPos)

                if charAfter and chr(charAfter) in "[]{}()" and styleAfter == stc.STC_P_OPERATOR:
                    braceAtCaret = caretPos

            if braceAtCaret >= 0:
                braceOpposite = self.BraceMatch(braceAtCaret)

            if braceAtCaret != -1  and braceOpposite == -1:
                self.BraceBadLight(braceAtCaret)
            else:
                self.BraceHighlight(braceAtCaret, braceOpposite)
                #pt = self.PointFromPosition(braceOpposite)
                #self.Refresh(True, wxRect(pt.x, pt.y, 5,5))
                #print pt
                #self.Refresh(False)


        def OnMarginClick(self, evt):
            # fold and unfold as needed
            if evt.GetMargin() == 2:
                if evt.GetShift() and evt.GetControl():
                    self.FoldAll()
                else:
                    lineClicked = self.LineFromPosition(evt.GetPosition())

                    if self.GetFoldLevel(lineClicked) & stc.STC_FOLDLEVELHEADERFLAG:
                        if evt.GetShift():
                            self.SetFoldExpanded(lineClicked, True)
                            self.Expand(lineClicked, True, True, 1)
                        elif evt.GetControl():
                            if self.GetFoldExpanded(lineClicked):
                                self.SetFoldExpanded(lineClicked, False)
                                self.Expand(lineClicked, False, True, 0)
                            else:
                                self.SetFoldExpanded(lineClicked, True)
                                self.Expand(lineClicked, True, True, 100)
                        else:
                            self.ToggleFold(lineClicked)


        def FoldAll(self):
            lineCount = self.GetLineCount()
            expanding = True

            # find out if we are folding or unfolding
            for lineNum in range(lineCount):
                if self.GetFoldLevel(lineNum) & stc.STC_FOLDLEVELHEADERFLAG:
                    expanding = not self.GetFoldExpanded(lineNum)
                    break

            lineNum = 0

            while lineNum < lineCount:
                level = self.GetFoldLevel(lineNum)
                if level & stc.STC_FOLDLEVELHEADERFLAG and \
                   (level & stc.STC_FOLDLEVELNUMBERMASK) == stc.STC_FOLDLEVELBASE:

                    if expanding:
                        self.SetFoldExpanded(lineNum, True)
                        lineNum = self.Expand(lineNum, True)
                        lineNum = lineNum - 1
                    else:
                        lastChild = self.GetLastChild(lineNum, -1)
                        self.SetFoldExpanded(lineNum, False)

                        if lastChild > lineNum:
                            self.HideLines(lineNum+1, lastChild)

                lineNum = lineNum + 1



        def Expand(self, line, doExpand, force=False, visLevels=0, level=-1):
            lastChild = self.GetLastChild(line, level)
            line = line + 1

            while line <= lastChild:
                if force:
                    if visLevels > 0:
                        self.ShowLines(line, line)
                    else:
                        self.HideLines(line, line)
                else:
                    if doExpand:
                        self.ShowLines(line, line)

                if level == -1:
                    level = self.GetFoldLevel(line)

                if level & stc.STC_FOLDLEVELHEADERFLAG:
                    if force:
                        if visLevels > 1:
                            self.SetFoldExpanded(line, True)
                        else:
                            self.SetFoldExpanded(line, False)

                        line = self.Expand(line, doExpand, force, visLevels-1)

                    else:
                        if doExpand and self.GetFoldExpanded(line):
                            line = self.Expand(line, True, force, visLevels-1)
                        else:
                            line = self.Expand(line, False, force, visLevels-1)
                else:
                    line = line + 1

            return line



	def __init__( self, parent ):
		self.parent = parent

                ## Load configurations
                self.configobj = WpConfigSystem()
                self.applySettings()
		
		##
		# We always construct parent with wx.TE_MULTILINE
		##
		wx.stc.StyledTextCtrl.__init__( self, parent, style=wx.TE_MULTILINE )
		## Text margin
		self.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER )    # Line numbering
		self.SetMarginWidth(0, 35)                          # Margin for line numbering
		self.SetEdgeColour("#555753" )
		self.SetEdgeColumn(self.editorTextMarginWidth)      # Text margin
		self.SetEdgeMode(wx.stc.STC_EDGE_LINE)              # Text margin type
		
		## Tab Setup
		self.setTabAndIndents()
		## Code folding
                self.setCodeFolding()


		## Fonts	
		font = wx.Font(
                            self.editorFontSize,
                            wx.DEFAULT,
                            wx.NORMAL,
                            wx.NORMAL,
                            False,
                            self.editorFontFace,
                            wx.FONTENCODING_UTF8
                        )
	
		## We must tell StyleSetSpec to use this face and size otherwise it won't get applied
		self.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,"face:%s,size:%d" % (self.editorFontFace, self.editorFontSize))
		
		self.StyleSetFont( 0, font )
		self.SetDefaultLexer()
		self.SetFocus()
		
		self.Bind( wx.EVT_KEY_DOWN, self._OnKeyDown )
		# self.Bind( wx.stc.EVT_STC_SAVEPOINTREACHED, self._OnSavePointReached )
		# self.Bind( wx.stc.EVT_STC_CHANGE, self._OnTextChange )
		
		
	#---------------------------------------------------------------
	# Get filepath defined for this instance of WpTextEditor
	# @return self
	#---------------------------------------------------------------
	def GetFilePath( self ):
		return self._curr_file_path
	
	#---------------------------------------------------------------
	# Set filepath defined for this instance of WpTextEditor and 
	# load content
	# @return self
	#---------------------------------------------------------------	
	def SetFilePath( self, filepath ):
		self._curr_file_path = filepath
		
		self.SetTextUTF8(
				WpFileSystem.ReadFromFile( self._curr_file_path )
			)
		
		##
		# Make sure we always empty the undo before we add pages
		##
		self.EmptyUndoBuffer()
		
		return self
		
	#---------------------------------------------------------------
	# Set filepath defined for this instance of WpTextEditor without 
	# loading content
	# @return self
	#---------------------------------------------------------------
	def SetFilePathNoRead( self, filepath ):
		self._curr_file_path = filepath
		
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
		
		## Python styles
		
		##
		# Default
		##
		self.StyleSetSpec( wx.stc.STC_P_DEFAULT, "fore:#ffffff,back:#232323" )
	
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
	
	#---------------------------------------------------------------
	# Handle events
	#---------------------------------------------------------------
	
	#---------------------------------------------------------------
	# Add ' * ' to tab title if text is modified
	#---------------------------------------------------------------
	def _OnTextChange( self, event ):
		tabheading = self.Parent.GetPageText( self.Parent.GetSelection() )
		dirtyfilter = re.compile( ' \* ' )
		
		if( dirtyfilter.search( tabheading ) == None ):
			tabheading += ( ' * ' )
			self.Parent.SetPageText( self.Parent.GetSelection(), tabheading )
		
	#---------------------------------------------------------------
	# Resetting title of tab
	#---------------------------------------------------------------
	def _OnSavePointReached( self, event ):
		tabheading = self.Parent.GetPageText( self.Parent.GetSelection() )
		
		if( tabheading.endswith( ' * ' ) == True ):
			self.Parent.SetPageText( self.Parent.GetSelection(), tabheading[:-3] )

	#---------------------------------------------------------------
	# Handle key events
	#---------------------------------------------------------------
	def _OnKeyDown( self, event ):
		## print "Key #", event.GetUniChar(), " CmdDown is ", event.CmdDown()
		key = event.GetUniChar()
		cmd = event.CmdDown()
		
		if( cmd == True ):
			##
			# Saving current file
			##
			if( key == 83 or key == 115 ):
				self.SaveFile()
				return
				
			##
			# Add new page with editor to current notebook instance
			##
			if( key == 78 or key == 110 ):
				self.parent.AddDefaultPage()
				return
				
			##
			# Open file
			## 
			if( key == 79 or key == 111 ):
				self.Parent.Parent.Parent.Parent.OpenPage() # :)
				return
				
			##
			# Close current tab where this instance of the editor resides
			##
			if( key == 87 or key == 119 ):
				##
				# If current editor is modified yield warning upon close
				##
				if( self.GetModify() == True ):	
					dialog = wx.MessageDialog( None, 
									'Are you sure to want to close this tab?', 
									'Question',
									wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION 
								)
		
					status = dialog.ShowModal()
	
					if( status != wx.ID_YES ):
						return
					
					dialog.Destroy()
				
				##
				# Continue closing
				##
				pagecount = self.Parent.GetPageCount()
			
				selected = self.Parent.GetSelection()	# Get which tab that is in focus
				
				##
				# Making sure we add a new page if we're deleting the last page
				##
				if( pagecount == 1 ):
					self.Parent.AddDefaultPage()
					selection = 0
				else:
					selection = selected-1
				
				self.Parent.DeletePage( selected )		# Delete unwanted tab	
				self.Parent.SetSelection( selection )	# Set focus to neighbour tab
				
				
				return									# Force return or else it'll segfault
			
			##
			# Closing this application
			##
			if( key == 81 or key == 113 ):
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
				self.SetFilePathNoRead( path )
				dialog.Destroy()
		
		WpFileSystem.SaveToFile( self.GetTextUTF8(), path )
		
		##
		# Setting savepoint upon save
		##
		self.SetSavePoint()
		
		##
		# Make sure the editor got the filepath set (and that it's not re-read
		##
		self.SetFilePathNoRead( path )
