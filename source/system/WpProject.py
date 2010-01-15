class WpProject:
    def __init__(self):
        self.id     = None
        self.title  = None
        self.datecreated = None
        self.description = None
        self.paths = []

    def SetId(self, id):
        """
        Set current project id
        """
        self.id = int(id)

    def GetId(self):
        """
        Get current project id
        """
        return int(self.id)

    def SetTitle(self, title):
        """
        Set current project id
        """
        self.title = str(title)

    def GetTitle(self):
        """
        Get current project title
        """
        return str(self.title)

    def AddPath(self, path):
        """
        Add associated project file path
        """
        self.paths.append(str(path))
        self.paths.sort()

    def GetPaths(self):
        """
        Get associated project file paths
        """
        return self.paths

    def SetDateCreated(self, date):
        """
        Set which date this project was created on
        """
        self.datecreated = str(date)

    def GetDateCreated(self):
        """
        Get which date this project was created on
        """
        return str(self.datecreated)

    def SetDescription(self, description):
        """
        Set decription for this project
        """
        self.description = str(description)

    def GetDescription(self):
        """
        Get description for this project
        """
        return str(self.description)