from ...common_components.datetime_datatypes import datetime_module as DateTime
from .hivecredentials_subcomponent import hivecredentials_module as Credentials
#from .webscraper_subcomponent import webscraper_module as WebScraper
#from .astroitem_subcomponent import astroitem_module as AstroItem
from urllib.parse import urlencode as DataEncoder
from urllib.request import urlopen as GetWebPage
from urllib.request import Request as GenerateWebRequest
from urllib.request import URLError as WebError



class DefineHiveInterface:

	def __init__(self):

		self.credentials = Credentials.createcredentials()

		self.todaydate = DateTime.createdatefromtriplet(1, 1, 2000)

		self.hivelibrary = []

		self.body = '{ "sessions": [{ "username": ' + self.credentials.getusername() + ', "password": ' + self.credentials.getpassword() + ', "caller": "WEB"}] }'

		self.urlendpointroot = "https://api-prod.bgchprod.info:443/omnia"

		testeroutput = self.interactwithhive(self.body, "/auth/sessions")

		print("\\/=======================================\\/")
		print(testeroutput.read())
		print("/\\=======================================/\\")


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


	def interactwithhive(self, requestdata, endpoint):

		fullurlendpoint = self.urlendpointroot + endpoint

		webrequest = GenerateWebRequest(fullurlendpoint, data=requestdata.encode('ascii', 'ignore'))
		webrequest.add_header('Content-Type', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('Accept', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('X-Omnia-Client', 'Hive Web Dashboard')
		outcome = GetWebPage(webrequest)

		return outcome