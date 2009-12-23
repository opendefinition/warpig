# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpElementData
# Desc: Class for storing simple data regarding a node or a file in project
# 		tree.
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

class WpElementData:
	def __init__(self):
		self.__current_directory = None
		self.__current_file = None
		self.__current_file_name = None
                self.__current_project_id = None

        def setProjectId(self, id):
                """
                Set which project this file belongs to
                @param Integer id
                """
                self.__current_project_id = id

        def getProjectId(self):
                """
                Get which project this file belongs to
                @return Integer id
                """
                return self.__current_project_id
		
	def getCurrentDirectory(self):	
		"""
		Get current directory path
		@return String Path
		"""
		return self.__current_directory
		
	def setCurrentDirectory(self, path):
		"""
		Set current directory path
		@param String path
		"""
		self.__current_directory = path
		
	def getCurrentFile(self):
		"""
		Get current file path
		@return String Path
		"""
		return self.__current_file
		
	def setCurrentFile(self, path):
		"""
		Set current file path
		@param String path
		"""
		self.__current_file = path
		
	def getCurrentFilename(self):
		"""
		Get current filename
		@return String Filename
		"""
		return self.__current_file_name
		
	def setCurrentFilename(self, filename):
		"""
		Set Current Filename
		@param String filename
		"""
		self.__current_file_name = filename