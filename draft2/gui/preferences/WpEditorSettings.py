# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpEditorSettings
# Desc: 
# 	GUI dialog for managing editor settings
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import wx
from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpConfigSystem import WpConfigSystem

class WpEditorSettings( wx.Panel ):
	def __init__( self, parent, *args, **kwargs ):
		wx.Panel.__init__( self, parent, *args, **kwargs )
		self.configobj = WpConfigSystem()
		self.Setup()
		None
		
	def Setup( self ):
		self.mainSizer = wx.FlexGridSizer( rows=4, cols=1, vgap=5, hgap=5 )
		self.saveBt = wx.Button( self, wx.ID_ANY, 'Save' )
		
		self.mainSizer.AddMany(
			[
				( self.TabSetting(), 1, wx.EXPAND ),
				( self.MarginSetting(), 1, wx.EXPAND ),
				( self.FontSetting(), 1, wx.EXPAND ),
				( self.saveBt, 1, wx.EXPAND )
			]
		) 
		
		self.SetSizer( self.mainSizer, wx.EXPAND )
		
		## Bind Savebutton
		self.Bind( wx.EVT_BUTTON, self.__OnSaveSettings, id=self.saveBt.GetId() )
		
	def TabSetting( self ):
		sizer = wx.BoxSizer( wx.HORIZONTAL )
		
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
		self.marginSizeInput.SetValue( self.configobj.settings['editor-textmargin'] )
		
		marginsizer.Add( label )
		marginsizer.Add( self.marginSizeInput )
		
		return marginsizer
		
	def FontSetting( self ):
		## Sizers
		sizer = wx.BoxSizer( wx.VERTICAL )
		fontSizer =  wx.FlexGridSizer(rows=2, cols=2, vgap=0, hgap=0)
		
		## Font size selector
		fontSizes = ['9','10','11','12', '13','14','15','16','17','18','19','20']
		fontSizeLabel = wx.StaticText( self, wx.ID_ANY, 'Font size' )
		self.fontSizeSelect = wx.Choice( self, -1, (100, 50), choices=fontSizes )

		## Font family selector
		fontFamilylabel = wx.StaticText( self, wx.ID_ANY, 'Font family' )
		enumerator = wx.FontEnumerator()
		enumerator.EnumerateFacenames()
		fontlist = enumerator.GetFacenames()
		
		self.fontListCtrl = wx.ListBox( self, wx.ID_ANY, choices=fontlist, style=wx.LB_SORT )
		
		## Making sure that any previous settings shows as defaults
		configuration = WpConfigSystem()
		
		currentSize = self.configobj.settings['editor-fontsize']
		self.fontSizeSelect.Select(fontSizes.index(currentSize))
		
		currentFontface = self.configobj.settings['editor-fontface']
		self.fontListCtrl.Select( self.fontListCtrl.FindString(currentFontface) )

		## Grouping
		fontSizer.AddMany(
			[
				( fontFamilylabel, 1, wx.EXPAND ),
				( fontSizeLabel, 1, wx.EXPAND ),
				( self.fontListCtrl, 1, wx.EXPAND ),
				( self.fontSizeSelect, 0 )
			]
		) 
		
		## Font selection preview text
		self.previewText = wx.StaticText( self, wx.ID_ANY, "Warpig Code Environment Text" )

		## Font events
		self.Bind( wx.EVT_CHOICE, self.__OnFontSelect, id=self.fontSizeSelect.GetId() )
		self.Bind( wx.EVT_LISTBOX, self.__OnFontSelect, id=self.fontListCtrl.GetId() )
		
		## Be sure that the font preview text is updated
		self.updateFontPreview()
		
		## Adding controllers to main sizer
		sizer.Add( fontSizer )
		sizer.Add( self.previewText )
		return sizer
		
	# ----[ START : Event handlers ]---
	def __OnFontSelect( self, event ): 
		self.updateFontPreview()
	
	def __OnSaveSettings( self, event ):
		self.saveSettings()	
	#---[ END : Event handlers ]---
	
	#---[ START: Helper functons ]---
	def updateFontPreview(self):
		"""
		Internal helper function for setting the font preview text
		"""
		face = self.fontListCtrl.GetStringSelection()
		size = int( self.fontSizeSelect.GetString( self.fontSizeSelect.GetSelection() ) )
	
		font = wx.Font( size, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, face )
		self.previewText.SetFont( font )
		
	def saveSettings(self):
		"""
		Save settings
		"""
		db = WpDatabaseAPI()
		
		## Savin margin settings
		textMarginValue = self.marginSizeInput.GetValue()
		db.AddRegisterSetting( 'textmargin', textMarginValue, 'editor' )
		self.configobj.settings['editor-textmargin'] = textMarginValue
		
		## Saving fonts
		fontFace = self.fontListCtrl.GetStringSelection()
		fontSize = int( self.fontSizeSelect.GetString( self.fontSizeSelect.GetSelection() ) )
		
		db.AddRegisterSetting( 'fontface', fontFace, 'editor' )
		self.configobj.settings['editor-fontface'] = fontFace
		db.AddRegisterSetting( 'fontsize', fontSize, 'editor' )
		self.configobj.settings['editor-fontsize'] = int( fontSize )
	#---[ END: Helper functons ]---
