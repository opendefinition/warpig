from system.WpDatabase import WpDatabase

class WpDatabaseAPI( WpDatabase ):
	def __init__( self ):
		WpDatabase.__init__( self )	
		
	##---------------------------------------------------------------
	## System Register API Functions
	##---------------------------------------------------------------
	def AddRegisterSetting( self, key, value, module ):
		"""
		Add Register Setting
		@param String key
		@param String value
		@param String module
		@param Boolean status
		"""
		## TODO: Add validation to input parameters
		query = "INSERT INTO systemregistry(key, value, module) VALUES('%s','%s','%s');" % ( key, value, module )
		return self.Insert( query )
		
	def GetRegisterSetting( self, key, module ):
		"""
		Obtain register setting identified by key
		"""
		query = "SELECT key, value, module FROM systemregistry WHERE key='%s' AND module='%s';" % ( key, module )
		return self.Select( query )