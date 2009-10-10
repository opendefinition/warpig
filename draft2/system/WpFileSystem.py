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

class WpFileSystem:
	#---------------------------------------------------------------
	# Save project file
	# @param string projectpath
	# @param string projectfilespath
	# @return dictionary fileinfo
	#---------------------------------------------------------------
	@staticmethod
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

	#---------------------------------------------------------------
	# Load projectfile
	# @param string path
	# @return dictionary fileinfo
	#---------------------------------------------------------------
	@staticmethod
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
	
	#---------------------------------------------------------------
	# Split file path
	# @param string path
	# @return dictionary pathinfo
	#---------------------------------------------------------------
	@staticmethod
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
	
	#---------------------------------------------------------------
	# List directory
	# @param string path
	# @return unknown information
	#---------------------------------------------------------------
	@staticmethod
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
		
	#---------------------------------------------------------------
	# Convert any structure into YAML format
	# @param mixed structure
	# @return yaml structure
	#---------------------------------------------------------------
	@staticmethod
	def StructureToYaml( structure ):
		return yaml.dump( structure )
	
	#---------------------------------------------------------------
	# Convert YAML to structure
	# @param yaml structure
	# @return mixed structure
	#---------------------------------------------------------------
	@staticmethod
	def YamlToStructure( yml ):
		return yaml.load( yml )
		
	#---------------------------------------------------------------
	# Save to file
	# @param string content
	# @param string filename
	# @param string writemode <optional>
	#---------------------------------------------------------------
	@staticmethod
	def SaveToFile( content, filename, mode='w' ):
                if filename != None:
                    file = open( filename, mode )
                    file.write( content )
                    file.close()
                    return True
                else:
                    return False
		
	#---------------------------------------------------------------
	# Read from file
	# @param string path
	# @return string content
	#---------------------------------------------------------------
	@staticmethod
	def ReadFromFile( path ):
		file = open( path, 'r' )
		retval = file.read()
		file.close()
		
		return retval