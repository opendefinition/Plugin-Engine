import os

class CommandParser: 
	def __init__(self, cmdpath, filelist):
		self.cmdpath = cmdpath
		self.filelist = filelist
		self.commandque = {}
		self.commandscounter = 0

	def GetNumberOfCommands(self):
		return self.commandscounter

	def Parse(self):
		for file in self.filelist:
			path = os.path.join(self.cmdpath, file)
			
			if(os.path.isfile(path) == True):
				self.Process(path)
			else:
				continue

	def Process(self, path):
		filehandle = open(path,'r')

		for command in filehandle:
			self.commandscounter += 1

			splittedline = command.split(';')

			## Build command line data
			linedata = {}
		
			for data in splittedline:
				splitdata = data.split('=')

				if len(splitdata) > 1:
					key = splitdata[0].strip()
					value = splitdata[1].strip("\"")
					
					linedata[key] = value

			## Add command line data to processing que
			try:
				self.commandque[linedata['scheduled']].append(linedata)
			except KeyError:
				self.commandque[linedata['scheduled']] = []
				self.commandque[linedata['scheduled']].append(linedata)

			## When done reading the commands, move them to storage for safe keeping
		filehandle.close()