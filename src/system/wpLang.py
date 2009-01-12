# -*- coding: utf-8 -*-
import yaml

class wpLang:
    _strings = None
    
    def __init__( self ):
        self.loadLanguage( 'en-gb' )
    
    def loadLanguage(self, language ):
        '''
        Load language file
        @param string language
        '''
        self._strings = yaml.load( open( './lang/en-gb.lang', 'r' ).read().close() )        
    
    def getString(self, string ):
        '''
        Load language string
        @param string string
        @return string
        '''
        return string[ string ]