import wx

class WpProgressDialog( wx.Dialog ):
	def __init__( self, title ):
		wx.Dialog.__init__( self, None, wx.ID_ANY, title, size=(500, 300) )
		self.Setup()
		
	def Setup( self ):
		##
		# Main Panel
		##
		mainpanel = wx.Panel(self, -1, size=(500,300), style=wx.EXPAND )
		mainsizer = wx.BoxSizer( wx.VERTICAL )
		panelsizer = wx.BoxSizer( wx.VERTICAL )
		
		##
		# Gauge
		##
		self.gauge = wx.Gauge( self, -1, 50, (110, 95), (250, 25) )
		
		##
		# Textcontrol
		##
		self.text = wx.TextCtrl( self, wx.ID_ANY, style=wx.TE_MULTILINE ) 
		
		self.Bind(wx.EVT_TIMER, self.TimerHandler)
		self.timer = wx.Timer(self)
		self.timer.Start( 100 )
		
		##
		# Sewing things together
		##
		panelsizer.Add( self.gauge, 1, wx.EXPAND )
		panelsizer.Add( self.text, 1, wx.EXPAND )

		##
		# Set the main sizer to panel
		##
		mainsizer.Add( panelsizer, 1, wx.EXPAND )
		
		self.SetSizer( mainsizer )
		self.Center()

	def __del__(self):
		self.timer.Stop()
	
	def TimerHandler( self, event ):
		self.gauge.Pulse()
		
	def AppendStatusText( self, text ):
		self.text.AppendText( text )