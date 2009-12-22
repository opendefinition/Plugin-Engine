from system.commandloader import CommandLoader
import commands
import os
import sys
import time

##------------------------------------------------------------------------------------------------------------------------------------------------------------
## Helper functions
##------------------------------------------------------------------------------------------------------------------------------------------------------------

def printStatus(statusmessage):
	print "\tStatus:\t%s" % (statusmessage)

def printSeparator():
	separator = '';

	for i in range(0,80):
		separator += '_'

	print separator

def clearScreen():
	os.system('clear')

##------------------------------------------------------------------------------------------------------------------------------------------------------------
## RUN
##------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
	clearScreen()
	print 'Open Definition Plugin Engine'
	printSeparator()
	printStatus('Loading commands')

	cmdloader = CommandLoader()
	cmdloader.Load()

	printStatus("Loaded %i commands in %i file(s)" %(cmdloader.numcmds, cmdloader.numcmdfiles))
	printSeparator()

	for entry in cmdloader.cmdque:
		for cmd in cmdloader.cmdque[entry]:
			print "Running command: %s" % (cmd['identifier'])
			
			status = commands.getstatusoutput(cmd['command'])
			print "\tOutput:\n\t%s" %(str(status[1]))
			
			if int(cmd['sleep']) > 0:
				print "\tPlease wait while I sleep for %s seconds" %(cmd['sleep'])
				time.sleep(int(cmd['sleep']))
			
			print "\n"

	printSeparator()
	print '.. Done'
except KeyboardInterrupt:
	print "User halted execution of commands"
	
