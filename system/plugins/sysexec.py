import commands
from system.plugins.pluginskeleton import PluginSkeleton

class SysExecPlugin(PluginSkeleton):
	def __init__(self, command):
		PluginSkeleton.__init__(self, command)

	def run(self):
		self.printOnRun(self.command.getIdentifier())

		## Put to presleep
		if self.command.getPresleep() > 0:
			self.sleep(self.command.getPresleep())

		status = commands.getstatusoutput(self.command.getCommand())
		statuscode = status[0]
		self.printOutput(status[1])
		

		## Put to sleep after run
		if self.command.getSleep() > 0:
			self.sleep(self.command.getSleep())

		self.printOnDone(self.command.getIdentifier())		
