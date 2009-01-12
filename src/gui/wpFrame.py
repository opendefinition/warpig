# -*- coding: utf-8 -*-

import wx

class wpFrame( wx.Frame ):
    def __init__( self, *args, **kwargs ):
        wx.Frame.__init__( self, *args, **kwargs )
        self.create_controls()
        
    def create_controls( self ):
        pass