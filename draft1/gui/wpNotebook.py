# -*- coding: utf-8 -*-
import wx
import wx.lib.flatnotebook as fnb
import wx.stc as stc

from gui.wpTextEditor import wpTextEditor

class  wpNoteBook( wx.Frame ):
    _notebook = None
    
    def __init__( self, ):
        None
        
    def createNoteBook( self, parent  ):
        self._notebook = fnb.FlatNotebook( parent, wx.ID_ANY )
        return self
        
    def addPage( self, filePath=None ):
        if filePath is None:
            title = '<empty>'
        else:
            length = len( filePath )
            start = filePath.rfind( '/' )+1
            title = filePath[start:length]
            
        self._notebook.AddPage( wpTextEditor().createTextEditor( self._notebook, filePath ),  title )
        
        
        
"""
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)

        bookStyle = fnb.FNB_NODRAG

        self.book = fnb.FlatNotebook(self, wx.ID_ANY, style=bookStyle)

        bookStyle &= ~(fnb.FNB_NODRAG)
        bookStyle |= fnb.FNB_ALLOW_FOREIGN_DND 
        self.secondBook = fnb.FlatNotebook(self, wx.ID_ANY, style=bookStyle)

        # Set right click menu to the notebook
        self.book.SetRightClickMenu(self._rmenu)

        # Set the image list 
        self.book.SetImageList(self._ImageList)
        mainSizer.Add(self.book, 6, wx.EXPAND)

        # Add spacer between the books
        spacer = wx.Panel(self, -1)
        spacer.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        mainSizer.Add(spacer, 0, wx.ALL | wx.EXPAND)

        mainSizer.Add(self.secondBook, 2, wx.EXPAND)

        # Add some pages to the second notebook
        self.Freeze()

        text = wx.TextCtrl(self.secondBook, -1, "Second Book Page 1\n", style=wx.TE_MULTILINE|wx.TE_READONLY)  
        self.secondBook.AddPage(text, "Second Book Page 1")

        text = wx.TextCtrl(self.secondBook, -1, "Second Book Page 2\n", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.secondBook.AddPage(text,  "Second Book Page 2")

        self.Thaw()    

        mainSizer.Layout()
        self.SendSizeEvent()

"""