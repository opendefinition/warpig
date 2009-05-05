# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpFileSystem
# Desc: Various filesystem helper functions wrapped in a class (static)
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

import os
import re
import yaml

class WpCallable:
    def __init__(self, call ):
        self.__call__ = call

class WpFileSystem:
	#---------------------------------------------------------------
	# Save project file
	# @param string projectpath
	# @param string projectfilespath
	# @return dictionary fileinfo
	#---------------------------------------------------------------
	def SaveProjectFile( projectfile, directories ):
	
		project = {
			'project' : {
						'path': projectfile,
						'name': os.path.split( projectfile )[ 1 ][0:-4]
					},
			'dir' : []
		}
		
		# Build up directory list
		for dir in directories:
			project['dir'].append( dir )
			
		# Convert projectinformation to YAML
		yamldata = WpFileSystem.StructureToYaml( project )
		
		# Store projectfile
		WpFileSystem.SaveToFile( yamldata, projectfile )
		
		# Always return the path to the current project file
		return projectfile
	
	
		"""
	
	
		##
		# Splitting fullpath into easier manageable parts
		##
		fileinfo = os.path.split( projectpath )
		filepath = fileinfo[ 0 ]
		filename = fileinfo[ 1 ]
		
		##
		# Get directory list
		##
		directory = WpFileSystem.ListDirectory( projectfilespath )
	
		##
		# Convert directory to YAML
		##
		yamllist = WpFileSystem.StructureToYaml( directory )
		
		##
		# Store YAML list inside project definition file
		##
		WpFileSystem.SaveToFile( yamllist, projectpath )
		
		return {
				'fpath' 	: filepath,
				'fname'	 	: filename,
				'orig'		: projectfilespath,
				'dirlist' 	: directory
 			}
				
		"""
		
 	SaveProjectFile = WpCallable( SaveProjectFile )
	
 	
	#---------------------------------------------------------------
	# Load projectfile
	# @param string path
	# @return dictionary fileinfo
	#---------------------------------------------------------------
 	def LoadProjectFile( path ):
 		##
		# read from file
 		##
		content = WpFileSystem.ReadFromFile( path )
 		
		##
 		# convert to native format
 		##
		structure = WpFileSystem.YamlToStructure( content )
 		
		return structure
		"""
 		##
		# Creating response packet
 		##
		fileinfo = os.path.split( path )
 		filepath = fileinfo[ 0 ]
 		filename = fileinfo[ 1 ]
 		
 		return { 
 				'fpath'		: filepath,
 				'fname'		: filename,
 				'orig'		: path,
 				'dirlist'	: structure
 			}
		"""

	LoadProjectFile = WpCallable( LoadProjectFile )
	
	#---------------------------------------------------------------
	# Split file path
	# @param string path
	# @return dictionary pathinfo
	#---------------------------------------------------------------
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
			'orig'  : path
		}
		
		return retval
	
	SplitFilepath = WpCallable( SplitFilepath )
	
	#---------------------------------------------------------------
	# List directory
	# @param string path
	# @return unknown information
	#---------------------------------------------------------------
	def ListDirectory( path ):
		##
		# Traversing current directory
		##
		dirlist = os.walk( path, topdown=True )
		
		files = []
		
		tmpfilefilter = re.compile( '~' )

		for entity in dirlist:
			files.append( entity )
	
		retval = {
				'path': path,
				'files': files
			}
	
		return retval
			
	ListDirectory = WpCallable( ListDirectory )
		
	#---------------------------------------------------------------
	# Convert any structure into YAML format
	# @param mixed structure
	# @return yaml structure
	#---------------------------------------------------------------
	def StructureToYaml( structure ):
		return yaml.dump( structure )

	StructureToYaml = WpCallable( StructureToYaml )
	
	#---------------------------------------------------------------
	# Convert YAML to structure
	# @param yaml structure
	# @return mixed structure
	#---------------------------------------------------------------
	def YamlToStructure( yml ):
		return yaml.load( yml )
		
	YamlToStructure = WpCallable( YamlToStructure )
	
	#---------------------------------------------------------------
	# Save to file
	# @param string content
	# @param string filename
	# @param string writemode <optional>
	#---------------------------------------------------------------
	def SaveToFile( content, filename, mode='w' ):
		file = open( filename, mode )
		file.write( content )
		file.close()
		
		return True
		
	SaveToFile = WpCallable( SaveToFile )
	
	#---------------------------------------------------------------
	# Read from file
	# @param string path
	# @return string content
	#---------------------------------------------------------------
	def ReadFromFile( path ):
		file = open( path, 'r' )
		retval = file.read()
		file.close()
		
		return retval
		
	ReadFromFile = WpCallable( ReadFromFile )