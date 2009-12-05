import wx
import time
import wx.lib.buttons as buttons

class StopwatchGui(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, wx.ID_ANY, 'Warpig Stopwatch', size=(300, 300))
        self.__Setup()
        self.counter = 0
        self.Center()

    def __Setup(self):
        # Mainpanel to hold everything
        sizeHeight = self.GetSize()[1]
        sizeWidth = self.GetSize()[0]

        # Mainsizer
        self.mainsizer = wx.BoxSizer( wx.VERTICAL )

        # Panel
        self.mainpanel = wx.Panel( self, -1, size=( sizeHeight, sizeWidth ) )
        mainpanel_sizer = wx.BoxSizer(wx.VERTICAL)

        # Time field
        self.time_field = wx.StaticText(self.mainpanel, wx.ID_ANY, '00:00:00')
        timefield_sizer = wx.BoxSizer(wx.VERTICAL)
        timefield_sizer.Add(self.time_field)

        # Stopwatch
        self.stopwatch = wx.Timer(self)

        # Recorded time list
        self.timelist = wx.ListCtrl(
                            self.mainpanel,
                            wx.ID_ANY,
                            style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_VRULES | wx.LC_HRULES | wx.LC_SINGLE_SEL
                        )

        self.timelist.InsertColumn(0, 'Time', 0, 295)
        timelist_sizer = wx.BoxSizer(wx.VERTICAL)
        timelist_sizer.Add(self.timelist, 1, wx.EXPAND)

        # Buttons
        #self.record_button = wx.Button(self.mainpanel, wx.ID_ANY, 'Record')
        self.record_button = buttons.ThemedGenButton(self.mainpanel, wx.ID_ANY, 'Record')
        self.start_stop_button = buttons.ThemedGenToggleButton(self.mainpanel, wx.ID_ANY, 'Start')
        self.start_stop_button.SetSize(self.record_button.GetSizer())
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.start_stop_button)
        button_sizer.Add(self.record_button)

        mainpanel_sizer.Add(timefield_sizer, 1, wx.EXPAND)
        mainpanel_sizer.Add(button_sizer, 0, wx.EXPAND)
        mainpanel_sizer.Add(timelist_sizer, 1, wx.EXPAND)

        # Sewing it all together
        self.mainsizer.Add(mainpanel_sizer, 1, wx.EXPAND)
        self.SetSizer(self.mainsizer, wx.EXPAND)

        # Bindings
        self.Bind(wx.EVT_BUTTON, self.__onToggleButton, id=self.start_stop_button.GetId())
        self.Bind(wx.EVT_TIMER, self.__onTimer, self.stopwatch)
        self.Bind(wx.EVT_BUTTON, self.__onRecord, id=self.record_button.GetId())

    def __onToggleButton(self, event):
        value = self.start_stop_button.GetValue()

        if value == True:
            self.start_stop_button.SetLabel('Stop')
            self.stopwatch.Start(1, wx.TIMER_CONTINUOUS)
        else:
            self.start_stop_button.SetLabel('Start')
            self.stopwatch.Stop()
            self.time_field.SetLabel(str(self.millisecondsToTime()))
            self.counter = 0

    def __onTimer(self, event):
        self.counter += 1
        self.time_field.SetLabel(str(self.millisecondsToTime()))

    def __onRecord(self, event):
        item = wx.ListItem()
        item.SetText(self.millisecondsToTime())
        self.timelist.InsertItem(item)

    def millisecondsToTime(self):
        milli = self.counter
        milli %= 1000
        seconds = self.counter/1000
        minutes = seconds/60
        seconds %= 60

        hours = minutes/60
        minutes %= 60

        return "%02d:%02d:%03d" % (minutes, seconds, milli)

class Stopwatch:
    def run(self):
        sw = StopwatchGui()
        sw.Show()