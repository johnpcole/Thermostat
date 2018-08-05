from ..common_components.clock_datatype import clock_module as Clock


class DefineSetter:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.desiredtemperature = 5.0

	# =========================================================================================

	def updatedesiredtemperature(self, scheduledtemperature):

		self.desiredtemperature = scheduledtemperature

		return self.desiredtemperature



	# =========================================================================================

	def gettemperature(self):

		return self.desiredtemperature

