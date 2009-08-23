import wx
from system.WpDatabaseAPI import WpDatabaseAPI

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
		
		savebt = wx.Button( self, wx.ID_ANY, 'Save' )
		self.mainsizer.Add( savebt )
		
		self.SetSizer( self.mainsizer, wx.EXPAND )
		
		## Bind Savebutton
		self.Bind( wx.EVT_BUTTON, self.OnSaveSettings, id=savebt.GetId() )
		
		
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
		self.marginSizeInput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		
		marginsizer.Add( label )
		marginsizer.Add( self.marginSizeInput )
		
		return marginsizer
		
	def FontSetting( self ):
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		fontsizesizer = wx.BoxSizer( wx.HORIZONTAL )
		label = wx.StaticText( self, wx.ID_ANY, "Font size: " )
		
		fontsizes = ['9','10','11','12', '13','14','15','16','17','18','19','20']
		
		self.fontsizeinput = wx.Choice( self, -1, (100, 50), choices=fontsizes )
		fontsizesizer.Add( label )
		fontsizesizer.Add( self.fontsizeinput )
		
		fontfamilysizer = wx.BoxSizer( wx.VERTICAL )
		fontfamilylabel = wx.StaticText( self, wx.ID_ANY, "Font family: " )
		
		## Getting system fonts
		enumerator = wx.FontEnumerator()
		enumerator.EnumerateFacenames()
		fontlist = enumerator.GetFacenames()
		
		## Font list control
		self.fontlistctrl = wx.ListBox( self, wx.ID_ANY, choices=fontlist )
		
		## Demo text
		self.demotext = wx.StaticText( self, wx.ID_ANY, "Fear of the D'Arc..." )
		
		fontfamilysizer.Add( fontfamilylabel )
		fontfamilysizer.Add( self.fontlistctrl )
		fontfamilysizer.Add( self.demotext )
		
		sizer.Add( fontsizesizer )
		sizer.Add( fontfamilysizer )
		
		## Font events
		self.Bind( wx.EVT_LISTBOX, self.OnFontSelect, id=self.fontlistctrl.GetId() )
		
		return sizer

	def OnFontSelect( self, event ):
		face = self.fontlistctrl.GetStringSelection()
		size = int( self.fontsizeinput.GetString( self.fontsizeinput.GetSelection() ) )
	
		font = wx.Font( size, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, face )
		self.demotext.SetFont( font )
		
	def OnSaveSettings( self, event ):
		db = WpDatabaseAPI()
		
		## Savin margin settings
		textMarginValue = self.marginSizeInput.GetValue()
		db.AddRegisterSetting( 'textmargin', textMarginValue, 'editor' )
		
		## Saving fonts
		fontFace = self.fontlistctrl.GetStringSelection()
		fontSize = int( self.fontsizeinput.GetString( self.fontsizeinput.GetSelection() ) )
		
		db.AddRegisterSetting( 'fontface', fontFace, 'editor' )
		db.AddRegisterSetting( 'fontsize', fontSize, 'editor' )
