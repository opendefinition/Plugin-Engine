import os

class Command:
    def __init__(self):
        self.commanddir = "./cmd/"
        self.commandfiles = []

        self.loadSuites();

    def loadSuites(self):
        self.commandfiles = os.listdir(self.commanddir)

    def getCommandSuites(self):
        return self.commandfiles
