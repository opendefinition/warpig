# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpConfigSystem
# Desc: 
# 	Borg pattern implementation.
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

class WpConfigSystem:
    __shared_state  = {}

    def __init__(self):
        self.__dict__ = self.__shared_state