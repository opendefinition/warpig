# -*- coding: utf-8 -*-
import wx

class wpWarPig( wx.App ):
    """The wx.App for the wxHello application"""

    def OnInit(self):
        """Override OnInit to create our Frame"""
        frame = wx.Frame( None, title='Something' )
        frame.Center()
        frame.Show()
        self.SetTopWindow(frame)

        return True