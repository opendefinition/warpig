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
		projectInsert = "INSERT INTO projects('title','description') VALUES('%s', '%s');" % (project.GetTitle(), project.GetDescription())
		projectId = self.Insert(projectInsert)

		for path in project.GetPaths():
			pathInsert = "INSERT INTO projectincludes('projectid','path') VALUES(%i,'%s');" % (projectId, path)
			self.Insert(pathInsert)

		return projectId

	def GetProjectList(self):
		"""
		Get a list of projects containing their title and id
		"""
		query = "SELECT id, title, description FROM projects ORDER BY title;"

		structure = []
		for entry in self.Select(query):
			info = {
						'id': entry[0],
						'title': entry[1],
						'description': entry[2]
					}

			structure.append(info)

		return structure

	def GetProject(self, projectid):
		project = WpProject()

		projectquery = "SElECT * FROM projects WHERE id=%i" % (int(projectid))
		projectinfo = self.Select(projectquery)

		for info in projectinfo:
			project.SetId(info[0])
			project.SetTitle(info[1])
			project.SetDescription(info[2])
			project.SetDateCreated(info[3])


		includesquery = "SELECT path FROM projectincludes WHERE projectid=%i" % (int(projectid))
		includes = self.Select(includesquery)

		for include in includes:
			project.AddPath(include[0])

		return project

	def GetProjectsLog(self):
		selectionQuery = "SELECT prj.id, prj.title FROM projectlog plog LEFT OUTER JOIN projects prj ON plog.id=prj.id WHERE prj.id NOT NULL ORDER BY plog.date DESC LIMIT 10;"
		result = self.Select( selectionQuery )

		if len( result ) == 0:
			result = []

		return result

	def DeleteProject(self, id):
		deleteProject = "DELETE FROM projects WHERE id=%i;" % (id)
		deleteIncludes = "DELETE FROM projectincludes WHERE projectid=%i;" % (id)

		self.Delete(deleteProject)
		self.Delete(deleteIncludes)

	def DeleteRegisteredOpenedTabs(self):
		deleteQuery = "DELETE FROM openedtabs;"
		self.Delete(deleteQuery)

	def RegisterOpenedTab(self, projectid, filepath):
		insertionQuery = "INSERT INTO openedtabs(prjid, file) VALUES('%s', '%s')" %(projectid, filepath)
		self.Insert(insertionQuery)

	def GetRegisteredTabs(self, key):
		selectionQuery = "SELECT file FROM openedtabs WHERE prjid='%s'" % (key)
		result = self.Select(selectionQuery)

		list = []
		for item in result:
			list.append(item[0])

		return list

	def AddRecentProjectLogEntry(self, projectId):
		insertionQuery = "INSERT OR REPLACE INTO projectlog (id) VALUES(%s)" % ( projectId )
		self.Insert( insertionQuery )

	##---------------------------------------------------------------
	## System Specific API Functions
	##---------------------------------------------------------------
	def RunScript( self, path ):
		self.RunSqlScript( path )