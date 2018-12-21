from . import hiveconnector_privatefunctions as HiveFunctions
from .hivecredentials_subcomponent import hivecredentials_module as HiveCredentials
from urllib.request import urlopen as GetWebPage
from urllib.request import Request as GenerateWebRequest
from json import loads as DecodeJson


class DefineConnector:

	def __init__(self):

		self.credentials = HiveCredentials.createcredentials()

		self.urlendpointroot = "https://api-prod.bgchprod.info:443/omnia"

		self.loginsessionid = ""

		self.logintohive()



	def logintohive(self):

		self.loginsessionid = ""
		loginrequestbody = '{ "sessions": [{ "username": ' + self.credentials.getusername() + ', "password": ' + self.credentials.getpassword() + ', "caller": "WEB"}] }'
		loginsessiondata = self.interactwithhive("/auth/sessions", loginrequestbody, "sessions")
		loginsessiondata = loginsessiondata[0]
		self.loginsessionid = loginsessiondata['sessionId']


	def getdevices(self):

		devicenodedata = self.interactwithhive("/nodes", "", "nodes")

		deviceids = {}
		deviceids['Home Hub'] = ""
		deviceids['Thermostat'] = ""
		deviceids['Boiler Switch'] = ""
		deviceids['Controller'] = ""

		for node in devicenodedata:
			#nodename = node['name']
			deviceattributes = node['attributes']
			rawdevicetype = HiveFunctions.getvalue(deviceattributes['nodeType'])
			devicetype = "OTHER"
			if rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostatui.json#':
				devicetype = "Thermostat"
			#	print("---------------------------------")
			#	print(nodename)
			elif rawdevicetype == 'http://alertme.com/schema/json/node.class.hub.json#':
				devicetype = "Home Hub"
			#	print("---------------------------------")
			#	print(nodename)
			elif rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostat.json#':
				if 'powerSupply' in deviceattributes:
					devicetype = "Boiler Switch"
			#		print("---------------------------------")
			#		print(nodename)
				elif 'schedule' in deviceattributes:
					devicetype = "Controller"
			#		print("---------------------------------")
			#		print(nodename)
			#		print("CONTROLLER TYPE")
			#		print(deviceattributes.keys())
			if devicetype in deviceids:
				deviceids[devicetype] = node['id']
			#	print(node['id'])
			#if devicetype == "OTHER":
			#	print("OTHER DEVICE TYPE: ", rawdevicetype)
			#if 'powerSupply' in deviceattributes:
			#	print(devicetype, "Device last seen: ", HiveFunctions.sanitiseunixdate(node['lastSeen']))
			#	powersupply = deviceattributes['powerSupply']
			#	if HiveFunctions.getvalue(powersupply) == "BATTERY":
			#		batterystate = deviceattributes['batteryVoltage']
			#		print(devicetype, "Device = battery: ", HiveFunctions.getvalue(batterystate), HiveFunctions.getpolltime(batterystate))
			#	else:
			#		print(devicetype, "Device = mains")

		return deviceids



	def interactwithhive(self, endpoint, requestdata, rootnodename):

		fullurlendpoint = self.urlendpointroot + endpoint

		if requestdata == "":
			webrequest = GenerateWebRequest(fullurlendpoint)
		else:
			webrequest = GenerateWebRequest(fullurlendpoint, data=requestdata.encode('ascii', 'ignore'))
		webrequest.add_header('Content-Type', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('Accept', 'application/vnd.alertme.zoo-6.1+json')
		webrequest.add_header('X-Omnia-Client', 'Hive Web Dashboard')
		if self.loginsessionid != "":
			webrequest.add_header('X-Omnia-Access-Token', self.loginsessionid)
		outcome = GetWebPage(webrequest)
		outcome = outcome.read()
		outcome = outcome.decode('utf-8', 'ignore')
		outcome = DecodeJson(outcome)
		outcome = outcome[rootnodename]

		#print("\\/=======================================\\/")
		#print(fullurlendpoint)
		#print("===========================================")
		#print(outcome)
		#print("/\\=======================================/\\")

		return outcome

