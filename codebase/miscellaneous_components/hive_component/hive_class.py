from ...common_components.datetime_datatypes import datetime_module as DateTime
from .hivecredentials_subcomponent import hivecredentials_module as Credentials
#from .webscraper_subcomponent import webscraper_module as WebScraper
#from .astroitem_subcomponent import astroitem_module as AstroItem
#from urllib.parse import urlencode as DataEncoder
from urllib.request import urlopen as GetWebPage
from urllib.request import Request as GenerateWebRequest
#from urllib.request import URLError as WebError
from json import loads as DecodeJson
from .hivewebscraper_subcomponent import hivewebscraper_privatefunctions as HiveFunctions


class DefineHiveInterface:

	def __init__(self):

		self.credentials = Credentials.createcredentials()

		self.todaydate = DateTime.createdatefromtriplet(1, 1, 2000)

		self.hivelibrary = []

		self.body = '{ "sessions": [{ "username": ' + self.credentials.getusername() + ', "password": ' + self.credentials.getpassword() + ', "caller": "WEB"}] }'

		self.urlendpointroot = "https://api-prod.bgchprod.info:443/omnia"

		self.loginsessiondata = self.interactwithhive("/auth/sessions", self.body, "", "sessions")
		self.loginsessiondata = self.loginsessiondata[0]

		self.devicenodedata = self.interactwithhive("/nodes", "", self.loginsessiondata['sessionId'], "nodes")


		for node in self.devicenodedata:
			nodename = node['name']
			print("---------------------------------")
			print(nodename)
			deviceattributes = node['attributes']
			rawdevicetype = HiveFunctions.getvalue(deviceattributes['nodeType'])
			if rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostatui.json#':
				devicetype = "Thermostat"
			elif rawdevicetype == 'http://alertme.com/schema/json/node.class.hub.json#':
				devicetype = "Home Hub"
			elif rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostat.json#':
				devicetype = "Boiler Switch"
			else:
				devicetype = "OTHER"
			if 'powerSupply' in deviceattributes:
				print(devicetype, "Device last seen: ", HiveFunctions.sanitiseunixdate(node['lastSeen']))
				powersupply = deviceattributes['powerSupply']
				if HiveFunctions.getvalue(powersupply) == "BATTERY":
					batterystate = deviceattributes['batteryVoltage']
					print(devicetype, "Device = battery: ", HiveFunctions.getvalue(batterystate), HiveFunctions.getpolltime(batterystate))
				else:
					print(devicetype, "Device = mains")



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


	def interactwithhive(self, endpoint, requestdata, sessionid, rootnodename):

		fullurlendpoint = self.urlendpointroot + endpoint

		if requestdata == "":
			webrequest = GenerateWebRequest(fullurlendpoint)
		else:
			webrequest = GenerateWebRequest(fullurlendpoint, data=requestdata.encode('ascii', 'ignore'))
		webrequest.add_header('Content-Type', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('Accept', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('X-Omnia-Client', 'Hive Web Dashboard')
		if sessionid != "":
			webrequest.add_header('X-Omnia-Access-Token', sessionid)
		outcome = GetWebPage(webrequest)
		outcome = outcome.read()
		outcome = outcome.decode('utf-8', 'ignore')
		outcome = DecodeJson(outcome)
		outcome = outcome[rootnodename]

		print("\\/=======================================\\/")
		print(fullurlendpoint)
		print("===========================================")
		print(outcome)
		print("/\\=======================================/\\")

		return outcome