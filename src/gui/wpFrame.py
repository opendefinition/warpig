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
        self.h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #Vertical sizer
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.textEditor = stc.StyledTextCtrl ( self, -1, style=wx.TE_MULTILINE )
        self.textEditor.SetMarginLeft( 10 )
        self.textEditor.SetLexerLanguage( 'python' )
        
        
        self.h_sizer.Add( self.textEditor, 0)
        
        self.v_sizer.Add(self.h_sizer, 0, wx.EXPAND)
        
        '''
        #Widget Creation
        #Create the static text widget and set the text
        self.text = wx.StaticText(self, label="Enter some text:")
        #Create the Edit Field (or TextCtrl)
        self.edit = wx.TextCtrl(self, size=wx.Size(250, -1))
        #Create the button
        self.button = wx.Button(self, label="Press me!")
    
        #Add to horizontal sizer
        #add the static text to the sizer, tell it not to resize
        self.h_sizer.Add(self.text, 0,)
        #Add 5 pixels between the static text and the edit
        self.h_sizer.AddSpacer((5,0))
        #Add Edit
        self.h_sizer.Add(self.edit, 1)
    
        #Add to the vertical sizer to create two rows
        self.v_sizer.Add(self.h_sizer, 0, wx.EXPAND)
        #Add button underneath
        self.v_sizer.Add(self.button, 0)
    
        #Set the sizer
        self.SetSizer(self.v_sizer)
        '''