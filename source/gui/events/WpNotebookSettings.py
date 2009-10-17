import wx

WARPIG_REFRESH_EDITOR_SETTINGS = wx.NewEventType()
REFRESH_EDITOR_SETTINGS = wx.PyEventBinder(WARPIG_REFRESH_EDITOR_SETTINGS,1)

class WpEditorSettingsEvent(wx.PyCommandEvent):
	def __init__(self, evtType, id):
		wx.PyCommandEvent.__init__(self, evtType, id)
