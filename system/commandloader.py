from system.commandparser import CommandParser
import os

class CommandLoader:
	def __init__(self):
		self.commanddir = './cmd/';
		self.numcmdfiles = 0
		self.commands = 0
		self.cmdque = {}

	def Load(self):
		filelist = os.listdir(self.commanddir)
			
		self.numcmdfiles = len(filelist)

		test = CommandParser(self.commanddir, filelist)
		test.Parse()

		self.cmdque = test.commandque

		self.numcmds = test.commandscounter
		