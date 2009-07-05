import wx

class WpEditorSettings( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__( self, parent, *args, **kwargs )
		self.Setup()
		None
		
	def Setup( self ):
		self.mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.mainsizer.Add( self.TabSetting() )
		self.mainsizer.Add( self.StaticLine() )
		self.mainsizer.Add( self.MarginSetting() )
		self.mainsizer.Add( self.StaticLine() )
		self.mainsizer.Add( self.FontSetting() )
		self.mainsizer.Add( self.StaticLine() )
		
		self.SetSizer( self.mainsizer, wx.EXPAND )
		
		
	def StaticLine( self ): 
		return wx.StaticLine( self, wx.ID_ANY, size=(100,-1), style=wx.LI_HORIZONTAL )
		
	def TabSetting( self ):
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		inputsizer =  wx.BoxSizer( wx.HORIZONTAL )
		checkboxsizer =  wx.BoxSizer( wx.HORIZONTAL )
		
		## Text input
		label = wx.StaticText( self, wx.ID_ANY, "Tabsize: " )
		tabsizeinput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
	
		inputsizer.Add( label )
		inputsizer.Add( tabsizeinput )
		
		## Checkbox
		checkbox = wx.CheckBox( self, wx.ID_ANY, "Use tab" )
		checkboxsizer.Add( checkbox )
		
		sizer.Add( inputsizer )
		sizer.Add( checkboxsizer )
		
		return sizer
		
	def MarginSetting( self ):
		marginsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		label = wx.StaticText( self, wx.ID_ANY, "Margin size: " )
		marginsizeinput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		
		marginsizer.Add( label )
		marginsizer.Add( marginsizeinput )
		
		return marginsizer
		
	def FontSetting( self ):
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		fontsizesizer = wx.BoxSizer( wx.HORIZONTAL )
		label = wx.StaticText( self, wx.ID_ANY, "Font size: " )
		fontsizeinput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		fontsizesizer.Add( label )
		fontsizesizer.Add( fontsizeinput )
		
		fontfamilysizer = wx.BoxSizer( wx.HORIZONTAL )
		fontfamilylabel = wx.StaticText( self, wx.ID_ANY, "Font family: " )
		fontfamilyinput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		fontfamilysizer.Add( fontfamilylabel )
		fontfamilysizer.Add( fontfamilyinput )
		
		sizer.Add( fontsizesizer )
		sizer.Add( fontfamilysizer )
		return sizer
		
