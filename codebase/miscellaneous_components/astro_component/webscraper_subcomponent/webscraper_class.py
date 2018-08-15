#from urllib2 import urlopen as GetWebPage
#from urllib2 import Request as GenerateWebRequest
#from urllib2 import URLError as WebError
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
			print "Could not access Sunrise/Sunset times from internet"

		return sunrise, sunset



	def retrievewebpage(self, specifiedyear):

		tries = 0

		currentdatetime = DateTime.getnow()
		timesincelastupdate = DateTime.secondsdifference(self.lastsuccessfulwebcall, currentdatetime)

		if (specifiedyear != self.lastsuccessfulyear) or (Duration.iswithinlimit(timesincelastupdate, self.resultagebuffer) == False):

			url = self.buildurl(specifiedyear)

			while tries < self.webcalltries:
				try:
					#webrequest = GenerateWebRequest(r'file:///C:/tester.html')
					#webresponse = GetWebPage(webrequest).read(20000)
					#astrorawdata = webresponse.split("\n")
					tries = tries + 1
					#print "Attempting data mocking, ", tries, " of ", self.webcalltries
					meteorawdata = []
					meteorawdata.append("01  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("02  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("03  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("04  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("05  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("06  0757 1649  0702 1745  0600 1833  0452 1925  0405 2011  0355 2031  0425 2008  0513 1910  0603 1800  0653 1655  0746 1609  0815 1606")
					meteorawdata.append("07  0756 1651  0700 1747  0557 1835  0450 1927  0404 2012  0355 2031  0427 2006  0515 1908  0604 1757  0655 1653  0747 1608  0815 1607")
					meteorawdata.append("08  0754 1653  0658 1749  0555 1837  0448 1928  0403 2013  0356 2031  0428 2005  0516 1906  0606 1755  0656 1651  0749 1607  0816 1608")
					meteorawdata.append("09  0754 1653  0658 1749  0555 1837  0448 1928  0403 2013  0356 2031  0428 2005  0516 1906  0606 1755  0656 1651  0749 1607  0816 1608")
					meteorawdata.append("10  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("11  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("12  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("13  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("14  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("15  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("16  0757 1649  0702 1745  0600 1833  0452 1925  0405 2011  0355 2031  0425 2008  0513 1910  0603 1800  0653 1655  0746 1609  0815 1606")
					meteorawdata.append("17  0756 1651  0700 1747  0557 1835  0450 1927  0404 2012  0355 2031  0427 2006  0515 1908  0604 1757  0655 1653  0747 1608  0815 1607")
					meteorawdata.append("18  0754 1653  0658 1749  0555 1837  0448 1928  0403 2013  0356 2031  0428 2005  0516 1906  0606 1755  0656 1651  0749 1607  0816 1608")
					meteorawdata.append("19  0754 1653  0658 1749  0555 1837  0448 1928  0403 2013  0356 2031  0428 2005  0516 1906  0606 1755  0656 1651  0749 1607  0816 1608")
					meteorawdata.append("20  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("21  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("22  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("23  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("24  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("25  0758 1647  0704 1743  0602 1832  0454 1923  0406 2009  0354 2031  0424 2009  0512 1912  0601 1802  0651 1657  0744 1610  0815 1606")
					meteorawdata.append("26  0757 1649  0702 1745  0600 1833  0452 1925  0405 2011  0355 2031  0425 2008  0513 1910  0603 1800  0653 1655  0746 1609  0815 1606")
					meteorawdata.append("27  0756 1651  0700 1747  0557 1835  0450 1927  0404 2012  0355 2031  0427 2006  0515 1908  0604 1757  0655 1653  0747 1608  0815 1607")
					meteorawdata.append("28  0754 1653  0658 1749  0555 1837  0448 1928  0403 2013  0356 2031  0428 2005  0516 1906  0606 1755  0656 1651  0749 1607  0816 1608")
					meteorawdata.append("29  0753 1654             0553 1838  0446 1930  0402 2014  0356 2031  0429 2003  0518 1903  0607 1753  0658 1649  0750 1606  0816 1609")
					meteorawdata.append("30  0752 1656             0551 1840  0444 1932  0401 2016  0357 2031  0431 2002  0519 1901  0609 1751  0700 1647  0752 1606  0816 1610")
					meteorawdata.append("31  0750 1658             0548 1842             0400 2017             0432 2000  0521 1859             0702 1645             0816 1611")
					tries = 99999
				except:
					print "Failed to mock data"
				#except WebError as errorobject:
					#print errorobject.reason

			if tries == 99999:
				print "Webcall Success"
				self.lastwebresult = meteorawdata # astrodata
				self.lastsuccessfulwebcall = DateTime.createfromobject(currentdatetime)
				self.lastsuccessfulyear = specifiedyear
			else:
				print "Webcall Failed"

		else:
			print "Relying on local cached data"



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


