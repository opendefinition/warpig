# -*- coding: utf-8 -*-

import wx
import wx.stc as stc

class wpFrame( wx.Frame ):
    def __init__( self, *args, **kwargs ):
        wx.Frame.__init__( self, *args, **kwargs )
        self.setup_widgets()
        
        self.Maximize()
        
    def setup_widgets( self ):
        """Called when the controls on Window are to be created"""
        
        # Sizers
        self.createHorizontalSizer()
        self.createVerticalSizer()
        
        # Toolbar
        toolBar = self.createToolBar()
        
        # Menubar
        menuBar = self.createMenuBar()
        self.SetMenuBar( menuBar )
        
        # Text Editor
        textEditor = self.createTextEditor()

        # Statusbar
        statusBar = self.createStatusBar()

        self.h_sizer.Add( toolBar, 0 ) 
        self.h_sizer.Add( textEditor, 1 )  
        self.h_sizer.Add( statusBar, 2 )    
                   
        self.v_sizer.Add(self.h_sizer, 0, wx.EXPAND)
        
    def createHorizontalSizer( self ):
        '''
        Create Horsizontal Sizer
        '''
        self.h_sizer = wx.BoxSizer( wx.HORIZONTAL )
        
    def createVerticalSizer( self ):
        '''
        Create Vertical Sizer
        '''
        self.v_sizer = wx.BoxSizer( wx.VERTICAL ) 

    def createToolBar( self ):
        '''
        Create Toolbar
        @return: object toolbar
        '''
        toolBar = self.CreateToolBar()
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/document-new.png' ) )
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/media-floppy.png' ) )
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/folder.png' ) )
        toolBar.Realize()  
        
        return toolBar
    
    def createMenuBar( self ):
        '''
        Create Menubar
        @return: object menubarr
        '''
        menuBar = wx.MenuBar(wx.MB_DOCKABLE)
        file = wx.Menu()
        edit = wx.Menu()
        view = wx.Menu()
        tool = wx.Menu()
        help = wx.Menu()

        menuBar.Append(file, '&File')
        menuBar.Append(edit, '&Edit')
        menuBar.Append(view, '&View')
        menuBar.Append(tool, '&Tools')
        menuBar.Append(help, '&Help')
               
        return menuBar
        
    def createTextEditor( self ):
        '''
        Create TextEditor
        @return: object styledtextctrl
        '''
        textEditor = stc.StyledTextCtrl ( self, -1, style=wx.TE_MULTILINE )
        
        ### @note: Experimental lexer support
        # textEditor.SetLexer(stc.STC_LEX_PYTHON)
        # textEditor.SetKeyWords(0, " ".join(keyword.kwlist))
        ### 
        
        textEditor.SetMarginType( 0, stc.STC_MARGIN_NUMBER )  # Line numbering!
        textEditor.SetMarginWidth( 0, 35 )
        textEditor.StyleSetBackground( 0, 'blue' )
        textEditor.StyleSetForeground( 0, 'yellow' )
        font = wx.Font( 12, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.BOLD )
        textEditor.StyleSetFont( 0, font ) 
        
        return textEditor
    
    def createStatusBar( self ):
        '''
        Create Statusbar
        
        @return: object statusbar
        '''
        statusBar = self.CreateStatusBar()
        
        return statusBar