# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpNoteBook
# Desc: Class for setting up main notebook interface
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import wx
import wx.lib.agw.aui as aui

from gui.WpTextEditor import WpTextEditor
from wx.lib.pubsub import Publisher as pub
from system.WpDatabaseAPI import WpDatabaseAPI

class WpNoteBook(aui.AuiNotebook):
    def __init__(self, parent):
        self.parent = parent
        aui.AuiNotebook.__init__(self, parent, wx.ID_ANY, style=wx.EXPAND | aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)

        ## Theme support
        arts = [
                aui.AuiDefaultTabArt,
                aui.AuiSimpleTabArt,
                aui.VC71TabArt,
                aui.FF2TabArt,
                aui.VC8TabArt,
                aui.ChromeTabArt
            ]

        art = arts[0]()
        self.SetArtProvider(art)

        self.openedtabs = { 'None': [] }

        ## Database
        self.db = WpDatabaseAPI()
        

        ## Subscribe to add page event message
        pub.subscribe(self.addPageSubscriber, 'notebook.addpage')
        pub.subscribe(self.deletePageWithFileSubscriber , 'notebook.deletepagewithfile')
        pub.subscribe(self.saveTabStateSubscriber , 'notebook.savetabstate')
        pub.subscribe(self.openSavedTabsSubscriber, 'notebook.opensavedtabs')
        pub.subscribe(self.closeTabSubscriber, 'notebook.closetab')
        pub.subscribe(self.saveFileSubscriber, 'notebook.savefile')

    ##--------------------------------------------------------------------------
    ## Subscriber action, add default page
    ##--------------------------------------------------------------------------
    def addPageSubscriber(self, message):
        data = message.data

        try:
            filepath = data['file']
            prjid = data['prjid']
        except TypeError:
            filepath = None
            prjid = None

        self.AddDefaultPage(filepath, prjid)

    def deletePageWithFileSubscriber(self, message):
        pagecount = self.GetPageCount()

        for i in range(0, pagecount):
            page = self.GetPage(i)
            if message.data == page.GetFilePath():
                self.DeletePage(i)
                break

    def saveTabStateSubscriber(self, message):
        self.db.DeleteRegisteredOpenedTabs()

        if message.data == True:
            for key in self.openedtabs:
                for value in self.openedtabs[key]:
                    self.db.RegisterOpenedTab(key, value)

    def openSavedTabsSubscriber(self, message):
        id = message.data
        self.openTabs(id)

    def closeTabSubscriber(self, message):
        editorfocus = self.FindFocus()

        if editorfocus.__class__.__name__ == 'WpTextEditor':
            ## If current editor is modified yield warning upon close
            if(editorfocus.GetModify() == True):
                dialog = wx.MessageDialog( None,
                                                'Are you sure to want to close this tab?',
                                                'Question',
                                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
                                        )

                status = dialog.ShowModal()

                if status != wx.ID_YES:
                    return

                dialog.Destroy()

            ## Deregister tab
            self.deRegisterTab(editorfocus.GetFilePath())

            ## Continue closing
            pagecount = self.GetPageCount()

            selected = self.GetSelection() # Get which tab that is in focus

            self.Freeze()

            ## Making sure we add a new page if we're deleting the last page
            if(pagecount == 1):
                self.AddDefaultPage()

            self.DeletePage(selected) # Delete unwanted tab
            self.Thaw()

        return

    def saveFileSubscriber(self, message):
        editor = self.FindFocus()

        if editor.__class__.__name__ == 'WpTextEditor':
            editor.SaveFile()
        

    #---------------------------------------------------------------
    # Add text editor to page
    # @param string filepath <conditional>
    # @return object texteditor
    #---------------------------------------------------------------
    def _AddTextEditor( self, filepath=None):
        texteditor = WpTextEditor( self )
        # Adding content
        if filepath is not None:
            texteditor.SetFilePath( filepath )
            texteditor.SetDefaultLexer()

        return texteditor

    #---------------------------------------------------------------
    # Register opened tab
    # @param integer prjid
    # @param string filepath
    #---------------------------------------------------------------
    def registerTab(self, prjid, filepath):
        if filepath != None:
            if prjid == None:
                self.openedtabs['None'].append(filepath)
            else:
                try:
                    self.openedtabs[prjid].append(filepath)
                except KeyError:
                    self.openedtabs[prjid] = []
                    self.openedtabs[prjid].append(filepath)

    #---------------------------------------------------------------
    # Deregister opened tab
    # @param integer prjid
    # @param string filepath
    #---------------------------------------------------------------
    def deRegisterTab(self, filepath):
        if filepath != None:
            for index in self.openedtabs:
                try:
                    self.openedtabs[index].remove(str(filepath))
                except:
                    continue

    ##---------------------------------------------------------------
    ## Add default page
    ## @param string filepath <conditional>
    ##---------------------------------------------------------------
    def AddDefaultPage(self, file_path=None, file_prj_id=None):
        self.registerTab(file_prj_id, file_path)
        page_title = 'new'

        page_count  = self.GetPageCount()
        page_reload = True
        page_index  = None

        for index in range(0, page_count):
            page_path = self.GetPage(index).GetFilePath()

            if page_path == None: continue
            elif page_path == file_path:
                page_reload = False ## Page already exists don't reload page
                page_index  = index

        ## Prevent multiple opening of file
        if page_reload == True:
            if file_path != None:
                splitted_path = os.path.split(file_path)
                page_title = splitted_path[1]

            self.Freeze() ## Prevent flickering
            page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
            self.AddPage(self._AddTextEditor(file_path), page_title, True, page_bmp)

            self.Thaw() ## Get back to normal state
            
        else:
            self.SetSelection(page_index)

    def openTabs(self, project='None'):
        ## Get tabs to be opened
        tabs = self.db.GetRegisteredTabs(project)
        totaltabs = len(tabs)

        self.Freeze()
        if tabs != None:
            for file in tabs:
                self.AddDefaultPage(file, project)
        self.Thaw()

        return totaltabs