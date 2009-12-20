# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpPreferences
# Desc: Class for handling preferences
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx

from gui.preferences.WpPreferenceTree import WpPreferenceTree
from gui.guid.guid import *

class WpPreferences( wx.Panel ):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(500, 500))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(WpPreferenceTree(self, CONST_PANE_PREFERENCE_TREE))
        self.SetSizer(sizer)