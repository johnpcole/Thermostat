from .hivecredentials_subcomponent import hivecredentials_module as HiveCredentials
from urllib.request import urlopen as GetWebPage
from urllib.request import Request as GenerateWebRequest
from urllib.request import URLError as WebError
from json import loads as DecodeJson


class DefineConnector:

	def __init__(self):

		self.credentials = HiveCredentials.createcredentials()

		self.urlendpointroot = "https://api-prod.bgchprod.info:443/omnia"

		self.loginsessionid = ""

		self.maximumtrieslimit = 3

		self.logintohive()



	def logintohive(self):

		self.loginsessionid = ""
		loginrequestbody = '{ "sessions": [{ "username": ' + self.credentials.getusername() + ', "password": ' + self.credentials.getpassword() + ', "caller": "WEB"}] }'
		loginsessiondata = self.interactwithhive("/auth/sessions", loginrequestbody, "sessions")
		loginsessiondata = loginsessiondata[0]
		self.loginsessionid = loginsessiondata['sessionId']



	def retrievelatestinfo(self):

		return self.interactwithhive("/nodes", "", "nodes")



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

		tries = 0
		outcome = ""

		while tries < self.maximumtrieslimit:
			try:

				outcome = GetWebPage(webrequest)
				tries = 99999

			except WebError as errorobject:
				tries = tries + 1
				print("Error accessing Hive website: ", errorobject.reason)

		if tries == 99999:
			outcome = outcome.read()
			outcome = outcome.decode('utf-8', 'ignore')
			outcome = DecodeJson(outcome)
			outcome = outcome[rootnodename]
		else:
			print("Gave up accessing Hive website")

		#print("\\/=======================================\\/")
		#print(fullurlendpoint)
		#print("===========================================")
		#print(outcome)
		#print("/\\=======================================/\\")

		return outcome



