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

		self.lastsuccessfulwebcall = DateTime.createdatefromtriplet(1, 1, 2000)

		self.lastsuccessfulyear = -9999

		self.lastresult = {}
		self.lastresult["Day"] = ""
		self.lastresult["Nau"] = ""
		self.lastresult["Civ"] = ""
		self.lastresult["Ast"] = ""



	def getastrotimes(self, lookupdateobject, datamode, nowdateobject):

		linesfound = 0
		rowvalidity, onestarttime, onestartvalid, oneendtime, oneendvalid = ScraperFunction.extracttimings("            ", 1)
		rowvalidity, twostarttime, twostartvalid, twoendtime, twoendvalid = ScraperFunction.extracttimings("            ", 1)

		lookupday, lookupmonth, lookupyear = lookupdateobject.getdatetriplet()

		# Only download the pages if the current ones are out of date
		# or for the wrong year
		if self.calculaterefresh(lookupyear, nowdateobject):
			self.retrievewebpages(lookupyear, nowdateobject)

		if self.lastresult[datamode] != "":

			desiredlinestart, desiredcolumn = ScraperFunction.getindexes(lookupday, lookupmonth)

			for dataline in self.lastresult[datamode]:
				if dataline[:4] == desiredlinestart:
					rowvalidity, starttime, startvalidity, endtime, endvalidity = ScraperFunction.extracttimings(dataline, desiredcolumn)
					if rowvalidity == True:
						linesfound = linesfound + 1
						if linesfound == 1:
							onestarttime = starttime
							onestartvalid = startvalidity
							oneendtime = endtime
							oneendvalid = endvalidity
						elif linesfound == 2:
							twostarttime = starttime
							twostartvalid = startvalidity
							twoendtime = oneendtime
							twoendvalid = oneendvalid
							oneendtime = endtime
							oneendvalid = endvalidity
						else:
							print "Too many data rows found on website"
							x = 1/0

		return linesfound, onestarttime, onestartvalid, oneendtime, oneendvalid, twostarttime, twostartvalid, twoendtime, twoendvalid



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
					if self.connectionmode == True:
						webresponse[datamode] = GetWebPage(webrequest).read(20000)
					else:
						webresponse[datamode] = ScraperFunction.generatedummydata(datamode)
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
