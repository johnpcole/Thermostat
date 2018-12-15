from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.appdisplay_framework import appdisplay_module as AppDisplay

from .graphicdata_subcomponents import graphicdata_colours as Colours
from .graphicdata_subcomponents import graphicdata_images as Images
from .graphicdata_subcomponents import graphicdata_fonts as Fonts

class DefineDisplay:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self, controls):

		# Sets up the application window size
		self.displaysize = Vector.createfromvalues(480, 320)
		self.origin = Vector.createfromvalues(0, 0)

		# Sets up pygame window related properties & methods and loads images, fonts & custom colours
		self.display = AppDisplay.createwindow(self.displaysize, "Thermostat")
		self.setupfonts()
		self.setupcolours()
		self.setupimages()



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
		for image in imagelist.keys():
			imagelocation = imagelist[image]
			self.display.addimage(image, imagelocation, image, True)



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

	def refreshscreen(self):

		# Refresh screen
		self.display.updatescreen()

		# Blank out area
		self.display.drawrectangle(self.origin, self.displaysize, "Black", "", 0)



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
				print(1/0)



	# -------------------------------------------------------------------
	# Calculates the width of text
	# -------------------------------------------------------------------

	def calculatetextsize(self, textstring, font):

		return self.display.gettextsize(textstring, font)
