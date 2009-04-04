# -*- coding: utf-8 -*-
#==================================================================================================
# Open Definition WpFileSystem
# Author: Roger C.B. Johnsen
# 
# Various filesystem helper functions wrapped in a class (static)
#==================================================================================================

import os
import re
import yaml

class WpCallable:
    def __init__(self, call ):
        self.__call__ = call

class WpFileSystem:
	def SaveProjectFile( fullpath ):
		# Splitting fullpath into easier manageable parts
		fileinfo = os.path.split( fullpath )
		filepath = fileinfo[ 0 ]
		filename = fileinfo[ 1 ]
		
		# Get directory list
		directory = WpFileSystem.ListDirectory( filepath )
		
		# Convert directory to YAML
		yamllist = WpFileSystem.StructureToYaml( directory )
		
		# Store YAML list inside project definition file
		WpFileSystem.SaveToFile( yamllist, fullpath)
		
		return {
				'fpath' 	: filepath,
				'fname'	 	: filename,
				'orig'		: fullpath,
				'dirlist' 	: directory
 			}
 			
 	SaveProjectFile = WpCallable( SaveProjectFile )

	def SplitFilepath( path ):
		"""
		Split path into path and filename
		@param string path
		"""
		length = len( path )
		startindex = path.rfind( '/' )+1
		
		retval = { 
			'fpath' : path[0:startindex],
			'fname' : path[startindex:length],
			'orig' : path
		}
		
		return retval
	
	SplitFilepath = WpCallable( SplitFilepath )
	
	def ListDirectory( path ):
		"""
		List Directory
		@param string path
		"""
		files = []
		
		tmpfilefilter = re.compile( '~' )

		for file in os.listdir( path ):
			if tmpfilefilter.search( file ) is None:
				files.append( file )
	
		retval = {
				'path': path,
				'files': files
			}
	
		return retval
			
	ListDirectory = WpCallable( ListDirectory )
		
	def StructureToYaml( structure ):
		"""
		Convert any structure into Yaml format
		@param mixed structure
		"""
		return yaml.dump( structure )

	StructureToYaml = WpCallable( StructureToYaml )
	
	def YamlToStructure( yml ):
		"""
		Convert Yaml to stucture
		@param string yml
		"""
		return yaml.load( yml )
		
	YamlToStructure = WpCallable( YamlToStructure )
	
	def SaveToFile( content, filename, mode='w' ):
		"""
		Write content to file
		@param string content
		@param string filename
		@param string writemode
		"""
		file = open( filename, mode )
		file.write( content )
		file.close()
		
		return True
		
	SaveToFile = WpCallable( SaveToFile )
	
	def ReadFromFile( path ):
		"""
		Read content from file
		@param string path
		"""
		file = open( path, 'r' )
		retval = file.read()
		file.close()
		
		return retval
		
	ReadFromFile = WpCallable( ReadFromFile )