from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.datetime_datatypes import datetime_module as DateTime
from webscraper_subcomponent import webscraper_module as WebScraper
from . import astro_privatefunctions as AstroFunction
from astroitem_subcomponent import astroitem_module as AstroItem



class DefineAstro:

	def __init__(self, locationname, longitude, latitude, timeshift):

		self.todaydatetime = DateTime.createfromsextuplet(1, 1, 2000, 0, 0, 0)

		self.astrolibrary = []

		self.webscraper = WebScraper.createscraper(locationname, longitude, latitude, timeshift)



	def updateastrotimes(self):

		nowday, nowmonth, nowyear, tomday, tommonth, tomyear, differenceflag = AstroFunction.calculatedatevalues(self.todaydatetime)

		if differenceflag == True:

			self.astrolibrary = []

			self.todaydatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)

			for datamode in ("Day", "Nau", "Civ", "Ast"):

				starttime, endtime = self.webscraper.getastrotimes(nowday, nowmonth, nowyear, datamode)
				self.astrolibrary.append(AstroItem.createitem(datamode, starttime, endtime, False))

				starttime, endtime = self.webscraper.getastrotimes(tomday, tommonth, tomyear, datamode)
				self.astrolibrary.append(AstroItem.createitem(datamode, starttime, endtime, True))

		#else:
			#print "Not updating sunrise/set times"



	def getlibrary(self):

		outcome = []

		todayflag, tomorrowflag = AstroFunction.calculatefilter(self.todaydatetime)

		for item in self.astrolibrary:

			if item.gettomorrow() == False:
				if todayflag == True:
					outcome.append(item)
			else:
				if tomorrowflag == True:
					outcome.append(item)

		return outcome