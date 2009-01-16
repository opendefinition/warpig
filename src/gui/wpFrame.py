# -*- coding: utf-8 -*-

import wx
import wx.stc as stc

class wpFrame( wx.Frame ):
    def __init__( self, *args, **kwargs ):
        wx.Frame.__init__( self, *args, **kwargs )
        self.setup_widgets()
        
    def setup_widgets( self ):
        """Called when the controls on Window are to be created"""

        #Horizontal sizer
        self.h_sizer = wx.BoxSizer( wx.HORIZONTAL )
        #Vertical sizer
        self.v_sizer = wx.BoxSizer( wx.VERTICAL )
        
        #===============================================================================================================
        # Toolbar
        #===============================================================================================================
        toolBar = self.CreateToolBar()
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/document-new.png' ) )
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/media-floppy.png' ) )
        toolBar.AddLabelTool( -1, '', wx.Bitmap( './system/icons/folder.png' ) )
        toolBar.Realize()   
        #===============================================================================================================
        # Text Editor
        #===============================================================================================================
        textEditor = stc.StyledTextCtrl ( self, -1, style=wx.TE_MULTILINE )
        
        ### @note: Experimental lexer support
        # textEditor.SetLexer(stc.STC_LEX_PYTHON)
        # textEditor.SetKeyWords(0, " ".join(keyword.kwlist))
        ### 
        
        textEditor.SetMarginType( 0, stc.STC_MARGIN_NUMBER )  # Line numbering!
        textEditor.SetMarginWidth( 0, 35 )
        #===============================================================================================================
        # Statusbar
        #===============================================================================================================
        statusBar = self.CreateStatusBar()

        self.h_sizer.Add( toolBar, 0 ) 
        self.h_sizer.Add( textEditor, 1 )  
        self.h_sizer.Add( statusBar, 2 )    
                   
        self.v_sizer.Add(self.h_sizer, 0, wx.EXPAND)