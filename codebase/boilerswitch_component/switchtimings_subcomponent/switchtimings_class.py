from ...common_components.clock_datatype import clock_module as Clock


class DefineSwitchTiming:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.latestswitchtime = Clock.getnow()



	# -------------------------------------------------------------------
	# Returns the number of seconds since the last switch update
	# -------------------------------------------------------------------

	def getsecondssincelastswitched(self):

		timesincelastswitched = Clock.timediff(self.latestswitchtime, Clock.getnow())

		return timesincelastswitched.getvalue()



	# -------------------------------------------------------------------
	# Returns the time of the last switch
	# -------------------------------------------------------------------

	def getlastswitchedtime(self):

		return self.latestswitchtime



	# -------------------------------------------------------------------
	# Updates the boiler clocks, based on current switch status
	# -------------------------------------------------------------------

	def updateswitchedtime(self):

		self.latestswitchtime = Clock.getnow()
