from ....common_components.enumeration_datatype import enumeration_module as Enumeration

class DefineItem:

	def __init__(self, astrotype, starttime, endtime, dateobject, startvalidity, endvalidity):

		self.astrotype = Enumeration.createenum(["Day", "Civ", "Nau", "Ast"], astrotype)

		self.starttime = starttime

		self.endtime = endtime

		self.date = dateobject

		self.startvalid = startvalidity

		self.endvalid = endvalidity



	def gettype(self):

		return self.astrotype.displaycurrent()



	def getstarttime(self):

		return self.starttime



	def getendtime(self):

		return self.endtime



	def getdate(self):

		return self.date



	def getstartvalidity(self):

		return self.startvalid



	def getendvalidity(self):

		return self.endvalid
