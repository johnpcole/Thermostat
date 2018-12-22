from .hiveconnector_subcomponent import hiveconnector_module as HiveConnector
from . import hive_privatefunctions as HiveFunctions



class DefineHiveInterface:

	def __init__(self):

		self.hiveconnector = HiveConnector.createhiveconnector()

		self.devicedata = {'Home Hub': "", 'Thermostat': "", 'Boiler Switch': "", 'Controller': ""}

		self.retrievelatestinfo()

		for device in self.devicedata:
			print("==========================================")
			print(device)
			print("------------------------------------------")
			print(self.devicedata[device])
		print("==========================================")

		#self.printcontrollerdata()
		self.getcurrenttemperature()
		self.getboilerswitchstatus()



	def retrievelatestinfo(self):

		rawdevicenodedata = self.hiveconnector.retrievelatestinfo()

		self.devicedata = {'Home Hub': "", 'Thermostat': "", 'Boiler Switch': "", 'Controller': ""}

		for node in rawdevicenodedata:
			deviceattributes = node['attributes']
			devicetype = HiveFunctions.identifydevice(deviceattributes)

			if devicetype in self.devicedata:
				self.devicedata[devicetype] = deviceattributes



	def getcurrenttemperature(self):

		rawdata = self.getdata("Controller", "temperature")
		print("TEMPERATURE: ", rawdata)
		return rawdata



	def getheatingschedule(self):

		rawdata = self.getdata("Controller", "schedule")
		return rawdata



	def getboilerswitchstatus(self):
		rawdata = self.getdata("Controller", "stateHeatingRelay")
		print("SWITCH STATE: ", rawdata)



	def printcontrollerdata(self):

		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		print("======================================")
		deviceattributes = self.devicedata["Controller"]
		for devicekey in deviceattributes:
			print("======================================")
			print(devicekey)
			print("--------------------------------------")
			tempo = deviceattributes[devicekey]
			for tempoitem in tempo:
				print(tempoitem, " = ", tempo[tempoitem])
		print("======================================")


	def getdata(self, devicelabel, datafield):

		device = self.devicedata[devicelabel]
		return HiveFunctions.getvalue(device[datafield])


