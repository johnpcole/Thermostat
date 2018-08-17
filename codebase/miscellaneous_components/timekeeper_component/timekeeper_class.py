from ...common_components.clock_datatype import clock_module as Clock



class DefineTimekeeper:

	def __init__(self):

		self.currenttime = Clock.getnow()

		self.previoustime = Clock.getnow()

		self.cyclemeasure = 0




	def update(self):

		self.cyclemeasure = self.cyclemeasure + 1
		#self.currenttime = Clock.createastime(20, 30, 0)
		self.currenttime = Clock.getnow()

		if Clock.isequal(self.currenttime, self.previoustime) == False:
			#print "Cycles last second =", self.cyclemeasure
			self.cyclemeasure = 0
			self.previoustime = Clock.createasclock(self.currenttime)


	def getclock(self):

		return Clock.createastime(self.currenttime.gethour(), self.currenttime.getminute(), 0)



	def getaccurateclock(self):

		return self.currenttime