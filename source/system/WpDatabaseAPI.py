# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpDatabaseAPI
# Desc: 
# 	Database API for common database interaction
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

from system.WpDatabase import WpDatabase
from system.WpProject import WpProject

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
	## Project API Functions
	##---------------------------------------------------------------

        def AddProject(self, project):
            """
            Add project into persistent storage
            Input project instance of WpProject.
            """
            ## TODO: Add better checks here
            projectInsert = "INSERT INTO projects('title') VALUES('%s');" % (project.GetTitle())
            projectId = self.Insert(projectInsert)

            for path in project.GetPaths():
                pathInsert = "INSERT INTO projectincludes('projectid','path') VALUES(%i,'%s');" % (projectId, path)
                self.Insert(pathInsert)

            return True

        def GetProjectList(self):
            """
            Get a list of projects containing their title and id
            """
            query = "SELECT id, title FROM projects ORDER BY title;"

            structure = []
            for entry in self.Select(query):
                info = {
                            'id': entry[0],
                            'title': entry[1]
                        }

                structure.append(info)
                
            return structure





	##---------------------------------------------------------------
	## System Specific API Functions
	##---------------------------------------------------------------
	def RunScript( self, path ):
            self.RunSqlScript( path )