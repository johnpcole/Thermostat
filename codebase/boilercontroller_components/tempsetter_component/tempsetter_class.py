from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.enumeration_datatype import enumeration_module as Enumeration


class DefineSetter:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.desiredtemperature = 5.0

		self.currentscheduledtemperature = 5.0

		self.overrideexpire = Clock.createastime(0, 0, 0)

		self.overridemode = Enumeration.createenum(["Off", "Lock", "Timed", "Next"], "Off")

	# =========================================================================================

	def updatedesiredtemperature(self, scheduledtemperature, currenttime):

		if self.overridemode.get("Timed"):
			if Clock.isequal(self.overrideexpire, currenttime) == True:
				self.overridemode.set("Off")
				print "Ending Timed Override"

		elif self.overridemode.get("Next"):
			if scheduledtemperature != self.currentscheduledtemperature:
				self.overridemode.set("Off")
				print "Ending Next Limited Override"

		if self.overridemode.get("Off") == True:
			self.desiredtemperature = scheduledtemperature

		self.currentscheduledtemperature = scheduledtemperature

		return self.desiredtemperature



	# =========================================================================================

	def setoverridetemperature(self, expiryinstruction, currenttime):

		self.desiredtemperature = expiryinstruction.getslidervalue()

		expire = expiryinstruction.getselectedtime()

		if (expire == "Lock") or (expire == "Next"):
			self.overridemode.set(expire)
		else:
			self.overridemode.set("Timed")
			self.overrideexpire = Clock.timeadd(currenttime, Clock.createastime(0, int(expire), 0))

		return self.desiredtemperature



	# =========================================================================================

	def gettemperature(self):

		return self.desiredtemperature



	# =========================================================================================

	def getoverridemode(self):

		return self.overridemode



	# =========================================================================================

	def getoverridetime(self):

		return self.overrideexpire

