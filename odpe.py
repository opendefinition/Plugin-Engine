import os
import sys
from system.plugins.sysexec import SysExecPlugin
from system.parser import Parser

class Application:
	def __init__(self):
		self.parser = Parser()
		self.suites = []

	def loadMenu(self):
		print "Suites"

		cmddir = './commands/'
		list = os.listdir(cmddir)

		counter = 0;
		for item in list:
			counter += 1
			self.suites.append(item)
			print " %i. %s" %(counter, item[:-4])
	
		try:
			## Picking suite from menu
			suitenum = int(raw_input("\nsuite #  "))

			## Running desired suite
			self.printSeparator()
			self.run(self.suites[(suitenum-1)])
		except: 
			sys.exit("Menu choice invalid")		

	def run(self, suitename):
		commands = self.parser.registerSuite(suitename).parse()
		
		for command in commands:
			plugin = None

			if command.getPlugin() == 'sysexec':
				plugin = SysExecPlugin(command)

			if plugin != None:
				plugin.run()
			else:
				sys.exit()

	def printHeader(self):
		os.system('clear')
		print "Open Definition :: Plugin Engine, V0.1"
		self.printSeparator()

	def printSeparator(self):
		sep = ''
		for i in range(0, 80):
			sep += '-'

		print sep
driver = Application()
driver.printHeader()
driver.loadMenu()
