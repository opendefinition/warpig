# -*- coding: utf-8 -*-

#
# EXPERIMENTAL: DO NOT USE!
#

import wx
import wx.stc as stc
import keyword

class wpTextEditor( wx.Frame ):
    def __init__( self ):
        None
        
    def createTextEditor( self, parent, filePath=None ):
        self.textEditor = stc.StyledTextCtrl ( parent, 1337, style=wx.TE_MULTILINE )
        
        self.textEditor.SetMarginType( 0, stc.STC_MARGIN_NUMBER )  # Line numbering!
        self.textEditor.SetMarginWidth( 0, 35 ) # Margin for line numbering
        # textEditor.StyleSetBackground( 0, 'blue' )
        # textEditor.StyleSetForeground( 0, 'yellow' )
        font = wx.Font( 12, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.BOLD )
        self.textEditor.StyleSetFont( 0, font ) 
        
        # Adding content
        if filePath is not None:
            self.textEditor.LoadFile( filePath )

        # Experimental Lexer support
        self.setLexer()
        
        return self.textEditor
    
    def setLexer( self ):
        self.textEditor.SetLexer( stc.STC_LEX_PYTHON )
        
        keys = keyword.kwlist[ : ]
        keys.append("zzzzzz?2")
        keys.append("aaaaa?2")
        keys.append("__init__?3")
        keys.append("zzaaaaa?2")
        keys.append("zzbaaaa?2")
        keys.append("this_is_a_longer_value")

        # Setup lexer styles
        '''
        faces = { 'times': '',
              'mono' : '',
              'helv' : '',
              'other': '',
              'size' : '',
              'size2': '',
             }
        '''
        # Global default styles for all languages
        # self.textEditor.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        self.textEditor.StyleClearAll()  # Reset all to be like the default
        
        # Global default styles for all languages
        # self.textEditor.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        # self.textEditor.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        # self.textEditor.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        self.textEditor.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        self.textEditor.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default 
        self.textEditor.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000")
        # Comments
        self.textEditor.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore: #99cc00, bold" )
        # Number
        self.textEditor.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F")
        # String
        self.textEditor.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F")
        # Single quoted string
        self.textEditor.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F")
        # Keyword
        self.textEditor.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold")
        # Triple quotes
        self.textEditor.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000")
        # Triple double quotes
        self.textEditor.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000")
        # Class name definition
        self.textEditor.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#336699,bold")
        # Function or method name definition
        self.textEditor.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold")
        # Operators
        self.textEditor.StyleSetSpec(stc.STC_P_OPERATOR, "bold")
        # Identifiers
        self.textEditor.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000")
        # Comment-blocks
        self.textEditor.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore: #C0C0C0, bold")
        # End of line where string is not closed
        self.textEditor.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000")

        self.textEditor.SetCaretForeground( 'BLACK' )
        
        #####
        self.textEditor.SetKeyWords( 0, " ".join( keyword.kwlist ) )

        
'''
        import  keyword
        ### @note: Experimental lexer support
        # textEditor.SetLexer(stc.STC_LEX_PYTHON)
        # textEditor.SetKeyWords(0, " ".join(keyword.kwlist))
        ### 
        textEditor.SetLexer( stc.STC_LEX_PYTHON )
        kw = keyword.kwlist[:]
        kw.append("zzzzzz?2")
        kw.append("aaaaa?2")
        kw.append("__init__?3")
        kw.append("zzaaaaa?2")
        kw.append("zzbaaaa?2")
        kw.append("this_is_a_longer_value")
        # Make some styles,  The lexer defines what each style is used for, we
        # just have to define what each style looks like.  This set is adapted from
        # Scintilla sample property files.
        faces = { 'times': 'Times',
              'mono' : 'Courier',
              'helv' : 'Helvetica',
              'other': 'new century schoolbook',
              'size' : 12,
              'size2': 10,
             }
        # Global default styles for all languages
        textEditor.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        textEditor.StyleClearAll()  # Reset all to be like the default

        # Global default styles for all languages
        textEditor.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        textEditor.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        textEditor.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        textEditor.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        textEditor.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default 
        textEditor.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comments
        textEditor.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        # Number
        textEditor.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # String
        textEditor.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Single quoted string
        textEditor.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Keyword
        textEditor.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        # Triple quotes
        textEditor.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        # Triple double quotes
        textEditor.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        # Class name definition
        textEditor.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        # Function or method name definition
        textEditor.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Operators
        textEditor.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        # Identifiers
        textEditor.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comment-blocks
        textEditor.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        # End of line where string is not closed
        textEditor.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)

        textEditor.SetCaretForeground("BLUE")
        
        #####
        textEditor.SetKeyWords( 0, " ".join( keyword.kwlist ) )

'''