# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpProjectsSettings
# Desc:
# 	GUI dialog for managing projects settings
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx
from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpConfigSystem import WpConfigSystem

class WpProjectsSettings(wx.Panel):
    def __init__( self, parent, *args, **kwargs ):
        wx.Panel.__init__( self, parent, *args, **kwargs )
        self.configobj = WpConfigSystem()
        self.Setup()
        None

    def Setup( self ):
        self.mainSizer = wx.FlexGridSizer(rows=2, cols=1, vgap=5, hgap=5)
        self.saveBt = wx.Button( self, wx.ID_ANY, 'Save' )
        self.mainSizer.AddSpacer(5)

        ## Box sizer
        boxsizer = wx.BoxSizer(wx.VERTICAL)

        ## Prefix
        prefixlabel = wx.StaticText(self, wx.ID_ANY, "Prefix")
        self.prefixBox = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE, size=(300,50))

        ## Suffix
        suffixlabel = wx.StaticText(self, wx.ID_ANY, "Suffix")
        self.suffixBox = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE, size=(300,50))

        ## Populating data
        self.suffixBox.SetValue(self.configobj.settings['projecttree-suffixexclude'])
        self.prefixBox.SetValue(self.configobj.settings['projecttree-prefixexclude'])

        boxsizer.Add(prefixlabel)
        boxsizer.Add(self.prefixBox)
        boxsizer.Add(suffixlabel)
        boxsizer.Add(self.suffixBox)

        self.mainSizer.AddMany(
                [
                    (boxsizer, 1, wx.EXPAND),
                    (self.saveBt)
                ]
        )

        self.mainSizer.AddGrowableRow(1)
        self.mainSizer.AddGrowableRow(2)

        self.SetSizer(self.mainSizer, wx.EXPAND)

        ## Bind Savebutton
        self.Bind(wx.EVT_BUTTON, self.OnSave, id=self.saveBt.GetId())

    def OnSave(self, event):
        db = WpDatabaseAPI()
        self.configobj.settings['projecttree-prefixexclude'] = self.prefixBox.GetValue()
        self.configobj.settings['projecttree-suffixexclude'] = self.suffixBox.GetValue()
        db.AddRegisterSetting( 'prefixexclude', self.configobj.settings['projecttree-prefixexclude'], 'projecttree' )
        db.AddRegisterSetting( 'suffixexclude', self.configobj.settings['projecttree-suffixexclude'], 'projecttree' )