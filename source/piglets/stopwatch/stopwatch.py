import wx
import wx.lib.analogclock as ac
import time

class StopwatchGui(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, wx.ID_ANY, 'Warpig Stopwatch', size=(300, 300))
        self.__Setup()
        self.count_flag = False
        self.Center()

    def __Setup(self):
        # Mainpanel to hold everything
        sizeHeight = self.GetSize()[1]
        sizeWidth = self.GetSize()[0]

        # Mainsizer
        self.mainsizer = wx.BoxSizer( wx.VERTICAL )

        # Panel
        self.mainpanel = wx.Panel( self, -1, size=( sizeHeight, sizeWidth ) )
        mainpanel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Time field
        self.time_field = wx.StaticText(self.mainpanel, wx.ID_ANY, '00:00:00')
        timefield_sizer = wx.BoxSizer(wx.VERTICAL)
        self.clock      = ac.AnalogClock(
                                self.mainpanel,
                                style           = wx.STATIC_BORDER,
                                hoursStyle      = ac.TICKS_SQUARE,
                                minutesStyle    = ac.TICKS_CIRCLE,
                                clockStyle      = ac.SHOW_HOURS_TICKS| \
                                                  ac.SHOW_MINUTES_TICKS|
                                                  ac.SHOW_HOURS_HAND| \
                                                  ac.SHOW_MINUTES_HAND| \
                                                  ac.SHOW_SECONDS_HAND)
                                                  
        self.clock.SetTickSize(12, target=ac.HOUR)

        timefield_sizer.Add(self.clock, 1, wx.EXPAND)
        timefield_sizer.Add(self.time_field)

        # Buttons
        # self.record_button = wx.Button(self.mainpanel, wx.ID_ANY, 'Record')
        self.start_stop_button = wx.ToggleButton(self.mainpanel, wx.ID_ANY, 'Start')
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.start_stop_button)
        # button_sizer.Add(self.record_button)

        mainpanel_sizer.Add(timefield_sizer, 1, wx.EXPAND)
        mainpanel_sizer.Add(button_sizer, 0, wx.EXPAND)

        # Sewing it all together
        self.mainsizer.Add(mainpanel_sizer, 1, wx.EXPAND)
        self.SetSizer(self.mainsizer, wx.EXPAND)

        # Bindings
        self.Bind(wx.EVT_TOGGLEBUTTON, self.__onToggleButton, id=self.start_stop_button.GetId())

    def __onToggleButton(self, event):
        value = self.start_stop_button.GetValue()

        if value == True:
            self.start_stop_button.SetLabel('Stop')
            self.count_flag = True
            self.count()
        else:
            self.start_stop_button.SetLabel('Start')
            self.count_flag = False
            self.count()

    def count(self):
        while True:
            if self.count_flag == False:
                break
                
            time.sleep(0.1)
            print ".",

class Stopwatch:
    def run(self):
        sw = StopwatchGui()
        sw.Show()