

class DefineThermostat:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.calculatedboilerstate = False

		self.desiredtemperature = 5.0

		self.currenttemperature = 99.9

		self.switchthreshold = 0.5

	# =========================================================================================

	def updatethermostatstatus(self):

		if self.currenttemperature >= (self.desiredtemperature + self.switchthreshold):
			self.calculatedboilerstate = True
		elif self.currenttemperature <= (self.desiredtemperature - self.switchthreshold):
			self.calculatedboilerstate = False
		# else:
			# Leave the boiler as it is

		return self.calculatedboilerstate

	# =========================================================================================

	def getstatus(self):

		return self.calculatedboilerstate

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
