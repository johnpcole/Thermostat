from .colours_subcomponent import colours_module as ColourLibrary
from .images_subcomponent import images_module as ImageLibrary
from .text_subcomponent import text_module as TextGenerator
from ..vector_datatype import vector_module as Vector
from ..userinterface_framework import userinterface_module as GUI



class DefineApplicationWindow:
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================



	def __init__(self, windowsize, windowtitle):


		# Defines the size of the application window
		# Creates the application window object
		if (windowsize.getx() > 0) and (windowsize.gety() > 0):
			self.screensize = Vector.createfromvector(windowsize)
			self.windowobject = GUI.display.set_mode((self.screensize.getcoordinates()))
		else:
			self.windowobject = GUI.display.set_mode((0,0), GUI.FULLSCREEN)
			displayinfo = GUI.display.Info()
			self.screensize = Vector.createfromvalues(displayinfo.current_w, displayinfo.current_h)

		# Defines the application window title
		GUI.display.set_caption(windowtitle)

		# Loads image library
		self.imagelibrary = ImageLibrary.createlibrary()

		# Loads text generator
		self.textgenerator = TextGenerator.creategenerator()

		# Loads colour library
		self.colourlibrary = ColourLibrary.createlibrary()



	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Adds a colour to the colour library
	# -------------------------------------------------------------------

	def addcolour(self, colourlabel, redvalue, greenvalue, bluevalue):

		self.colourlibrary.add(colourlabel, redvalue, greenvalue, bluevalue)



	# -------------------------------------------------------------------
	# Adds an image to the image library
	# -------------------------------------------------------------------

	def addimage(self, imagelabel, subfolder, filename, transparency):

		self.imagelibrary.add(imagelabel, subfolder, filename, transparency)



	# -------------------------------------------------------------------
	# Adds a font to the font library
	# -------------------------------------------------------------------

	def addfont(self, fontname, subfolder, fontfile, fontsize):

		self.textgenerator.addfont(fontname, subfolder, fontfile, fontsize)



	# -------------------------------------------------------------------
	# Prints image / text to screen
	# -------------------------------------------------------------------

	def drawimage(self, picture, position):

		self.windowobject.blit(self.imagelibrary.get(picture), (position.getcoordinates()))



	# -------------------------------------------------------------------
	# Flips the display
	# -------------------------------------------------------------------

	def updatescreen(self):

		GUI.display.flip()



	# -------------------------------------------------------------------
	# Draws a line
	# -------------------------------------------------------------------

	def drawline(self, firstpoint, secondpoint, linecolour, linewidth, aliased):

		# Draw aliased
		if aliased == "":
			GUI.draw.line(self.windowobject, self.colourlibrary.get(linecolour),
											firstpoint.getcoordinates(), secondpoint.getcoordinates(), linewidth)
		else:
			GUI.draw.aaline(self.windowobject, self.colourlibrary.get(linecolour),
											firstpoint.getcoordinates(), secondpoint.getcoordinates())



	# -------------------------------------------------------------------
	# Draws a rectangle
	# -------------------------------------------------------------------

	def drawrectangle(self, topleft, rectanglesize, fillcolour, bordercolour, borderwidth):

		# Draw fill
		if fillcolour != "":
			GUI.draw.rect(self.windowobject, self.colourlibrary.get(fillcolour),
														(topleft.getcoordinates(), rectanglesize.getcoordinates()), 0)

		# Draw outline
		if (bordercolour != "") and (borderwidth != 0):
			GUI.draw.rect(self.windowobject, self.colourlibrary.get(bordercolour),
												(topleft.getcoordinates(), rectanglesize.getcoordinates()), borderwidth)



	# -------------------------------------------------------------------
	# Draws a circle
	# -------------------------------------------------------------------

	def drawcircle(self, centre, radius, fillcolour, bordercolour, borderwidth):

		# Draw fill
		if fillcolour != "":
			GUI.draw.circle(self.windowobject, self.colourlibrary.get(fillcolour), (centre.getcoordinates()), radius, 0)

		# Draw outline
		if (bordercolour != "") and (borderwidth != 0):
			GUI.draw.circle(self.windowobject, self.colourlibrary.get(bordercolour),
																		(centre.getcoordinates()), radius, borderwidth)



	# -------------------------------------------------------------------
	# Writes text
	# -------------------------------------------------------------------

	def drawtext(self, outputtext, textposition, alignment, colour, fontname):

		textwidth = (self.gettextsize(outputtext, fontname)).getx()

		if alignment == "Left":
			margin = Vector.createorigin()
		elif alignment == "Right":
			margin = Vector.createfromvalues(textwidth, 0)
		elif alignment == "Centre":
			margin = Vector.createfromvalues(int(textwidth / 2), 0)
		else:
			margin = 1/0

		actualposition = Vector.subtract(textposition, margin)

		self.imagelibrary.settext(self.textgenerator.gettextimage(outputtext, self.colourlibrary.get(colour), fontname))
		self.drawimage("Text", actualposition)



	# ==========================================================================================
	# Get Information
	# ==========================================================================================

	# -------------------------------------------------------------------
	# Returns the screensize
	# -------------------------------------------------------------------

	def getscreensize(self):
		return self.screensize



	# -------------------------------------------------------------------
	# Returns the size of a block of a text
	# -------------------------------------------------------------------

	def gettextsize(self, outputtext, fontname):
		return Vector.createfrompair(self.textgenerator.gettextsize(outputtext, fontname))
