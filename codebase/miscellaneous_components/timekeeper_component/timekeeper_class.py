from ...common_components.datetime_datatypes import clock_module as Clock
from ...common_components.datetime_datatypes import datetime_module as DateTime



class DefineTimekeeper:

	def __init__(self):

		self.currenttime = Clock.getnow()

		self.previoustime = Clock.getnow()

		day, month, year = DateTime.getnow().getdatetriplet()
		self.currentdate = DateTime.createdatefromtriplet(day, month, year)

		self.cyclemeasure = 0



	def update(self):

		self.cyclemeasure = self.cyclemeasure + 1

		#pretendclockvalue = Clock.getnow().getvalue() * 60 * 3
		#tempvalue = pretendclockvalue % (24 * 60 * 60)
		#self.currenttime = Clock.createasinteger(tempvalue)
		self.currenttime = Clock.getnow()
		#self.currenttime = Clock.createastime(20, 30, 0)

		if Clock.isequal(self.currenttime, self.previoustime) == False:
			#print("Cycles last second =", self.cyclemeasure)
			self.cyclemeasure = 0
			self.previoustime = Clock.createasclock(self.currenttime)

		day, month, year = DateTime.getnow().getdatetriplet()
		self.currentdate = DateTime.createdatefromtriplet(day, month, year)



	def getclock(self):

		return Clock.createastime(self.currenttime.gethour(), self.currenttime.getminute(), 0)



	def getaccurateclock(self):

		return self.currenttime



	def gethourlyalarm(self, minutespasthour):

		outcome = False
		if self.currenttime.getminute() == minutespasthour:
			if self.cyclemeasure == 0:
				outcome = True

		return outcome



	def getdailyalarm(self, hoursintoday, minutespasthour):

		outcome = False
		if self.currenttime.gethour() == hoursintoday:
			if self.currenttime.getminute() == minutespasthour:
				if self.cyclemeasure == 0:
					outcome = True

		return outcome



	def getdate(self):

		return self.currentdate


#	def getdateitems(self):
#
#		day, month, year, dummy1, dummy2, dummy3 = self.currentdate.getsextuplet()
#
#	return day, month, year
