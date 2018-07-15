from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.appdisplay_framework import appdisplay_module as AppDisplay
from . import display_privatefunctions as DisplayFunction
from ..common_components.clock_datatype import clock_module as Clock
from ..common_components.transition_datatype import transition_module as Transition


class DefineDisplay:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		# Sets up the application window size
		self.displaysize = Vector.createfromvalues(480, 320)

		# Sets up pygame window related properties & methods and loads images, fonts & custom colours
		self.display = AppDisplay.createwindow(self.displaysize, "Thermostat")
		self.setupfonts()
		self.setupcustomcolours()
		self.setupimages()

		# Position of current time marker in the runway
		self.runwaystartline = 68

		# How many pixels make up an hour (36 or 48) in the runway
		self.runwaytimescale = 36

		# Height of runway (actually one pixel more!)
		self.runwayheight = 48

		# Data for capturing the animation of the desired temperature
		self.desiredtemperature = Transition.createtransition(1000, 1000, 0)

		# Stores the list of buttons to process
		#self.buttonlist = control.getbuttoncollection("")
		#self.buttonlist.remove("Field")



	# -------------------------------------------------------------------
	# Adds custom colours
	# -------------------------------------------------------------------

	def setupcustomcolours(self):

		colourlist = DisplayFunction.getcolourpallette()
		for colour in colourlist.keys():
			colourdef = colourlist[colour]
			self.display.addcolour(colour, colourdef[0], colourdef[1], colourdef[2])



	# -------------------------------------------------------------------
	# Adds images
	# -------------------------------------------------------------------

	def setupimages(self):

		self.display.addimage("test", None, "test", True)



	# -------------------------------------------------------------------
	# Adds fonts
	# -------------------------------------------------------------------

	def setupfonts(self):

		fontlist = DisplayFunction.getfontpallette()
		for font in fontlist.keys():
			fontdef = fontlist[font]
			self.display.addfont(font, "", fontdef[0], fontdef[1])


	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Updates all elements of the screen, flips the display, then
	# removes embellishments from the field ready for the next cycle
	# -------------------------------------------------------------------

	def refreshscreen(self, currenttime, controls, scheduler, boilercontroller):

		# Draw Runway
		self.drawrunway(currenttime, scheduler, boilercontroller)

		# Draw Board
		self.drawboard(boilercontroller)

 		# Refresh screen
		self.display.updatescreen()

		# Blank out area
		self.display.drawrectangle(Vector.createfromvalues(0, 0), Vector.createfromvalues(480, 240), "Black", "", 0)

#
#
# 	# -------------------------------------------------------------------
# 	# Draws the button groups
# 	# -------------------------------------------------------------------
#
# 	def paintbuttons(self, control):
#
# 		for buttonname in self.buttonlist:
# 			buttonstate = control.getbuttonstate(buttonname)
#
# 			if buttonstate != "Hidden":
# 				buttonlocation = control.getbuttonposition(buttonname)
# 				self.display.drawimage(buttonname, buttonlocation)
#
# 				if buttonstate == "Disabled":
# 					self.display.drawimage("Overlay - Disabled", buttonlocation)
#
# 				else:
# 					if control.getbuttonhoverstate(buttonname) == True:
# 						self.display.drawimage("Overlay - Hover", buttonlocation)





	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

	def drawboard(self, boilercontroller):

		# Draw current temperature
		items = DisplayFunction.getcurrenttemplayout(max(0, boilercontroller.getcurrenttemperature()),
																					Vector.createfromvalues(260, 40))

		for item in items.keys():
			itemdef = items[item]
			self.display.drawtext(itemdef[0], itemdef[1], itemdef[2], itemdef[3], itemdef[4])


	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

 	def drawrunway(self, currenttime, scheduler, boilercontroller):

		# The current hour
		lasthour = currenttime.gethour()

		# Number of pixels markers are shifted left
		offsetpixels = int(self.runwaytimescale * ((currenttime.getminute() * 60) + currenttime.getsecond()) / 3600)

		# Display current desired temperature
		self.drawdesiredtemperature(boilercontroller.getdesiredtemperature())

		# Draw hour/half/quarter markers
		self.drawrunwaytimings(currenttime, lasthour, offsetpixels)

		# Draw upcoming desired temperatures (from schedule)
		self.drawrunwayinstructions(currenttime, lasthour, offsetpixels, scheduler)

		# Draw the current time main marker
		self.display.drawline(Vector.createfromvalues(self.runwaystartline, 0),
								Vector.createfromvalues(self.runwaystartline, self.runwayheight),
								"Grey", 1, "")

		# Draw the runway edge
		#self.display.drawline(Vector.createfromvalues(0, 49),
		#						Vector.createfromvalues(480, 49),
		#						"Grey",
		#						1,
		#						"")



	# -------------------------------------------------------------------
	# Paints the desired temperature at the top of the screen
	# -------------------------------------------------------------------

	def drawdesiredtemperature(self, latestdesiredtemperature):

		self.desiredtemperature.updatevalue(latestdesiredtemperature)

		displayedtemperature = self.desiredtemperature.getswitchedvalue()

		transitionfraction = self.desiredtemperature.gettransitionfraction()

		self.display.drawtext(	str(displayedtemperature),
								Vector.createfromvalues(DisplayFunction.gettransitionposition(
										self.runwaystartline - 5, self.runwaystartline, transitionfraction), -3),
								"Right",
								DisplayFunction.gettransitioncolour(displayedtemperature, transitionfraction),
								"Desired Temp")

		self.display.drawrectangle(Vector.createfromvalues(self.runwaystartline, 0),
								Vector.createfromvalues(self.runwaystartline * 2, self.runwayheight),
								"Black", "", 0)


	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwaytimings(self, currenttime, lasthour, offsetpixels):

		# Print the hour/half/quarter markers
		for marker in DisplayFunction.gettimelinemarkers(self.runwaystartline, self.runwaytimescale, offsetpixels):

			self.display.drawline(Vector.createfromvalues(marker.getx(), 0), marker, "Grey", 1, "")

		# Print the hour labels
		for hourindex in range(0, 14):

			# Display the current hour at the current time marker only if it's exactly on the clock
			if (currenttime.getminute() == 0) or (hourindex > 0):

				# Position of hour marker line
				hourmarker = self.runwaystartline + (hourindex * self.runwaytimescale) - offsetpixels

				# Draw hour marker number
				self.display.drawtext(Clock.convert24hourtohuman(hourindex + lasthour),
										Vector.createfromvalues(hourmarker + 3, 1),
										"Left", "Grey", "Timeline Hours")




	# -------------------------------------------------------------------
	# Paints the scheduled settings at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwayinstructions(self, currenttime, lasthour, offsetpixels, scheduler):

		# Get list of scheduled times
		scheduledtimes = scheduler.getscheduledtimes()

		# Loop over scheduled times
		for scheduledtime in scheduledtimes:

			# Position of marker
			houroffset = DisplayFunction.getfuturetimevalue(scheduledtime.getvalue(), currenttime.getvalue()) - (3600 * lasthour)
			pixelposition = self.runwaystartline + int(houroffset * self.runwaytimescale / 3600) - offsetpixels

			# Draw marker
			self.display.drawline(Vector.createfromvalues(pixelposition, 18),
								 	Vector.createfromvalues(pixelposition, self.runwayheight),
								 	"Grey",
								 	1,
								 	"")

			# Get desired temperature
			tempvalue = scheduler.getscheduledinstruction(scheduledtime)

			# Draw desired temperature number
			self.display.drawtext(str(tempvalue),
									Vector.createfromvalues(pixelposition + 3, self.runwayheight - 29),
									"Left",
									DisplayFunction.gettemperaturecolour(tempvalue),
									"Timeline Temps")


#
#
#
# 	# ==========================================================================================
# 	# Get Information
# 	# ==========================================================================================
#
