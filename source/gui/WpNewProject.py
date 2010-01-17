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

import re
import wx
import wx.lib.buttons as buttons
import os

from wx.lib.expando import ExpandoTextCtrl, EVT_ETC_LAYOUT_NEEDED

from wx.lib.agw.multidirdialog import MultiDirDialog
from system.WpFileSystem import WpFileSystem

from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpProject import WpProject

from wx.lib.pubsub import Publisher as pub

class WpNewProject( wx.Dialog ):
    def __init__( self, treectrl ):
        self._treectrl = treectrl

        wx.Dialog.__init__( self, None, 6666, 'New Project', size=(500, 300) )

        ##
        # Main Panel
        ##
        mainpanel = wx.Panel(self, -1, size=(500, 300), style=wx.EXPAND)
        mainsizer = wx.BoxSizer( wx.VERTICAL )
        panelsizer = wx.FlexGridSizer( 3, 1, 0, 0 )

        ##
        # Projectname
        ##
        prjnamesizer = wx.BoxSizer( wx.HORIZONTAL )
        prjnamelabel = wx.StaticText( mainpanel, -1, 'Name' )
        self.prjnameinput = wx.TextCtrl( mainpanel, -1 )

        prjnamesizer.Add( prjnamelabel, 0, wx.EXPAND | wx.ALL, 5 )
        prjnamesizer.Add( self.prjnameinput , 1, wx.EXPAND | wx.ALL, 5 )
        self.Fit()

        ##
        # Controls for adding files to project
        ##
        prjfilesizer =wx.BoxSizer( wx.HORIZONTAL )

        self.filelist = wx.ListCtrl( mainpanel,
                                        -1,
                                        style=wx.BORDER_SUNKEN
                                                | wx.LC_REPORT
                                                | wx.LC_VRULES
                                                | wx.LC_HRULES
                                    )

        self.filelist.InsertColumn( 0, 'Path' )
        self.filelist.SetColumnWidth( 0, 1000 )

        fileactionsizer = wx.BoxSizer( wx.VERTICAL )

        imageadd = wx.Image( "./gui/icons/list-add.png", wx.BITMAP_TYPE_PNG ).ConvertToBitmap()
        imagerem = wx.Image( "./gui/icons/list-remove.png", wx.BITMAP_TYPE_PNG ).ConvertToBitmap()

        addfilebutton = wx.BitmapButton( mainpanel,
                                            wx.ID_ANY,
                                            bitmap=imageadd,
                                            pos=(10,20),
                                            size=(imageadd.GetWidth(), imageadd.GetHeight() ),
                                            #style=wx.NO_BORDER
                                        )
        remfilebutton = wx.BitmapButton( mainpanel,
                                            wx.ID_ANY,
                                            bitmap=imagerem,
                                            pos=(10,20),
                                            size=(imagerem.GetWidth(), imagerem.GetHeight() )
                                            #style=wx.NO_BORDER
                                        )

        fileactionsizer.Add( addfilebutton, 0, wx.RIGHT | wx.TOP, 5 )
        fileactionsizer.Add( remfilebutton, 0, wx.RIGHT | wx.TOP, 5, 1 )

        prjfilesizer.Add( self.filelist, 1, wx.EXPAND | wx.ALL, 5 )
        prjfilesizer.Add( fileactionsizer )

        ##
        # Save and cancel buttons
        ##
        buttonsizer = wx.BoxSizer( wx.HORIZONTAL )

        savebutton = buttons.ThemedGenButton( mainpanel, wx.ID_ANY, 'Save' )
        cancelbutton = buttons.ThemedGenButton( mainpanel, wx.ID_ANY, 'Cancel' )

        buttonsizer.Add( cancelbutton, 0, wx.EXPAND | wx.ALL, 5 )
        buttonsizer.Add( savebutton, 1, wx.EXPAND | wx.ALL, 5 )

        ##
        # Sewing things together
        ##
        panelsizer.AddMany(
                [
                    ( prjnamesizer, 1, wx.EXPAND ),
                    #( prjdescsizer, 1, wx.EXPAND ),
                    ( prjfilesizer, 1, wx.EXPAND ),
                    ( buttonsizer, 1, wx.EXPAND )
                ]
        )

        panelsizer.AddGrowableRow( 1 )
        panelsizer.AddGrowableCol( 0 )

        ##
        # Set the main sizer to panel
        ##
        mainsizer.Add( panelsizer, 1, wx.EXPAND )

        self.SetSizer( mainsizer )

        ##
        # Bindings
        ##
        self.Bind( wx.EVT_BUTTON, self._onAssociateFiles, id=addfilebutton.GetId())
        self.Bind( wx.EVT_BUTTON, self._onRemovingFilesFromProject, id=remfilebutton.GetId())
        self.Bind( wx.EVT_BUTTON, self._onSave, id=savebutton.GetId() )
        self.Bind( wx.EVT_BUTTON, self._onCancel, id=cancelbutton.GetId() )

        self.Center()

    #---------------------------------------------------------------
    # On adding files to project
    #---------------------------------------------------------------
    def _onAssociateFiles( self, event ):
        ## Find out where base path is dependend on platform
        ## TODO: Probably change this into the users own home directories in order to
        ## avoid having to load to much information.
        opsysname = os.name

        if opsysname == 'nt':
            basepath = 'C:\\'
        elif opsysname == 'posix':
            basepath = '/'
        elif opsysname == 'mac':
            basepath = '/Users'

        dialog = wx.lib.agw.multidirdialog.MultiDirDialog( None, 'New Project', 'Associate folders', defaultPath=basepath )
        dialog.Center()
        if dialog.ShowModal() == wx.ID_OK:
            paths = dialog.GetPaths()

            count = self.filelist.GetItemCount()+1
            for path in paths:
                # If on Mac, remove "Macintosh HD"
                macfilter = re.compile( "Macintosh HD" )

                if( macfilter.search( path ) != None ):
                    path = path[12:len(path)]

                self.filelist.InsertStringItem( count, path )
                count += 1

        dialog.Destroy()

    def _onRemovingFilesFromProject( self, event ):
        pos = self.filelist.GetFirstSelected()
        tmp = []

        while pos != -1:
            tmp.append( pos )
            pos = self.filelist.GetNextSelected( pos )

        tmp.sort()
        tmp.reverse()

        for thingy in tmp:
            self.filelist.DeleteItem( thingy )

    #---------------------------------------------------------------
    # Cancel inside project dialog
    #---------------------------------------------------------------
    def _onCancel( self, event ):
        self.Close()

    #---------------------------------------------------------------
    # On saving project
    #---------------------------------------------------------------
    def _onSave( self, event ):
        self.Close()

        db = WpDatabaseAPI()
        project = WpProject()

        project.SetTitle(self.prjnameinput.GetValue())
        # project.SetDescription(self.prjdescfield.GetValue())

        numberOfPaths = self.filelist.GetItemCount()

        for index in range( 0, numberOfPaths ):
            project.AddPath(self.filelist.GetItem( index, 0 ).GetText())

        # Saving this project
        projectId = db.AddProject(project)
        project.SetId(projectId)

        # Populate projecttree
        pub.sendMessage('projecttree.populate', project)