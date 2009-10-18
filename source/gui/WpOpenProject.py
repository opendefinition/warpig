# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpNewProject
# Desc: Class for handling operations regarding a project
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx
import wx.lib.buttons as buttons

from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpProject import WpProject

class WpOpenProject( wx.Dialog ):
	def __init__(self, treectrl):
            self._treectrl = treectrl
            wx.Dialog.__init__( self, None, wx.ID_ANY, 'Open Project', size=(500, 300) )
            self.Center()
            self.Setup()
                
        def Setup(self):
            mainsizer = wx.FlexGridSizer(2,1, vgap=5, hgap=5)
            mainsizer.AddMany(
                [
                    (self.ProjectList(), 1, wx.EXPAND),
                    (self.Buttons(), 1, wx.EXPAND)
                ]
            )

            mainsizer.AddGrowableRow( 0 )
            mainsizer.AddGrowableCol( 0 )

            self.SetSizer(mainsizer, wx.EXPAND)

        def ProjectList(self):
            panel = wx.Panel(self, wx.ID_ANY)
            panelsizer = wx.BoxSizer(wx.VERTICAL)
            
            self.projectlist = wx.ListCtrl(
                                    panel, wx.ID_ANY,
                                    style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_VRULES | wx.LC_HRULES
                                )

            self.projectlist.InsertColumn(0, 'Project')
            self.projectlist.SetColumnWidth(0, 1000)
            
            panelsizer.Add(self.projectlist, 1, wx.EXPAND)
            panel.SetSizer(panelsizer, wx.EXPAND)

            return panel
            

        def Buttons(self):
            panel = wx.Panel(self, wx.ID_ANY)
            panelsizer = wx.BoxSizer(wx.HORIZONTAL)

            savebutton = wx.Button(panel, wx.ID_SAVE)
            cancelbutton = wx.Button(panel, wx.ID_CANCEL)

            panelsizer.Add(savebutton)
            panelsizer.Add(cancelbutton)

            panel.SetSizer(panelsizer)

            return panel
