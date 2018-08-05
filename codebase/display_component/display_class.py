from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.appdisplay_framework import appdisplay_module as AppDisplay
from . import display_privatefunctions as DisplayFunction
#from ..common_components.clock_datatype import clock_module as Clock
from runway_subcomponent import runway_module as Runway
from board_subcomponent import board_module as Board
from buttons_subcomponent import buttons_module as Buttons
from graphicdata_subcomponent import graphicdata_colours as Colours
from graphicdata_subcomponent import graphicdata_images as Images
from graphicdata_subcomponent import graphicdata_fonts as Fonts

class DefineDisplay:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self, controls):

		# Sets up the application window size
		self.displaysize = Vector.createfromvalues(480, 320)

		# Sets up pygame window related properties & methods and loads images, fonts & custom colours
		self.display = AppDisplay.createwindow(self.displaysize, "Thermostat")
		self.setupfonts()
		self.setupcolours()
		self.setupimages()
		self.runway = Runway.createrunway()
		self.board = Board.createboard()
		self.buttons = Buttons.createbuttons(controls)




	# -------------------------------------------------------------------
	# Adds custom colours
	# -------------------------------------------------------------------

	def setupcolours(self):

		colourlist = Colours.getcolourpallette()
		for colour in colourlist.keys():
			colourdef = colourlist[colour]
			self.display.addcolour(colour, colourdef[0], colourdef[1], colourdef[2])



	# -------------------------------------------------------------------
	# Adds images
	# -------------------------------------------------------------------

	def setupimages(self):

		imagelist = Images.getimagepallette()
		for image in imagelist:
			self.display.addimage(image, None, image, True)



	# -------------------------------------------------------------------
	# Adds fonts
	# -------------------------------------------------------------------

	def setupfonts(self):

		fontlist = Fonts.getfontpallette()
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

	def refreshscreen(self, currenttime, controls, schedule, boilerswitch, thermostat, tempsetter, thermometer):

		# Draw Runway
		self.drawrunway(currenttime, schedule, tempsetter)

		# Draw Board
		self.drawboard(boilerswitch, thermostat, thermometer)

		# Draw Buttons
		self.drawbuttons(controls, tempsetter)

		# Refresh screen
		self.display.updatescreen()

		# Blank out area
		self.display.drawrectangle(Vector.createorigin(), Vector.createfromvalues(480, 240), "Black", "", 0)



	# -------------------------------------------------------------------
	# Paints the board in the center of the screen
	# -------------------------------------------------------------------

	def drawboard(self, boilerswitch, thermostat, thermometer):

		# Update the animation stats
		self.board.updateboardlayout(boilerswitch.getswitchstatus(), thermostat.getstatus())

		# Display current measured temperature
		self.paintitems(self.board.drawcurrenttemperature(thermometer.gettemperature()))

		# Display flame
		self.paintitems(self.board.drawflame(boilerswitch.getcurrentbufferstate()))



	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

 	def drawrunway(self, currenttime, schedule, tempsetter):

		# Display current desired temperature
		self.paintitems(self.runway.drawdesiredtemperature(tempsetter.gettemperature()))

		# Draw upcoming desired temperatures (from schedule)
		self.paintitems(self.runway.drawinstructions(currenttime, schedule))

		# Draw hour labels
		self.paintitems(self.runway.drawtimelinenumbers(currenttime))

		# Draw hour/half/quarter markers
		self.paintitems(self.runway.drawtimelinemarkers(currenttime))



	# -------------------------------------------------------------------
	# Paints stuff based on a list of draw commands
	# -------------------------------------------------------------------

	def paintitems(self, itemlist):

		for item in sorted(itemlist.keys()):

			itemdef = itemlist[item]
			itemtype = itemdef[0]

			if itemtype == "Line":
				self.display.drawline(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			elif itemtype == "Box":
				self.display.drawrectangle(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			elif itemtype == "Text":
				self.display.drawtext(itemdef[1], itemdef[2], itemdef[3], itemdef[4], itemdef[5])

			elif itemtype == "Image":
				self.display.drawimage(itemdef[1], itemdef[2])

			else:
				print 1/0

	# -------------------------------------------------------------------
	# Paints the buttons
	# -------------------------------------------------------------------

	def drawbuttons(self, controls, tempsetter):

		# Semi transparent background if the start button is hidden - implies other buttons are displayed
		self.paintitems(self.buttons.drawmodaloverlay(controls))

		# The Start Menu
		self.paintitems(self.buttons.drawstartmenu(controls, tempsetter.gettemperature()))

