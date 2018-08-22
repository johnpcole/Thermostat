from boilercontroller_components import boilercontroller_module as BoilerController

from userinterface_components import userinterface_module as UserInterface

from miscellaneous_components.astro_component import astro_module as Astro
from miscellaneous_components.timekeeper_component import timekeeper_module as TimeKeeper

from common_components.userinterface_framework import userinterface_module as GUI

def runapplication():

	# ===============================================================================================================
	GUI.init()
	# ===============================================================================================================

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# Define objects used to drive application     #
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	boilercontroller = BoilerController.createboilercontroller()

	userinterface = UserInterface.createuserinterface()

	timekeeper = TimeKeeper.createtimekeeper()

	connecttowebsite = False
	astrodata = Astro.createlocation("Bristol+(UK)", -2.570310, 51.497772, 0, connecttowebsite, timekeeper) #51.497772


	# ===============================================================================================================
	# ===============================================================================================================

	while userinterface.getquitstate() == False:

		# Update the system clock (not used by boiler switch)
		timekeeper.update()

		# Process any input events (mouse clicks, mouse moves)
		useraction = userinterface.processinputs(boilercontroller)

		# If a temperature override was set, apply this
		if useraction.get("Override Temperature") == True:
			boilercontroller.setoverridetemperature(userinterface, timekeeper)

		# Update the boiler controller with latest current & desired temperatures,
		# and switch on/off the boilder accordingly
		boilercontroller.updateboilercontroller(timekeeper)

		# Update sunrise/sunset data
		astrodata.updateastrotimes(timekeeper)

		# Refresh Screen
		userinterface.refreshscreen(boilercontroller, timekeeper, astrodata)



	# ===============================================================================================================
	GUI.quit()
	# ===============================================================================================================

