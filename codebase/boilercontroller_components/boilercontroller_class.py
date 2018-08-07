from boilerswitch_component import boilerswitch_module as BoilerSwitch
from thermostat_component import thermostat_module as Thermostat
from schedule_component import schedule_module as Schedule
from tempsetter_component import tempsetter_module as TempSetter
from thermometer_component import thermometer_module as Thermometer



class DefineBoilerController:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		# The object which physically turns the boiler on & off
		self.boilerswitch = BoilerSwitch.createboilerswitch()

		# The object which compares the current and desired temperatures to decide
		# whether the boiler should be switched on or off
		self.thermostat = Thermostat.createthermostat()

		# The object which holds all scheduled desired temperature instructions
		self.schedule = Schedule.createschedule()

		# The object which determines what the desired temperature should be
		# based on scheduled and manually overridden settings
		self.tempsetter = TempSetter.createsetter()

		# The object which physically measures the current temperature
		self.thermometer = Thermometer.createthermometer()



	# =========================================================================================



	# -------------------------------------------------------------------
	# Updates the boiler controller components
	# -------------------------------------------------------------------

	def updateboilercontroller(self, currenttime):

		# Get the current temperature
		self.thermometer.updatethermometer()

		# Get the desired temperature
		self.tempsetter.updatedesiredtemperature(self.schedule.getcurrentinstruction(currenttime),
																						currenttime)

		# Determine whether the boiler needs to be switched on/off
		self.thermostat.updatethermostatstatus(self.thermometer.gettemperature(),
																	self.tempsetter.gettemperature())

		# Update the boiler switch based on the thermostat outcome
		self.boilerswitch.updateboilerstatus(self.thermostat.getstatus())



	# -------------------------------------------------------------------
	# Manually overrides the desired temperature
	# -------------------------------------------------------------------

	def setoverridetemperature(self, userinterface, currenttime):

			self.tempsetter.setoverridetemperature(userinterface.getoverridetemperatureinstruction(), currenttime)



	# -------------------------------------------------------------------
	# Returns the current desired temperature
	# -------------------------------------------------------------------

	def getcurrentdesiredtemperature(self):

		return self.tempsetter.gettemperature()



	# -------------------------------------------------------------------
	# Returns the current desired temperature
	# -------------------------------------------------------------------

	def getcurrentmeasuredtemperature(self):

		return self.thermometer.gettemperature()



	# -------------------------------------------------------------------
	# Returns the schedule (object)
	# -------------------------------------------------------------------

	def getschedule(self):

		return self.schedule



	# -------------------------------------------------------------------
	# Gets boiler status
	# -------------------------------------------------------------------

	def getboilerswitchstatus(self):

		return self.boilerswitch.getswitchstatus()



	# -------------------------------------------------------------------
	# Gets boiler status
	# -------------------------------------------------------------------

	def getthermostatstatus(self):

		return self.thermostat.getstatus()



	# -------------------------------------------------------------------
	# Gets boiler buffer status
	# -------------------------------------------------------------------

	def getboilerswitchbufferstate(self):

		return self.boilerswitch.getcurrentbufferstate()


