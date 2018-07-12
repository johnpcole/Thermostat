class DefineBoilerController:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.boilerswitchstatus = False

		self.desiredtemperature = 28.0

		self.currenttemperature = 1.0

	# =========================================================================================

	def updateboilerswitch(self):

		if self.desiredtemperature > self.currenttemperature:
			self.turnboileron()
		else:
			self.turnboileroff()
		return self.getboilerstatus()

	# =========================================================================================

	def getboilerstatus(self):

		return self.boilerswitchstatus

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
		#CODE TO THROW RELAY

	# =========================================================================================

	def turnboileroff(self):

		self.boilerswitchstatus = False
		#CODE TO THROW RELAY
