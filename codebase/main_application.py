from boilercontroller_components import boilercontroller_module as BoilerController

from miscellaneous_components.astro_component import astro_module as Astro

from userinterface_components import userinterface_module as UserInterface

from common_components.userinterface_framework import userinterface_module as GUI

from .common_components.clock_datatype import clock_module as Clock

def runapplication():

	# ===============================================================================================================
	GUI.init()
	# ===============================================================================================================

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# Define objects used to drive application     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	boilercontroller = BoilerController.createboilercontroller()

	userinterface = UserInterface.createuserinterface()

	previousmeasuretime = Clock.getnow()
	cyclemeasure = 0

	astrodata = Astro.createlocation("Bristol+(UK)", -2.570310, 51.497772, 0)


	# ===============================================================================================================
	# ===============================================================================================================

	while userinterface.getquitstate() == False:

		currentmeasuretime = Clock.getnow()
		cyclemeasure = cyclemeasure + 1
		if currentmeasuretime.getvalue() != previousmeasuretime.getvalue():
			#print "Cycles last second =", cyclemeasure
			cyclemeasure = 0
		previousmeasuretime = currentmeasuretime

		# Get current time as hours & minutes only
		currenttime = Clock.getsecondlessnow()

		# Process any input events (mouse clicks, mouse moves)
		useraction = userinterface.processinputs(boilercontroller)

		# If a temperature override was set, apply this
		if useraction.get("Override Temperature") == True:
			boilercontroller.setoverridetemperature(userinterface, currenttime)

		# Update the boiler controller with latest current & desired temperatures,
		# and switch on/off the boilder accordingly
		boilercontroller.updateboilercontroller(currenttime)

		# Update sunrise/sunset data
		astrodata.updatesuntimes()

		# Refresh Screen
		userinterface.refreshscreen(boilercontroller, currenttime)



	# ===============================================================================================================
	GUI.quit()
	# ===============================================================================================================

