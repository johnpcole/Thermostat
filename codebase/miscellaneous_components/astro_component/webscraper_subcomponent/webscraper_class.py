from urllib2 import urlopen as GetWebPage
from urllib2 import Request as GenerateWebRequest
from urllib2 import URLError as WebError
from ....common_components.clock_datatype import clock_module as Clock
from ....common_components.datetime_datatypes import datetime_module as DateTime
from ....common_components.datetime_datatypes import duration_module as Duration


class DefineScraper:

	def __init__(self, locationname, longitude, latitude, timeshift):

		self.location = locationname   # Bristol+(UK)

		self.longitude = longitude     # -2.570310

		self.latitude = latitude       # 51.497772

		self.lonsig, self.londeg, self.lonmin = self.preparelocation(longitude)

		self.latsig, self.latdeg, self.latmin = self.preparelocation(latitude)

		self.timeshift = timeshift

		self.webcalltries = 10

		self.resultagebuffer = Duration.createfromvalues(5, "Days")

		self.lastsuccessfulwebcall = DateTime.createfromsextuplet(1, 1, 2000, 0, 0, 0)

		self.lastsuccessfulyear = -9999

		self.lastwebresult = ""



	def getsuntimes(self, day, month, year):

		sunrise = Clock.createasinteger(0)
		sunset = Clock.createasinteger(0)

		self.retrievewebpage(year)

		if self.lastwebresult != "":

			desiredlinestart = str(day) + "  "
			if day < 10:
				desiredlinestart = "0" + desiredlinestart

			for dataline in self.lastwebresult:
				if dataline[:4] == desiredlinestart:

					index = (month * 11) - 7
					sunrise = self.sanitisetime(dataline[(index + 0):(index + 4)])
					sunset = self.sanitisetime(dataline[(index + 5):(index + 9)])

		else:
			print "Could not extract Sunrise/Sunset times from internet scrape"

		return sunrise, sunset



	def retrievewebpage(self, specifiedyear):

		tries = 0

		currentdatetime = DateTime.getnow()
		timesincelastupdate = DateTime.secondsdifference(self.lastsuccessfulwebcall, currentdatetime)

		if (specifiedyear != self.lastsuccessfulyear) or (Duration.iswithinlimit(timesincelastupdate, self.resultagebuffer) == False):

			url = self.buildurl(specifiedyear)
			webresponse = ""

			while tries < self.webcalltries:
				try:
					webrequest = GenerateWebRequest(url)
					webresponse = GetWebPage(webrequest).read(20000)
					tries = 99999
				except WebError as errorobject:
					tries = tries + 1
					#print "Error accessing website: ", errorobject.reason

			if tries == 99999:
				print "Access to website data Succeeded"
				self.lastwebresult = webresponse.split("\n")
				self.lastsuccessfulwebcall = DateTime.createfromobject(currentdatetime)
				self.lastsuccessfulyear = specifiedyear
			else:
				print "Access to website data Failed"

		else:
			print "Relying on local cached data (Still fresh)"



	def sanitisetime(self, textstring):

		hour = textstring[0:2]
		min = textstring[2:4]
		# Doesn't cope with //// or ==== results indicating permanent above/below limits
		try:
			hourvalue = int(hour)
			minvalue = int(min)
		except:
			hourvalue = 0
			minvalue = 0
			print "Problems reading sunrise/sunset time: ", textstring

		return Clock.createastime(hourvalue, minvalue, 0)



	def preparelocation(self, decimallocation):

		if decimallocation < 0.0:
			sign = -1
		else:
			sign = 1

		location = abs(decimallocation)

		degs = int(location)

		mins = int((location - float(degs)) * 60.0)

		return sign, degs, mins



	def buildurl(self, year):

		datamode = 0 # for sunrise/set
		# datamode = 1 # for moonrise/set
		# datamode = 2 # for civil
		# datamode = 3 # for nautical
		# datamode = 4 # for astro

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
		url = url + "&tz=&tz_sign=-1"

		return url


