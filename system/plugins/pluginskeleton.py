import time

class PluginSkeleton:
	def __init__(self, command):
		self.command = command

	def run(self):
		print "This function isn't implemented correctly. Please fix."

	def printOnRun(self, commandname):
		print "[%s:START]" % (commandname)

	def printOnDone(self, commandname):
		print "[%s:DONE]\n" % (commandname)

	def printOutput(self, output):
		print "\n\t%s\n" % (output)
		
	def sleep(self, amount):
		print "\tSleeping for %.2f seconds" %(float(amount)) 
		time.sleep(float(amount))
