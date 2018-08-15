from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.datetime_datatypes import datetime_module as DateTime
from webscraper_subcomponent import webscraper_module as WebScraper



class DefineAstro:

	def __init__(self, locationname, longitude, latitude, timeshift):

		self.todaydatetime = DateTime.createfromsextuplet(1, 1, 2000, 0, 0, 0)

		self.todaysunrise = Clock.createasinteger(0)

		self.todaysunset = Clock.createasinteger(0)

		self.tomorrowsunrise = Clock.createasinteger(0)

		self.tomorrowsunset = Clock.createasinteger(0)

		self.webscraper = WebScraper.createscraper(locationname, longitude, latitude, timeshift)



	def updatesuntimes(self):
		
		nowday, nowmonth, nowyear, dummy1, dummy2, dummy3 = DateTime.getnow().getsextuplet()
		lastday, lastmonth, lastyear, dummy1, dummy2, dummy3 = self.todaydatetime.getsextuplet()

		if (nowday != lastday) or (nowmonth != lastmonth) or (nowyear != lastyear):

			self.todaydatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)

			self.todaysunrise, self.todaysunset = self.webscraper.getsuntimes(nowday, nowmonth, nowyear)

			tomorrowdatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
			tomorrowdatetime.adjustdays(1)
			tomday, tommonth, tomyear, dummy1, dummy2, dummy3 = tomorrowdatetime.getsextuplet()

			self.tomorrowsunrise, self.tomorrowsunset = self.webscraper.getsuntimes(tomday, tommonth, tomyear)

			print "Updated Sunrise/set times: ", self.todaydatetime.getiso(),\
													self.todaysunrise.gettext(),\
													self.todaysunset.gettext(), \
													self.tomorrowsunrise.gettext(), \
													self.tomorrowsunset.gettext()

		#else:
			#print "Not updating sunrise/set times"


	def getcurrentsuntimes(self, currenttime):

		baselinevalue = currenttime.getvalue()

		if baselinevalue > (self.todaysunrise - 120):
			sunrise = Clock.createasclock(self.tomorrowsunrise)
		else:
			sunrise = Clock.createasclock(self.todaysunrise)

		if baselinevalue > (self.todaysunset - 120):
			sunset = Clock.createasclock(self.todaysunset)
		else:
			sunset = Clock.createasclock(self.todaysunset)

		return sunrise, sunset
