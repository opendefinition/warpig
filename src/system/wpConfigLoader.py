# -*- coding: utf-8 -*-
#=======================================================================================================================
# Load Configuration
#
# Note: This is just my ideas jotted down in a hurry
#=======================================================================================================================

import yaml

class wpConfigLoader:
    _editorConfigFilePath = None
    _systemConfigFilePath = None
    _editorConfig = None
    _systemConfig = None
    
    def __init__( self ):
        None
        
    def load( self ):
        '''
        Load configuration files
        '''
        
        if self._editorConfig is not None:
            self._editorConfig = None
            
        if self._systemConfig is not None:
            self._systemConfig = None
        
        try:
            tmpEditorCfg = open( self._editorConfigFilePath, 'r' ).read().close()
            tmpSystemCfg = open( self._systemConfigFilePath, 'r' ).read().close()
            
            # Load YAML configuration files
            self._editorConfig = yaml.load( tmpEditorCfg )  
            self._systemConfig = yaml.load( tmpSystemCfg )
        except:
            #@todo: implement an error handler for WarPig
            print "Loading configurationfiles failed."
        
t = wpConfigLoader()
t.load()
        
        