# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpDatabase
# Desc: 
# 	Database connection class
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------


from sqlite3 import *

class WpDatabase():
	def __init__( self ):
		self.dbName = './db/warpig.db'
	
	def __Open( self ):
		"""
		Open Database Connection
		@return Boolean status
		"""
		try:
			self.connection = connect( self.dbName )
			self.cursor = self.connection.cursor()
			
			return True
		except:
			return False
			
	def __Close( self ):
		"""
		Close Database Connection
		@return Boolean status
		"""
		try:
			self.connection.close()
			return True
		except:
			return False
			
	def Insert( self, querystring ):
		"""
		Run insert SQL query
		"""
		retval = False
		
		self.__Open()
		
		try:
			self.cursor.execute( querystring )
			self.connection.commit()
			retval = True
		except IntegrityError:
			self.connection.rollback()
		finally:
			self.__Close()
			
		return retval
		
	def Select( self, querystring ):
		retval = False
		
		self.__Open()
		
		self.cursor.execute( querystring )
		self.connection.commit()
		retval = self.cursor.fetchall()
		
		self.__Close()
		
		return retval

	def RunSqlScript( self, path ):
		self.__Open()
		self.connection.executescript(path)
	
		