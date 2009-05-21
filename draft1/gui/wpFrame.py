# -*- coding: utf-8 -*-

import wx
import wx.stc as stc
from gui.wpNotebook import wpNoteBook

class wpFrame( wx.Frame ):
    _notebook = None
    
    def __init__( self, *args, **kwargs ):
        wx.Frame.__init__( self, *args, **kwargs )
        self.setup_widgets()
        
        # Bindings 
        self.Bind( wx.EVT_MENU, self.onNew, id=101 )  
        self.Bind( wx.EVT_MENU, self.onOpen, id=102 )
        self.Bind( wx.EVT_MENU, self.onExit, id=105 )
        self.Bind( wx.EVT_MENU, self.onAbout, id=501 )
        self.Bind( wx.EVT_MENU, self.onSave, id=103)    
                
    def setup_widgets( self ):
        """
        Called when the controls on Window are to be created
        """    
        self._notebook = wpNoteBook().createNoteBook( self )
        mainSizer = self.createVerticalSizer()
        gridSizer = self.createFlexGridSizer( 3, 1, 0, 0 )
        
        # Menubar
        self.SetMenuBar( self.createMenuBar() )
    
        # Adding widgets to gridsizer
        gridSizer.AddMany( [
                            ( self.createToolBar(), 0, wx.EXPAND ),
                            ( self._notebook._notebook , 0, wx.EXPAND ),
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
        toolBar.AddLabelTool( 101, '', wx.Bitmap( './system/icons/document-new.png' ) )
        toolBar.AddLabelTool( 103, '', wx.Bitmap( './system/icons/media-floppy.png' ) )
        toolBar.AddLabelTool( 102, '', wx.Bitmap( './system/icons/folder.png' ) )
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
        
        # File menu setup
        fileNew = wx.MenuItem( file , 101, '&New', 'Create new file' )
        fileOpen = wx.MenuItem( file, 102, '&Open', 'Open file' )
        fileSave = wx.MenuItem( file, 103, '&Save', 'Save file' )
        fileSaveAs = wx.MenuItem( file, 104, '&Save as', 'Save file as'  )
        appQuit = wx.MenuItem( file, 105, '&Quit', 'Quit WarPig' )
        
        file.AppendItem( fileNew )
        file.AppendItem( fileOpen )
        file.AppendSeparator()
        file.AppendItem( fileSave )
        file.AppendItem( fileSaveAs )
        file.AppendSeparator()
        file.AppendItem( appQuit )
        
        # Help menu setup
        helpAbout = wx.MenuItem( help, 501, '&About', 'About WarPig'  )
        help.AppendItem( helpAbout )
                
        
        return menuBar
    
    def onExit( self, event ):
        self.Close()
        
    def onNew( self, event ):
        self._notebook.addPage()
        
    def onOpen( self, event ):
        # Create an open file dialog
        dialog = wx.FileDialog ( None, style = wx.OPEN )

        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self._notebook.addPage( dialog.GetPath() )
        
        dialog.Destroy()
    
    
    def createStatusBar( self ):
        '''
        Create Statusbar    
        @return: object statusbar
        '''
        statusBar = self.CreateStatusBar()
        
        return statusBar
    
    def onAbout( self, event ):
        description = """
            WarPig is a simple but yet useful code editor written in Python.
        """


        information = wx.AboutDialogInfo()
        # information.SetIcon(wx.Icon('something', wx.BITMAP_TYPE_PNG))
        information.SetName( 'WarPig Code Editor' )
        information.SetVersion( '0.01' )
        information.SetDescription( description )
        information.SetCopyright('(C) 2009 Open Definition' )
        information.SetWebSite( 'http://www.opendefinition.com' )
        information.AddDeveloper( 'Roger Johnsen' )

        wx.AboutBox( information )
        
    def onSave( self, event ):
        print "Hello"

        
    