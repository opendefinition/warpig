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
		query = "UPDATE systemregistry SET value='%s' WHERE module='%s' AND key='%s';" % ( value, module, key )
		return self.Insert( query )
		
	def GetRegisterSetting( self, key, module ):
		"""
		Obtain register setting identified by key
		"""
		query = "SELECT key, value, module FROM systemregistry WHERE key='%s' AND module='%s';" % ( key, module )
		result = self.Select( query )
		
		return result
		
	def LoadRegistry(self):
		"""
		Obtain All Settings In Registry
		"""
		query = "SELECT key,value,module FROM systemregistry;"
		result = self.Select( query )
		
		return result
	
	##---------------------------------------------------------------
	## System Specific API Functions
	##---------------------------------------------------------------
	def RunScript( self, path ):
		self.RunSqlScript( path )