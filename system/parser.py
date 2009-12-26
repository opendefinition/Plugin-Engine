import os
from system.command import Command

class Parser:
	def __init__(self):
		## Location of stored commands
		self.cmddir = './commands/'

		## Suite filename
		self.suite = None

		## List of registered commands
		self.registry = []

		## Metadata total estimated runtime
		self.runtime = 0.0

	## Register command suire
	def registerSuite(self, name):
		self.suite = name
		return self

	## Parse command suite
	def parse(self):
		path = os.path.join(self.cmddir, self.suite) 
		filehandle = open(path, 'r')
		
		for command in filehandle:
			semicolonsplit = command.split(';')
			command = Command()
	
			for entity in semicolonsplit:
				data = entity.strip().split("=")
				
				if len(data) > 1:
					key = data[0].strip()
					val = data[1].strip("'")

					if key == 'identifier':
						command.setIdentifier(val)
					elif key == 'command':
						command.setCommand(val)
					elif key == 'presleep':
						self.runtime += float(val)
						command.setPresleep(val)
					elif key == 'sleep':
						self.runtime += float(val)
						command.setSleep(val)
					elif key == 'plugin':
						command.setPlugin(val)
					elif key == 'outputplugin':
						command.setOutputPlugin(val)
			
			## Add command to registry
			self.registry.append(command)

		filehandle.close()

		## Return parsed command list (the registry)
		return self.registry
		
