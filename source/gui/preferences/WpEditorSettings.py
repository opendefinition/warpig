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
		self.mainSizer.AddSpacer(5)
		self.mainSizer.AddMany(
			[
				(self.TabSetting(), 1, wx.EXPAND),
				(self.MarginSetting(), 1, wx.EXPAND),
				(self.FontSetting(), 1, wx.EXPAND),
                                (self.FoldingSetting(), 1, wx.EXPAND),
				(self.saveBt, 1, wx.EXPAND )
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
		self.tabsizeinput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		
		self.tabsizeinput.SetValue( self.configobj.settings['editor-tabsize'])
	
		inputsizer.Add( label )
		inputsizer.Add( self.tabsizeinput )
		
		## Checkbox
		self.checkbox = wx.CheckBox( self, wx.ID_ANY, "Use tab" )
		checkboxsizer.Add( self.checkbox )
                
                usetabulator = int(self.configobj.settings['editor-usetab'])
                if usetabulator == True:
			self.checkbox.SetValue(True)    # Set to checked state
                        self.tabsizeinput.Disable()     # Disable user input
		else:
			self.checkbox.SetValue(False)   # Set to unchecked state
                        self.tabsizeinput.Enable()      # Enable user input
		
		sizer.Add( inputsizer )
		sizer.Add( checkboxsizer )
		
		self.Bind(wx.EVT_CHECKBOX, self.onUseTabChecked,id=self.checkbox.GetId())
		
		return sizer
		
	def onUseTabChecked(self,event):
		if self.tabsizeinput.IsEnabled() == True:
			self.tabsizeinput.Disable()
		else:
			self.tabsizeinput.Enable()
		
	def MarginSetting( self ):
		marginsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		label = wx.StaticText( self, wx.ID_ANY, "Margin size: " )
		self.marginSizeInput = wx.TextCtrl( self, wx.ID_ANY, size=(100, -1) )
		self.marginSizeInput.SetValue( self.configobj.settings['editor-textmargin'] )
		
		marginsizer.Add( label )
		marginsizer.Add( self.marginSizeInput )
		
		return marginsizer

        def FoldingSetting(self):
                # Sizers
                sizer = wx.BoxSizer(wx.VERTICAL)
            
                # Checkbox
                self.codeFoldCheckbox = wx.CheckBox(self, wx.ID_ANY, "Fold code")

                foldCode = int(self.configobj.settings['editor-foldcode'])
                
                if foldCode == True:
			self.codeFoldCheckbox.SetValue(True)    # Set to checked state
		else:
			self.codeFoldCheckbox.SetValue(False)   # Set to unchecked state
            
                # Fold style
                styles = [
                        'Arrows',
                        'Plus and minus',
                        'Circular Flattened Tree',
                        'Square Flattened Tree'
                    ]
                self.foldCodeStyleSelect = wx.ComboBox(self, wx.ID_ANY, style=wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT, choices=styles)

                # Preselect folding style
                preselectedStyle = styles[ int(self.configobj.settings['editor-foldcodestyle']) ]
                self.foldCodeStyleSelect.SetStringSelection(preselectedStyle)

                sizer.Add(self.codeFoldCheckbox)
                sizer.Add(self.foldCodeStyleSelect)
                
                return sizer

		
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
		
		try:
			currentSize = str( self.configobj.settings['editor-fontsize'] )
			currentFontface = str( self.configobj.settings['editor-fontface'] )
	
			self.fontSizeSelect.Select(fontSizes.index( currentSize ) )
			self.fontListCtrl.Select( self.fontListCtrl.FindString(currentFontface) )
		except ValueError:
			## Silently supress any error messages
			None
			
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
		
		## Saving tab size
		self.configobj.settings['editor-tabsize'] = self.tabsizeinput.GetValue()
		db.AddRegisterSetting('tabsize', self.configobj.settings['editor-tabsize'], 'editor')

                # Saving if tab is to be used
                self.configobj.settings['editor-usetab'] = 1 if self.checkbox.IsChecked() == True else 0
		db.AddRegisterSetting('usetab', self.configobj.settings['editor-usetab'], 'editor')
		
		## Saving margin settings
		self.configobj.settings['editor-textmargin'] = self.marginSizeInput.GetValue()
		db.AddRegisterSetting( 'textmargin', self.configobj.settings['editor-textmargin'], 'editor' )

                ## Saving code folding
                self.configobj.settings['editor-foldcode'] = 1 if self.codeFoldCheckbox.IsChecked() == True else 0
		db.AddRegisterSetting('foldcode', self.configobj.settings['editor-foldcode'], 'editor')

                ## Saving code folding style
                self.configobj.settings['editor-foldcodestyle'] = self.foldCodeStyleSelect.GetCurrentSelection()
		db.AddRegisterSetting('foldcodestyle', self.configobj.settings['editor-foldcodestyle'], 'editor')

		## Saving fonts
		self.configobj.settings['editor-fontface'] = self.fontListCtrl.GetStringSelection()
		self.configobj.settings['editor-fontsize'] = int( self.fontSizeSelect.GetString( self.fontSizeSelect.GetSelection() ) )
		db.AddRegisterSetting( 'fontface', self.configobj.settings['editor-fontface'], 'editor' )
		db.AddRegisterSetting( 'fontsize', self.configobj.settings['editor-fontsize'], 'editor' )
	#---[ END: Helper functons ]---
