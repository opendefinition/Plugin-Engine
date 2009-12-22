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
        return self.parse(file)

    ##--------------------------------------------------------------------------
    ## Parser
    ##--------------------------------------------------------------------------

    def parse(self, path):
        file = os.path.join(self.commanddir, path)
        filehandle = open(file, 'r')
        que = {}

        numcommands = 0
        sleepminutes = 0

        for command in filehandle:
            numcommands += 1
            splittedline = command.split(';')
            commanddata  = {}

            for data in splittedline:
                splitdata = data.split('=')

                if len(splitdata) > 1:
                    key = splitdata[0].strip()
                    value = splitdata[1].strip("\"")

                    commanddata[key] = value

                    if key == 'presleep' or key == 'sleep':
                        sleepminutes += int(value)

            que[commanddata['identifier']] = commanddata


        filehandle.close()

        ## Metadata
        que['metadata'] = {}
        que['metadata']['sleeptime'] = sleepminutes
        que['metadata']['file'] = path
        que['metadata']['suite'] = path[:-4]
        que['metadata']['commands'] = numcommands

        return que