##------------------------------------------------------------
## Command Representation Class
##------------------------------------------------------------
class Command:
	def __init__(self):
		self.identifier = None
		self.command = None
		self.presleep = 0
		self.sleep = 0
		self.plugin = None
		self.outputplugin = None
		

	## Set identifer
	def setIdentifier(self, identifier):
		self.identifier = identifier
		return self

	## Get identifier
	def getIdentifier(self):
		return self.identifier

	## Set command
	def setCommand(self, command):
		self.command = command 
		return self

	## Get command
	def getCommand(self):
		return self.command

	## Set presleep
	def setPresleep(self, amount):
		self.presleep = amount
		return self

	## Get presleep
	def getPresleep(self):
		return self.presleep

	## Set sleep
	def setSleep(self, amount):
		self.sleep = amount
		return self

	## Get Sleep
	def getSleep(self):
		return self.sleep

	## Set plugin
	def setPlugin(self, plugin):
		self.plugin = plugin
		return self

	## Get plugin
	def getPlugin(self):
		return self.plugin

	## Set output plugin
	def setOutputPlugin(self, plugin):
		self.outputplugin = plugin
		return self

	## Get output plugin
	def getOutputPlugin(self):
		return self.outputplugin
	
