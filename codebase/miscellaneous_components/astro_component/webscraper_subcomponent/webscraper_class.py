from urllib2 import urlopen as GetWebPage
from urllib2 import Request as GenerateWebRequest
from urllib2 import URLError as WebError
from ....common_components.datetime_datatypes import datetime_module as DateTime
from ....common_components.datetime_datatypes import duration_module as Duration
from . import webscraper_privatefunctions as ScraperFunction

class DefineScraper:

	def __init__(self, locationname, longitude, latitude, timeshift, connectionmode):

		self.connectionmode = connectionmode

		self.location = locationname   # Bristol+(UK)

		self.longitude = longitude     # -2.570310

		self.latitude = latitude       # 51.497772

		self.lonsig, self.londeg, self.lonmin = ScraperFunction.preparelocation(longitude)

		self.latsig, self.latdeg, self.latmin = ScraperFunction.preparelocation(latitude)

		self.timeshift = timeshift

		self.webcalltries = 10

		self.resultagebuffer = Duration.createfromvalues(5, "Days")

		self.lastsuccessfulwebcall = DateTime.createfromsextuplet(1, 1, 2000, 0, 0, 0)

		self.lastsuccessfulyear = -9999

		self.lastresult = {}
		self.lastresult["Day"] = ""
		self.lastresult["Nau"] = ""
		self.lastresult["Civ"] = ""
		self.lastresult["Ast"] = ""



	def getastrotimes(self, lookupdateobject, datamode, nowdateobject):

		lookupday, lookupmonth, lookupyear, dummy1, dummy2, dummy3 = lookupdateobject.getsextuplet()

		if self.connectionmode == False:
			starttime, startvalidity, endtime, endvalidity = ScraperFunction.generatedummydata(lookupday, datamode)

		else:
			starttext = "----"
			endtext = "----"

			# Only download the pages if the current ones are out of date
			# or for the wrong year
			if self.calculaterefresh(lookupyear, nowdateobject):
				self.retrievewebpages(lookupyear, nowdateobject)

			if self.lastresult[datamode] != "":

				linefound = False
				desiredlinestart = str(lookupday) + "  "
				if lookupday < 10:
					desiredlinestart = "0" + desiredlinestart

				for dataline in self.lastresult[datamode]:
					if (dataline[:4] == desiredlinestart) and (linefound == False):

						index = (lookupmonth * 11) - 7
						starttext = dataline[(index + 0):(index + 4)]
						endtext = dataline[(index + 5):(index + 9)]
						linefound = True

			starttime, startvalidity = ScraperFunction.sanitisetime(starttext, "Start")
			endtime, endvalidity = ScraperFunction.sanitisetime(endtext, "End")

		return starttime, startvalidity, endtime, endvalidity



	def retrievewebpages(self, specifiedyear, currentdateobject):

		tries = 0

		print "Downloading data for:", specifiedyear

		while tries < self.webcalltries:
			try:
				webresponse = {}
				for datamode in ("Day", "Nau", "Civ", "Ast"):
					webresponse[datamode] = ""
					url = self.buildurl(specifiedyear, datamode)
					webrequest = GenerateWebRequest(url)
					webresponse[datamode] = GetWebPage(webrequest).read(20000)
					tries = 99999
			except WebError as errorobject:
				tries = tries + 1
				print "Error accessing website: ", errorobject.reason

		if tries == 99999:
			#print "Access to website data Succeeded"
			for datamode in ("Day", "Nau", "Civ", "Ast"):
				self.lastresult[datamode] = webresponse[datamode].split("\n")
			self.lastsuccessfulwebcall = DateTime.createfromobject(currentdateobject)
			self.lastsuccessfulyear = specifiedyear
		else:
			print "Access to website data Failed"



	def buildurl(self, year, mode):

		if mode == "Day":
			datamode = 0 # for sunrise/set
		# datamode = 1 # for moonrise/set
		elif mode == "Civ":
			datamode = 2 # for civil
		elif mode == "Nau":
			datamode = 3 # for nautical
		elif mode == "Ast":
			datamode = 4 # for astro
		else:
			datamode = 1/0

		url = "http://aa.usno.navy.mil/cgi-bin/aa_rstablew.pl?ID=AA"
		url = url + "&year=" + str(year)
		url = url + "&task=" + str(datamode)
		url = url + "&place=" + self.location
		url = url + "&lon_sign=" + str(self.lonsig)
		url = url + "&lon_deg=" + str(self.londeg)
		url = url + "&lon_min=" + str(self.lonmin)
		url = url + "&lat_sign=" + str(self.latsig)
		url = url + "&lat_deg=" + str(self.latdeg)
		url = url + "&lat_min=" + str(self.latmin)
		url = url + "&tz=0"
		url = url + "&tz_sign=1"
		if mode == "Ast":
			print url
		return url



	def calculaterefresh(self, specifiedyear, currentdatetime):

		timesincelastupdate = DateTime.secondsdifference(self.lastsuccessfulwebcall, currentdatetime)

		outcome = False

		if specifiedyear != self.lastsuccessfulyear:
			outcome = True
		else:
			if Duration.iswithinlimit(timesincelastupdate, self.resultagebuffer) == False:
				outcome = True

		return outcome