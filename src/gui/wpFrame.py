# -*- coding: utf-8 -*-

import wx
import wx.stc as stc
from gui.wpNotebook import wpNoteBook

class wpFrame( wx.Frame ):
    def __init__( self, *args, **kwargs ):
        wx.Frame.__init__( self, *args, **kwargs )
        self.setup_widgets()
                
    def setup_widgets( self ):
        """
        Called when the controls on Window are to be created
        """    
       
        mainSizer = self.createVerticalSizer()
        gridSizer = self.createFlexGridSizer( 3, 1, 0, 0 )
        
        # Menubar
        self.SetMenuBar( self.createMenuBar() )
        
        ### TESTING : START ###
        splitWindow = wx.SplitterWindow(self, -1, style=wx.BORDER_SUNKEN )
        splitWindow.SetMinimumPaneSize(20)
        
        leftPanel = wx.Panel( splitWindow, -1, size=(100,100) )
        leftPanel.SetBackgroundColour( wx.WHITE )
            
        tree = wx.TreeCtrl( leftPanel, size=(200,100))
        root = tree.AddRoot("Python Example")
        items = [
                 "script1.py",
                 "script2.py",
                 "script3.py",
                 "script4.py"
                 ]

        tree.AppendItem( root, items[0]  )
        tree.AppendItem( root, items[1]  )
        tree.AppendItem( root, items[2]  )
        splitWindow.SplitVertically( leftPanel, wpNoteBook().createNoteBook( splitWindow ), 200 )
        ### TESTING : END ###
        
        # Adding widgets to gridsizer
        gridSizer.AddMany( [
                            ( self.createToolBar(), 0, wx.EXPAND ),
                            ( splitWindow, 0, wx.EXPAND ),
                            #( wpNoteBook().createNoteBook( self ), 0, wx.EXPAND ),
                            #( self.createTextEditor() , 0, wx.EXPAND ),
                            ( self.createStatusBar(), 0, wx.EXPAND )
                          ] )

        # Setting main row growable
        gridSizer.AddGrowableRow(1, 1)


        mainSizer.Add( gridSizer, 1, wx.EXPAND )
        self.SetSizer( mainSizer )
        
        self.Centre()
        self.Maximize()
        self.Show(True)
        
    def createFlexGridSizer( self, rows, cols, vgap, hgap ):
        '''
        Create Flexgridsizer
        @return: object FlexGridSizer
        '''
        return wx.FlexGridSizer( rows, cols, vgap, hgap ) 
    
    def createHorizontalSizer( self ):
        '''
        Create Horsizontal Sizer
        @return:  object BoxSizer( wx.HORIZONTAL )
        '''
        return  wx.BoxSizer( wx.HORIZONTAL )
        
    def createVerticalSizer( self ):
        '''
        Create Vertical Sizer
        @return:  object  wx.BoxSizer( wx.VERTICAL ) 
        '''
        return wx.BoxSizer( wx.VERTICAL ) 

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
        menuBar = wx.MenuBar()
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
        
        textEditor.SetMarginType( 0, stc.STC_MARGIN_NUMBER )  # Line numbering!
        textEditor.SetMarginWidth( 0, 35 ) # Margin for line numbering
        # textEditor.StyleSetBackground( 0, 'blue' )
        # textEditor.StyleSetForeground( 0, 'yellow' )
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
    