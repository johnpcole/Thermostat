from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.appdisplay_framework import appdisplay_module as AppDisplay
from . import display_privatefunctions as DisplayFunction
from ..common_components.clock_datatype import clock_module as Clock
from runway_subcomponent import runway_module as Runway
from . import display_colourdata as DisplayColours
from . import display_imagedata as DisplayImages
from . import display_fontdata as DisplayFonts


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
		self.setupcolours()
		self.setupimages()
		self.runway = Runway.createrunway()


		# Stores the list of buttons to process
		#self.buttonlist = control.getbuttoncollection("")
		#self.buttonlist.remove("Field")



	# -------------------------------------------------------------------
	# Adds custom colours
	# -------------------------------------------------------------------

	def setupcolours(self):

		colourlist = DisplayColours.getcolourpallette()
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

		fontlist = DisplayFonts.getfontpallette()
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

		# Display current desired temperature
		self.paintitems(self.runway.drawdesiredtemperature(boilercontroller.getdesiredtemperature()))

		# Draw upcoming desired temperatures (from schedule)
		self.paintitems(self.runway.drawinstructions(currenttime, scheduler))

		# Draw hour labels
		self.paintitems(self.runway.drawtimelinenumbers(currenttime))

		# Draw hour/half/quarter markers
		self.paintitems(self.runway.drawtimelinemarkers(currenttime))



	# -------------------------------------------------------------------
	# Paints stuff based on a list of draw commands
	# -------------------------------------------------------------------

	def paintitems(self, itemlist):

		for item in itemlist.keys():

			itemdef = itemlist[item]
			itemtype = itemdef[0]

			if itemtype == "Line":
				self.display.drawline(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			elif itemtype == "Box":
				self.display.drawrectangle(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			elif itemtype == "Text":
				self.display.drawtext(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			else:
				print 1/0


#
#
#
# 	# ==========================================================================================
# 	# Get Information
# 	# ==========================================================================================
#
