import wx

from gui.preferences.WpEditorSettings import WpEditorSettings

class WpPreferenceTree( wx.Treebook ):
	def __init__(self, parent, id ):
		wx.Treebook.__init__(self, parent, id, style=wx.BK_DEFAULT|wx.EXPAND )
		self.Setup()
		
	def Setup( self ):
		##
		# Adding pages
		##
		
		testpanel1 = wx.Panel( self, -1 )
		button1 = wx.Button( testpanel1, -1, "Test button 1" )
		
		testpanel2 = wx.Panel( self, -1 )
		button2 = wx.Button( testpanel2, -1, "Test button 2" )
		
		testpanel3 = wx.Panel( self, -1 )
		button3 = wx.Button( testpanel3, -1, "Test button 3" )
		
		##
		# Subpages
		##
		
		self.AddPage( testpanel1, "General" )
		self.AddSubPage( WpEditorSettings( self ), "Editor" )
		self.AddSubPage( wx.Panel( self, -1 ), "Fonts" )
		self.AddPage( testpanel2, "Look and feel" )
		self.AddPage( testpanel3, "VCS" )
		
		wx.FutureCall( 100, self.AdjustSize )
		
	def AdjustSize(self):
		self.GetTreeCtrl().InvalidateBestSize()
		self.SendSizeEvent()