from urllib import urlretrieve as GetWebPage

class DefineMeteo:

	def __init__(self, locationname, longitude, latitude, timeshift):

		self.location = locationname   # Bristol+(UK)

		self.longitude = longitude     # -2.570310

		self.latitude = latitude       # 51.497772

		self.lonsig, self.londeg, self.lonmin = self.preparelocation(longitude)

		self.latsig, self.latdeg, self.latmin = self.preparelocation(latitude)

		self.timeshift = timeshift


	def getsuntimes(self, day, month, year):

		url = "http://aa.usno.navy.mil/cgi-bin/aa_rstablew.pl?ID=AA&year="
		url = url + str(year)
		url = url + "&task=0&place="
		url = url + self.location
		url = url + "&lon_sign="
		url = url + str(self.lonsig)
		url = url + "&lon_deg="
		url = url + str(self.londeg)
		url = url + "&lon_min="
		url = url + str(self.lonmin)
		url = url + "&lat_sign="
		url = url + str(self.latsig)
		url = url + "&lat_deg="
		url = url + str(self.latdeg)
		url = url + "&lat_min="
		url = url + str(self.latmin)
		url = url + "&tz=&tz_sign=-1"

#		GetWebPage(url, inFile)
#		return inFile


	def preparelocation(self, decimallocation):

		if decimallocation < 0.0:
			sign = -1
		else:
			sign = 1

		location = abs(decimallocation)

		degs = int(location)

		mins = int((location - float(degs)) * 60.0)

		return sign, degs, mins