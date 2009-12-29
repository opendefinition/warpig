##------------------------------------------------------------------------------
## Class Keybindings
##
## Handles any keycode combinations in Warpig CE by sending messages to widgets
##------------------------------------------------------------------------------

import wx
from wx.lib.pubsub import Publisher as pub

class Keybindings:
    def __init__(self, parent):
        ## Reference to widget that called that instantiated this class
        self.parent = parent

    ##--------------------------------------------------------------------------
    ## Initialize keybindings
    ##--------------------------------------------------------------------------
    def init(self):
        ## Listen for any key down events triggered
        self.parent.Bind(wx.EVT_KEY_DOWN, self.KeyDownEvent)

    ##--------------------------------------------------------------------------
    ## Responder for keydown event
    ##--------------------------------------------------------------------------
    def KeyDownEvent(self, event):
        commandKey = event.CmdDown()
        pressedKey = event.GetUniChar()

        if commandKey == True:
            self.HandleCommandKeyCombination(pressedKey)
            event.Skip(True)
        else:
            event.Skip(False)

        return


    ##--------------------------------------------------------------------------
    ## Handle commandkey+keycode combinations
    ## @param integer keycode
    ##--------------------------------------------------------------------------
    def HandleCommandKeyCombination(self, keycode):

        ## Exit this application
        ## NOTE: This might possibly be deleted
        if keycode == 83 or keycode == 113:
            self.parent.Close()

        ## Add new page with editor to current notebook instance
        elif keycode == 78 or keycode == 110:
            self.notifySubscribers('notebook.addpage')
            
        ## Open file
        if keycode == 79 or keycode == 111:
            self.notifySubscribers('mainmenu.openfile')

    ##--------------------------------------------------------------------------
    ## Handle regular keycodes
    ## @param ineger keycode
    ##--------------------------------------------------------------------------
    def HandleRegularKey(self, keycode):
        print "Regular key"

    ##--------------------------------------------------------------------------
    ## Notify subscriber widgets that they are inwoked
    ## @param string subject Subscription subjects
    ## @param mixed value Any valued that needs to be sent
    ##--------------------------------------------------------------------------
    def notifySubscribers(self, subject, value=None):
        pub.sendMessage(subject, value)
        return