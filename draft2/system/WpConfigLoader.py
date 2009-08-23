## Load config from database using borg pattern (see class WpConfigSystem)

from system.WpDatabaseAPI import WpDatabaseAPI
from system.WpConfigSystem import WpConfigSystem

class WpConfigLoader:
	def LoadConfig( self ):
		db = WpDatabaseAPI()
		
		storage = WpConfigSystem()
		storage.settings = {}
		
		registrysettings = db.LoadRegistry()

		for config in registrysettings:
			setting = config[2] + "-" + config[0]
			storage.settings[setting] = config[1]