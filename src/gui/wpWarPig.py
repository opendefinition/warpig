# -*- coding: utf-8 -*-
import wx

from gui.wpFrame import wpFrame

class wpWarPig( wx.App ):
    """The wx.App for the wxHello application"""

    def OnInit(self):
        """Override OnInit to create our Frame"""
        frame = wpFrame( None, title='Something' )
        frame.Center()
        frame.Show()
        self.SetTopWindow(frame)

        return True