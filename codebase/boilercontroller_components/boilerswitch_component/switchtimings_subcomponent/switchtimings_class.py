from ....common_components.datetime_datatypes import datetime_module as DateTime


class DefineSwitchTiming:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.latestswitchtime = DateTime.getnow()



	# -------------------------------------------------------------------
	# Returns the number of seconds since the last switch update
	# -------------------------------------------------------------------

	def getsecondssincelastswitched(self):

		timesincelastswitched = DateTime.secondsdifference(self.latestswitchtime, DateTime.getnow())

		return timesincelastswitched.getvalue("Seconds")



	# -------------------------------------------------------------------
	# Returns the time of the last switch
	# -------------------------------------------------------------------

	def getlastswitchedtime(self):

		return self.latestswitchtime



	# -------------------------------------------------------------------
	# Updates the boiler clocks, based on current switch status
	# -------------------------------------------------------------------

	def updateswitchedtime(self):

		self.latestswitchtime = DateTime.getnow()
