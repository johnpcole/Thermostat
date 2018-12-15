from ....common_components.datetime_datatypes import datetime_module as DateTime


class DefineSwitchTiming:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.latestswitchdatetime = DateTime.getnow()



	# -------------------------------------------------------------------
	# Returns the duration since the last switch update
	# -------------------------------------------------------------------

	def getdurationsincelastswitched(self):

		return DateTime.secondsdifference(DateTime.getnow(), self.latestswitchdatetime)



	# -------------------------------------------------------------------
	# Returns the time of the last switch
	# -------------------------------------------------------------------

	def getlastswitcheddatetime(self):

		return self.latestswitchdatetime



	# -------------------------------------------------------------------
	# Updates the boiler clocks, based on current switch status
	# -------------------------------------------------------------------

	def updateswitchedtime(self):

		self.latestswitchdatetime = DateTime.getnow()
