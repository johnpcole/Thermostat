from ..common_components.clock_datatype import clock_module as Clock


class DefineBoilerController:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.status = "Unknown"

		self.boilerswitchstatus = False

		self.boilerswitchbuffer = 0 # minutes

		self.boilerlastontime = Clock.getnow()

		self.boilerlastofftime = Clock.getnow()

		self.desiredtemperature = 5.0

		self.currenttemperature = 99.9

		self.boilerswitchthreshold = 0.5

	# =========================================================================================

	def updateboilerstatus(self):

		self.updateboilerclocks()

		outcome = self.calculateboilerstatus()

		if self.status != outcome:
			print "New Boiler Controller Status:", outcome

		if outcome == "On - Switch On":
			self.turnboileron()
		elif outcome == "Off - Switch Off":
			self.turnboileroff()

		self.status = outcome
		#print self.desiredtemperature, "|", self.currenttemperature, "|", self.boilerswitchstatus, "|", self.status, "|", self.getboilerswitchtiming(True).getvalue(), "|", self.getboilerswitchtiming(False).getvalue()
		return outcome

	# =========================================================================================

	def calculateboilerstatus(self):

		if self.desiredtemperature > self.currenttemperature:
			perfectswitchstatus = True
			theoreticaloutcome = "On"
			oppositeoutcome = "Off"
		else:
			perfectswitchstatus = False
			theoreticaloutcome = "Off"
			oppositeoutcome = "On"

		outcome = "Unknown"
		if self.boilerswitchstatus == perfectswitchstatus:
			outcome = theoreticaloutcome + " - Continue " + theoreticaloutcome
		else:
			if self.gettemperaturethreshold() == True:
				if self.getmostrecentboilerswitchtimingoffset() > 0:
					outcome = theoreticaloutcome + " - Switch " + theoreticaloutcome
				else:
					outcome = theoreticaloutcome + " - " + oppositeoutcome + " Override"
			else:
				outcome = oppositeoutcome + " - Within " + theoreticaloutcome + " Ignore Tolerance"

		return outcome

	# =========================================================================================

	def gettemperaturethreshold(self):

		if abs(self.desiredtemperature - self.currenttemperature) >= self.boilerswitchthreshold:
			return True
		else:
			return False

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

	def getmostrecentboilerswitchtimingoffset(self):

		if self.boilerswitchstatus == False:
			outcome = True
		else:
			outcome = False
		return (self.getboilerswitchtiming(outcome).getvalue() - (self.boilerswitchbuffer * 60))
	# =========================================================================================

	def getboilerswitchstatus(self):

		return self.boilerswitchstatus

	# =========================================================================================

	def getstatus(self):

		return self.status

	# =========================================================================================

	def setdesiredtemperature(self, temp):

		self.desiredtemperature = float(temp)

		return self.getdesiredtemperature()

	# =========================================================================================

	def getdesiredtemperature(self):

		return int(self.desiredtemperature)

	# =========================================================================================

	def setcurrenttemperature(self, temp):

		self.currenttemperature = float(temp)

		return self.getcurrenttemperature()

	# =========================================================================================

	def getcurrenttemperature(self):

		return self.currenttemperature

	# =========================================================================================

	def turnboileron(self):

		self.boilerswitchstatus = True
		print "Boiler switched on at", Clock.getnow().gettext()
		self.updateboilerclocks()
		#CODE TO THROW RELAY

	# =========================================================================================

	def turnboileroff(self):

		self.boilerswitchstatus = False
		print "Boiler switched off at", Clock.getnow().gettext()
		self.updateboilerclocks()
		#CODE TO THROW RELAY


