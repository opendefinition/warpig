import wx

from wx.lib.agw import buttonpanel as bp

class MainButtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonpanel = bp.ButtonPanel(self, wx.ID_ANY, "", style=wx.NO_BORDER, alignment=bp.BP_ALIGN_LEFT)
        mainsizer.Add(self.buttonpanel, 1, wx.EXPAND)
        self.__setup()

        self.SetSizer(mainsizer)

    def __setup(self):
        new = bp.ButtonInfo(self.buttonpanel, wx.ID_NEW, wx.Bitmap("./gui/icons/document-new.png", wx.BITMAP_TYPE_PNG))
        self.buttonpanel.AddButton(new)

        open = bp.ButtonInfo(self.buttonpanel, wx.ID_OPEN, wx.Bitmap("./gui/icons/folder.png", wx.BITMAP_TYPE_PNG))
        self.buttonpanel.AddButton(open)

        save = bp.ButtonInfo(self.buttonpanel, wx.ID_SAVE, wx.Bitmap("./gui/icons/media-floppy.png", wx.BITMAP_TYPE_PNG))
        self.buttonpanel.AddButton(save)

        self.buttonpanel.DoLayout()

        ##self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarNewPage, id=btn1.GetId() )
        ##self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarOpenPage, id=btn2.GetId() )
        ##self.Bind( wx.EVT_BUTTON, self.Parent.Parent._OnToolBarSavePage, id=btn3.GetId() )


        ##return self.buttonpanel
        