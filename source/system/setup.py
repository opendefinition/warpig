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

    removed_database_status = False
    if( os.path.isfile( databaseName ) ):
        os.remove( databaseName )
        removed_database_status = True
        print removed_database_status
    else:
        print removed_database_status

    ## Creating database
    print "\t#2. Created database:",
    created_database_status = False
    try:
        connection = sqlite3.connect( databaseName )
        created_database_status = True
        print created_database_status
    except:
        print created_database_status

    ## Populate database
    print "\t#3. Populating database: ",
    populate_database_status = False
    try:
        file = open( setupScript, 'r' )
        script = file.read()
        file.close()

        connection.executescript( script )
        created_database_status = True
        print created_database_status
    except:
        print created_database_status

    ## Finished

    if (removed_database_status and created_database_status and created_database_status):
        print "Warpig Coding Environment has been installed. Go forth and enjoy!";
    else:
        print "Installation failed. Please check filepermissions and Sqlite3 access in folder /db"