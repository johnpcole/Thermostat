from boilerswitch_component import boilerswitch_module as BoilerSwitch
from thermostat_component import thermostat_module as Thermostat
from schedule_component import schedule_module as Schedule
from tempsetter_component import tempsetter_module as TempSetter
from thermometer_component import thermometer_module as Thermometer

from meteo_component import meteo_module as Meteo

from display_component import display_module as Display
from controls_component import controls_module as Controller

from common_components.userinterface_framework import userinterface_module as GUI
from common_components.clock_datatype import clock_module as Clock


def runapplication():

	# ===============================================================================================================
	GUI.init()
	# ===============================================================================================================

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# Define objects used to drive application     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	boilerswitch = BoilerSwitch.createboilerswitch()
	thermostat = Thermostat.createthermostat()
	schedule = Schedule.createschedule()
	tempsetter = TempSetter.createsetter()
	thermometer = Thermometer.createthermometer()

	controls = Controller.createcontroller()
	display = Display.createdisplay(controls)

	meteolocation = Meteo.createlocation("Bristol+(UK)", -2.570310, 51.497772, 0)
	print meteolocation.getsuntimes(1, 1, 2018)


	# ===============================================================================================================
	# ===============================================================================================================

	while controls.getquitstate() == False:

		currenttime = Clock.getnow()

		# Get scheduled desired temperature
		scheduledtemperature = schedule.getcurrentinstruction(currenttime)

		# Process any input events (mouse clicks, mouse moves)
		controls.processinput(scheduledtemperature)

		# Get the current temperature
		thermometer.updatethermometer()

		# Get the desired temperature
		tempsetter.updatedesiredtemperature(scheduledtemperature)

		# Determine whether the boiler needs to be switched on/off
		thermostat.updatethermostatstatus(thermometer.gettemperature(),
											tempsetter.gettemperature())

		# Update the boiler switch based on the thermostat outcome
		boilerswitch.updateboilerstatus(thermostat.getstatus())

		# Refresh Screen
		display.refreshscreen(currenttime,
								controls,
								schedule,
								boilerswitch,
								thermostat,
								tempsetter,
								thermometer)



	# ===============================================================================================================
	GUI.quit()
	# ===============================================================================================================

