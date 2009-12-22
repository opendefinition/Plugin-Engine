import os

class Command:
    def __init__(self):
        self.commanddir = "./cmd/"
        self.suites = {}
        self.loadSuites();

    ##--------------------------------------------------------------------------
    ## Retrieve command suite lists
    ##--------------------------------------------------------------------------
    def loadSuites(self):
        list = os.listdir(self.commanddir)

        for file in list:
            name = file[:-4]
            self.suites[name] = file

    ##--------------------------------------------------------------------------
    ## Retrieve mapped command suites
    ##--------------------------------------------------------------------------
    def getSuites(self):
        return self.suites

    def openSuite(self, name):
        file = self.suites[name]
        return file