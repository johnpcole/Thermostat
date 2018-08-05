

class DefineThermostat:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.calculatedboilerstate = False

		self.switchthreshold = 0.5

	# =========================================================================================

	def updatethermostatstatus(self, currenttemperature, desiredtemperature):

		if currenttemperature >= (desiredtemperature + self.switchthreshold):
			self.calculatedboilerstate = False
		elif currenttemperature <= (desiredtemperature - self.switchthreshold):
			self.calculatedboilerstate = True
		# else:
			# Leave the boiler as it is

		return self.calculatedboilerstate

	# =========================================================================================

	def getstatus(self):

		return self.calculatedboilerstate

