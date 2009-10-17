import os

import sqlite3
from system.WpDatabaseAPI import WpDatabaseAPI

def RunSetup():
	## Setup variables
	databaseName = './db/warpig.db'
	setupScript = './db/sql/default-system.sql'
	
	## Heading
	print "Open Definition Warpig Setup Tool\n"
	print "Status:"
	
	## If the database is already present, delete it
	print "\t#1. Removing old database:",
	
	if( os.path.isfile( databaseName ) ):
		os.remove( databaseName )
		print True
	else:
		print False
		
	## Creating database
	print "\t#2. Created database:",
	
	try:
		connection = sqlite3.connect( databaseName )
		print True
	except:
		print False
		
	## Populate database
	print "\t#3. Populating database: ",
	
	try:
		file = open( setupScript, 'r' )
		script = file.read()
		file.close()
	
		connection.executescript( script )
		print True
	except:
		print False
		
	## Finished
	print "Warpig Coding Environment has been installed. Go forth and enjoy!";
