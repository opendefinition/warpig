# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpConfigLoader
# Desc: 
# 	Load config from database using borg pattern (see class WpConfigSystem)
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

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