# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpWarPig
# Desc: This application
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import sqlite3
import sys

try:
    import wx
except:
    print "\nCouldn't load WXWidget library. Please install WX (unicode) before running Warpig"
    sys.exit(0)

from gui.WpAuiMainFrame import WpAuiMainFrame
from system.setup import RunSetup
from system.WpConfigLoader import WpConfigLoader
from gui.Keybindings import Keybindings

class WpWarPig( wx.App ):
    """
    Main class for creating frame
    """

    def OnInit(self):
        config = self.loadConfiguration()

        if( config == False ):
            RunSetup()
            config = self.loadConfiguration()

        if( config != False ):
            ## Load keybindings
            keybinding = Keybindings(self)
            keybinding.init()

            frame = WpAuiMainFrame( None )
            frame.Show()
            self.SetTopWindow(frame)

        return True

    def loadConfiguration(self):
        try:
            configuration = WpConfigLoader()
            configuration.LoadConfig()
            result = True
        except sqlite3.OperationalError:
            result = False
        finally:
            return result
