# -*- coding: utf-8 -*
#---------------------------------------------------------------------------
#
# Class: WpProjectData
# Desc: Class for storing simple data regarding the project.
#
#---------------------------------------------------------------------------
# Owner: Open Definition.
# Author: Roger C.B. Johnsen.
# License: Open Definiton General Lisence (ODGL). Available upon request.
#---------------------------------------------------------------------------

class WpProjectData:
    def __init__(self):
        self.__project_name = None

    def getProjectName(self):
        """
        Get projectname
        @return String Projectname
        """
        return self.__project_name

    def setProjectName(self, projectname):
        """
        Set projectname
        @param String projectname
        """
        self.__project_name = projectname