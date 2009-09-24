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
		
		##
		# Subpages
		##
		
		self.AddPage( testpanel1, "General" )
		self.AddSubPage( WpEditorSettings( self ), "Editor" )
			
		wx.FutureCall( 100, self.AdjustSize )
		
	def AdjustSize(self):
		self.GetTreeCtrl().InvalidateBestSize()
		self.SendSizeEvent()