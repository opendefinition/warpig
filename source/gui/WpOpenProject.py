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
from gui.guid.guid import *


# Interprocess communications
from wx.lib.pubsub import Publisher as pub


class WpOpenProject( wx.Dialog ):
    def __init__(self):
        wx.Dialog.__init__(self, None, CONST_WIDGET_PROJECT_OPEN, 'Open Project', size=(500, 300))
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
        panel = wx.Panel(self, CONST_WIDGET_PROJECT_PANEL)
        panelsizer = wx.BoxSizer(wx.VERTICAL)

        self.projectlist = wx.ListCtrl(
                                panel, CONST_WIDGET_PROJECT_LIST,
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
        panel = wx.Panel(self, CONST_WIDGET_PROJECT_LIST_PANEL)
        panelsizer = wx.BoxSizer(wx.HORIZONTAL)

        openbutton = buttons.ThemedGenButton(panel, CONST_WIDGET_PROJECT_BUTTON_OPEN, 'Open')
        cancelbutton = buttons.ThemedGenButton(panel, CONST_WIDGET_PROJECT_BUTTON_CANCEL, 'Cancel')
        deletebutton = buttons.ThemedGenButton(panel, CONST_WIDGET_PROJECT_BUTTON_DELETE, 'Delete')

        panelsizer.Add(deletebutton, 0, wx.RIGHT, 2)
        panelsizer.Add(cancelbutton)
        panelsizer.Add(openbutton, 1, wx.EXPAND | wx.RIGHT, 2)

        panel.SetSizer(panelsizer)

        self.Bind(wx.EVT_BUTTON, self.onOpen, id=CONST_WIDGET_PROJECT_BUTTON_OPEN)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=CONST_WIDGET_PROJECT_BUTTON_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.onDelete, id=CONST_WIDGET_PROJECT_BUTTON_DELETE)

        return panel

    ##----------------------------------------------------------------------
    ## Bindings
    ##----------------------------------------------------------------------

    def onOpen(self, event):
        projectid = self.__getItemDataForSelectedElement()

        if projectid != None:
            db = WpDatabaseAPI()
            project = db.GetProject(projectid)

            # Open tab
            pub.sendMessage('notebook.opensavedtabs', projectid)

            # Populate the tree
            pub.sendMessage('projecttree.populate', project)

            self.Destroy()

    def onCancel(self, event):
        self.Destroy()

    def onDelete(self, event):
        projectid = self.__getItemDataForSelectedElement()

        if projectid != None:
            db = WpDatabaseAPI()
            db.DeleteProject(projectid)

            self.projectlist.DeleteItem(self.__getSelectedItem())


    def __getItemDataForSelectedElement(self):
        """
        Get itemdata for current selected project
        Return None if none selected
        """
        try:
            data = int(self.projectlist.GetItemData(self.projectlist.GetFirstSelected()))
            return data
        except:
            return None

    def __getSelectedItem(self):
        """
        Get selected project
        """
        return self.projectlist.GetFirstSelected()
