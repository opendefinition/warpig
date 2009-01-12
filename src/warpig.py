# -*- coding: utf-8 -*-
#=======================================================================================================================
#
# WarPig main file 
# Date: 2009-01-10
#
# @author: Roger C.B. Johnsen
# @contact: johnsen@opendefinition.com
# @license: LPGL
# @organization: Open Definition
#
# usage: 
#    python warpig    >    Launches WarPig
#    python warpog --update > update WarPig (non-gui)
#
#=======================================================================================================================
import sys

from gui.wpWarPig import wpWarPig

def main(argv):
    if len( argv ) > 1:
        if argv[1] == '--update':
            # Run update engine
            print 'Running update engine'
    else:
        # Disregard anything else and continue normal operation
        app = wpWarPig( 0 )
        app.MainLoop()
        
if __name__ == "__main__":
    sys.exit( main( sys.argv ) )