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

#from wx._misc import Get
import os
import wx
import wx.lib.agw.aui as aui

from gui.WpTextEditor import WpTextEditor
from wx.lib.pubsub import Publisher as pub

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

        art = arts[3]()
        self.SetArtProvider(art)

        ## Subscribe to add page event message
        pub.subscribe(self.addPageSubscriber, 'notebook.addpage')

    ##--------------------------------------------------------------------------
    ## Subscriber action, add default page
    ##--------------------------------------------------------------------------
    def addPageSubscriber(self, message):
        self.AddDefaultPage(message.data)

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

    ##---------------------------------------------------------------
    ## Add default page
    ## @param string filepath <conditional>
    ##---------------------------------------------------------------
    def AddDefaultPage(self, file_path=None):
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

            if page_count > 0 and self.GetPage(0).GetFilePath() == None and len(self.GetPage(0).GetText()) == 0 and file_path != None:
                page_title = os.path.split(file_path)[1]
                self.SetPageText(0, page_title)
                self.GetPage(0).SetFilePath(file_path)
            else:
                self.AddPage(self._AddTextEditor(file_path), page_title, True, page_bmp)

            self.Thaw() ## Get back to normal state
            
        else:
            self.SetSelection(page_index)