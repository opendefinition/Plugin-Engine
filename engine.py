import sys

from gui.application import Application

def boot():
    application = Application(0)
    application.MainLoop()

if __name__ == '__main__':
    sys.exit(boot())