from ..common_components.clock_datatype import clock_module as Clock


class DefineBoilerController:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.status = "Unknown"

		self.boilerswitchstatus = False

		self.boilerswitchbuffer = 1 # minutes

		self.boilerlastontime = Clock.getnow()

		self.boilerlastofftime = Clock.getnow()

		self.desiredtemperature = 5.0

		self.currenttemperature = 99.9

	# =========================================================================================

	def updateboilerstatus(self):

		self.updateboilerclocks()

		outcome = "Unknown!"

		if self.desiredtemperature > self.currenttemperature:
			# Boiler should be switched on if it's not already on AND it's been off for 5 minutes
			if self.boilerswitchstatus == False:
				if self.getboilerswitchtiming(False).getvalue < (self.boilerswitchbuffer * 60):
					self.turnboileron()
					outcome = "On - New"
				else:
					outcome = "On - Off Snooze"
			else:
				outcome = "On - Hold On"
		else:
			# Boiler should be switched off if it's not already off AND it's been on for 5 minutes
			if self.boilerswitchstatus == True:
				if self.getboilerswitchtiming(True).getvalue < (self.boilerswitchbuffer * 60):
					self.turnboileroff()
					outcome = "Off - New"
				else:
					outcome = "Off - On Extend"
			else:
				outcome = "Off - Hold Off"

		self.status = outcome

		return outcome

	# =========================================================================================

	def updateboilerclocks(self):

		if self.boilerswitchstatus == True:
			self.boilerlastontime = Clock.getnow()
		else:
			self.boilerlastofftime = Clock.getnow()

	# =========================================================================================

	def getboilerswitchtiming(self, mode):

		currenttime = Clock.getnow()
		if mode == True:
			switchtime = self.boilerlastontime
		else:
			switchtime = self.boilerlastofftime
		return Clock.timediff(switchtime, currenttime)

	# =========================================================================================

	def getboilerswitchstatus(self):

		return self.boilerswitchstatus

	# =========================================================================================

	def getstatus(self):

		return self.status

	# =========================================================================================

	def setdesiredtemperature(self, temp):

		self.desiredtemperature = temp

		return self.getdesiredtemperature()

	# =========================================================================================

	def getdesiredtemperature(self):

		return int(self.desiredtemperature)

	# =========================================================================================

	def setcurrenttemperature(self, temp):

		self.currenttemperature = temp

		return self.getcurrenttemperature()

	# =========================================================================================

	def getcurrenttemperature(self):

		return self.currenttemperature

	# =========================================================================================

	def turnboileron(self):

		self.boilerswitchstatus = True
		self.updateboilerclocks()
		#CODE TO THROW RELAY

	# =========================================================================================

	def turnboileroff(self):

		self.boilerswitchstatus = False
		self.updateboilerclocks()
		#CODE TO THROW RELAY


