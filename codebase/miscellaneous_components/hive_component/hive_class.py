from ...common_components.datetime_datatypes import datetime_module as DateTime
from .hivecredentials_subcomponent import hivecredentials_module as Credentials
#from .webscraper_subcomponent import webscraper_module as WebScraper
#from .astroitem_subcomponent import astroitem_module as AstroItem



class DefineHiveInterface:

	def __init__(self):

		self.credentials = Credentials.createcredentials()

		self.todaydate = DateTime.createdatefromtriplet(1, 1, 2000)

		self.hivelibrary = []

		#self.webscraper = WebScraper.createscraper(locationname, longitude, latitude, timeshift, connectionmode)

		#self.updateastrotimes(currenttimeobject)



	# def updateastrotimes(self, currenttimeobject):
	#
	# 	nowdate = currenttimeobject.getdate()
	#
	# 	if DateTime.areidentical(self.todaydate, nowdate) == False:
	#
	# 		self.astrolibrary = []
	#
	# 		self.todaydatetime = DateTime.createfromobject(nowdate)
	#
	# 		for dayshift in range(-1, 2, 1):
	#
	# 			lookupdate = self.createcustomdate(dayshift)
	#
	# 			#print("Updating Astrodata for", lookupdate.getsextuplet())
	#
	# 			for datamode in ("Day", "Nau", "Civ", "Ast"):
	#
	# 				linesfound, onestarttime, onestartvalid, oneendtime, oneendvalid, twostarttime, twostartvalid, twoendtime, twoendvalid = self.webscraper.getastrotimes(lookupdate, datamode, nowdate)
	# 				if linesfound > 0:
	# 					self.astrolibrary.append(AstroItem.createitem(datamode, onestarttime, oneendtime, lookupdate, onestartvalid, oneendvalid))
	# 					#if datamode == "Ast":
	# 						#print("Line 1:", onestarttime.gettext(), onestartvalid, oneendtime.gettext(), oneendvalid)
	# 				if linesfound > 1:
	# 					self.astrolibrary.append(AstroItem.createitem(datamode, twostarttime, twoendtime, lookupdate, twostartvalid, twoendvalid))
	# 					#if datamode == "Ast":
	# 						#print("Line 2:", twostarttime.gettext(), twostartvalid, twoendtime.gettext(), twoendvalid)
	#
	# 	#else:
	# 	#	print("Not updating sunrise/set times")
	#
	#
	#
	# def getlibrary(self):
	#
	# 	return self.astrolibrary
	#
	#
	#
	# def createcustomdate(self, dayshift):
	#
	# 	outcome = DateTime.createfromobject(self.todaydatetime)
	# 	outcome.adjustdays(dayshift)
	#
	# 	return outcome
