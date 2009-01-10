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

def main(argv):
    for arg in sys.argv:
        if arg == '--update':
            # Run update engine
            print 'Running update engine.'
        else:
            # Disregard anything else and continue normal operation
            continue
    
if __name__ == "__main__":
    sys.exit( main( sys.argv ) )