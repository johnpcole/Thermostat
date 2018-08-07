from ...common_components.clock_datatype import clock_module as Clock


class DefineThermometer:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.currenttemperature = 99.9

	# =========================================================================================

	def updatethermometer(self):

		currenttime = Clock.getnow()
		timephase = abs((currenttime.getvalue() % 300) - 150)
		self.currenttemperature = timephase / 5.0
		return self.currenttemperature



	# =========================================================================================

	def gettemperature(self):

		return self.currenttemperature
