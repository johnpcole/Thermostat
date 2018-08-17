from ....common_components.enumeration_datatype import enumeration_module as Enumeration

class DefineItem:

	def __init__(self, astrotype, starttime, endtime, datemode, dstmode):

		self.astrotype = Enumeration.createenum(["Day", "Civ", "Nau", "Ast"], astrotype)

		self.starttime = starttime

		self.endtime = endtime

		self.datemode = Enumeration.createenum(["Yesterday", "Today", "Tomorrow"], datemode)

		self.daylightsavings = dstmode


	def gettype(self):

		return self.astrotype.displaycurrent()



	def getstarttime(self):

		return self.starttime



	def getendtime(self):

		return self.endtime



	def getdate(self):

		return self.datemode.displaycurrent()



	def getdst(self):

		return self.daylightsavings