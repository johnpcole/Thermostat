from ....common_components.enumeration_datatype import enumeration_module as Enumeration

class DefineItem:

	def __init__(self, astrotype, starttime, endtime, istomorrow):

		self.astrotype = Enumeration.createenum(["Day", "Civ", "Nau", "Ast"], astrotype)

		self.starttime = starttime

		self.endtime = endtime

		self.tomorrowflag = istomorrow


	def gettype(self):

		return self.astrotype.displaycurrent()



	def getstarttime(self):

		return self.starttime



	def getendtime(self):

		return self.endtime



	def gettomorrow(self):

		return self.tomorrowflag
