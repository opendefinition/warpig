import os.path
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
import shutil
import yaml

class WpFileSystem:
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

        #--------------------------------------------------------------
        # Delete file or directory
        # @param string path
        #--------------------------------------------------------------
        @staticmethod
        def DeleteFromDisk( path ):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

        #--------------------------------------------------------------
        # Rename file or directory
        # @param string path
        #--------------------------------------------------------------
        @staticmethod
        def Rename( data, newname ):
            if data.getCurrentFilename() == None:
                split = os.path.split(data.getCurrentDirectory())
                new = os.path.join(split[0], newname)
                orig = data.getCurrentDirectory()
            else:
                orig = data.getCurrentFile()
                new = os.path.join(data.getCurrentDirectory(), newname)

            os.rename(orig, new)