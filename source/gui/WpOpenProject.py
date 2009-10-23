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
                    (self.ProjectList(), 1, wx.EXPAND | wx.ALL, 5),
                    (self.Buttons(), 1, wx.EXPAND | wx.ALL, 15)
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
                                    style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER
                                )

            self.projectlist.InsertColumn(0, 'Project')
            self.projectlist.SetColumnWidth(0, 1000)

            ## Populate the list
            for project in self.__GetProjectList():
                item = wx.ListItem()
                item.SetText(project['title'])
                item.SetData(project['id'])

                self.projectlist.InsertItem(item)

            panelsizer.Add(self.projectlist, 1, wx.EXPAND)
            panel.SetSizer(panelsizer, wx.EXPAND)

            return panel

        def __GetProjectList(self):
            db = WpDatabaseAPI()
            return db.GetProjectList()
            

        def Buttons(self):
            panel = wx.Panel(self, wx.ID_ANY)
            panelsizer = wx.BoxSizer(wx.HORIZONTAL)

            openbutton = buttons.ThemedGenButton(panel, wx.ID_OPEN, 'Open')
            cancelbutton = buttons.ThemedGenButton(panel, wx.ID_CANCEL, 'Cancel')
            deletebutton = buttons.ThemedGenButton(panel, wx.ID_DELETE, 'Delete')

            panelsizer.Add(openbutton)
            panelsizer.Add(deletebutton)
            panelsizer.Add(cancelbutton)

            panel.SetSizer(panelsizer)

            self.Bind(wx.EVT_BUTTON, self.onOpen, id=openbutton.GetId())
            self.Bind(wx.EVT_BUTTON, self.onCancel, id=cancelbutton.GetId())
            self.Bind(wx.EVT_BUTTON, self.onDelete, id=deletebutton.GetId())

            return panel

        ##----------------------------------------------------------------------
        ## Bindings
        ##----------------------------------------------------------------------

        def onOpen(self, event):
            projectid = int(self.projectlist.GetItemData(self.projectlist.GetFirstSelected()))

            db = WpDatabaseAPI()
            project = db.GetProject(projectid)

            # Populate the tree
            self._treectrl.treectrl.PopulateTree(project)
            self.Destroy()

        def onCancel(self, event):
            self.Destroy()

        def onDelete(self, event):
            projectid = int(self.projectlist.GetItemData(self.projectlist.GetFirstSelected()))

            db = WpDatabaseAPI()
            db.DeleteProject(projectid)
            self.Destroy()
