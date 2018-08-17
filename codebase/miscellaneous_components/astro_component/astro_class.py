from ...common_components.datetime_datatypes import datetime_module as DateTime
from webscraper_subcomponent import webscraper_module as WebScraper
from astroitem_subcomponent import astroitem_module as AstroItem



class DefineAstro:

	def __init__(self, locationname, longitude, latitude, timeshift, connectionmode, currenttimeobject):

		self.todaydatetime = DateTime.createfromsextuplet(1, 1, 2000, 0, 0, 0)

		self.astrolibrary = []

		self.webscraper = WebScraper.createscraper(locationname, longitude, latitude, timeshift, connectionmode)

		#self.updateastrotimes(currenttimeobject)



	def updateastrotimes(self, currenttimeobject):

		nowdate = currenttimeobject.getdate()

		if DateTime.areidentical(self.todaydatetime, nowdate) == False:

			self.astrolibrary = []

			self.todaydatetime = DateTime.createfromobject(nowdate)

			for dayshift in range(0, 2, 1):   #  range(-1, 2, 1):

				lookupdate = DateTime.createfromobject(self.todaydatetime)
				lookupdate.adjustdays(dayshift)

				print "Updating Astrodata for", lookupdate.getsextuplet()

				for datamode in ("Day", "Nau", "Civ", "Ast"):

					starttime, startvalidity, endtime, endvalidity = self.webscraper.getastrotimes(lookupdate, datamode, nowdate)
					self.astrolibrary.append(AstroItem.createitem(datamode, starttime, endtime, lookupdate, startvalidity, endvalidity))
					if datamode == "Ast":
						print starttime.gettext(), startvalidity, endtime.gettext(), endvalidity


		#else:
			#print "Not updating sunrise/set times"



	def getlibrary(self):

		return self.astrolibrary

