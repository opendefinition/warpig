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
		
		retval = []
		
		tmpfilefilter = re.compile( '~' )

		for file in os.listdir( path ):
			if tmpfilefilter.search( file ) is None:
				retval.append( file )

		return retval
			
	ListDirectory = WpCallable( ListDirectory )
		
	def YamlConvert( structure ):
		"""
		Convert any structure into Yaml format
		@param mixed structure
		"""
		return yaml.dump( structure )

	YamlConvert = WpCallable( YamlConvert )
	
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