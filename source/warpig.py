# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Open Definition Warpig Coding Environment Loader.
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

print "Open Definition Warpig Coding Environment"
print "Copyright 2009-2011, all rights reserved"

import sys
from system.WpWarpig import WpWarPig

def main(argv):
    """
    Warpig booter
    """

    if len( argv ) > 1:
        if argv[1] == '--update':
            # Update engine
            print 'Running update engine (not implemented)'
        if argv[1] == '--setup':
            RunSetup() # a setup is basically a full reset
        if argv[1] == '--reset':
            RunSetup() # a reset is basically a new installation
    else:
        # Boot
        app = WpWarPig( 0 )
        app.MainLoop()
        
if __name__ == "__main__":
    sys.exit( main( sys.argv ) )