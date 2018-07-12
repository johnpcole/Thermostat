#from ..common_components.scale_datatype import scale_module as Scale
from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.appdisplay_framework import appdisplay_module as AppDisplay
#from displayactors_subcomponent import displayactors_module as DisplayActorList
from . import display_privatefunctions as DisplayFunction
from ..clock_datatype import clock_module as Clock


class DefineDisplay:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		# Sets up the application window size
		self.displaysize = Vector.createfromvalues(480, 320)

		# Sets up pygame window related properties & methods and loads images, fonts & custom colours
		self.display = AppDisplay.createwindow(self.displaysize, "Thermostat")
		self.display.addfont("Timeline Hours", "", "Font", 14)
		self.display.addfont("Timeline Temps", "", "Font", 28)
		self.display.addfont("Desired Temp", "", "Font", 54)
		self.setupcustomcolours()
		self.setupimages()

		self.runwaystartline = 65
		self.runwaytimescale = 36   # How many pixels make up an hour


		# Sets up animation clock for next wave plaque and coins & crystals
		#self.miscanimationclock = Scale.createfull(1000)

		# Sets up the list of actors, for efficient painting of defenders, ammo and enemies
		#self.actorlist = DisplayActorList.createlist()

		# Stores right-hand location of field for wiping overhang
		#self.overhanglocation = Vector.createfromvalues(field.getsize().getx(), 0)
		#self.overhangsize = Vector.createfromvalues(self.displaysize.getx() - field.getsize().getx(),
		#																						field.getsize().gety())

		# Stores the list of buttons to process
		#self.buttonlist = control.getbuttoncollection("")
		#self.buttonlist.remove("Field")



	# -------------------------------------------------------------------
	# Adds custom colours
	# -------------------------------------------------------------------
	def setupcustomcolours(self):

		self.display.addcolour("5", 0, 0, 255)
		self.display.addcolour("6", 0, 51, 255)
		self.display.addcolour("7", 0, 102, 255)
		self.display.addcolour("8", 0, 153, 255)
		self.display.addcolour("9", 0, 204, 255)
		self.display.addcolour("10", 0, 255, 255)
		self.display.addcolour("11", 0, 255, 204)
		self.display.addcolour("12", 0, 255, 153)
		self.display.addcolour("13", 0, 255, 102)
		self.display.addcolour("14", 0, 255, 51)
		self.display.addcolour("15", 0, 255, 0)
		self.display.addcolour("16", 51, 255, 0)
		self.display.addcolour("17", 102, 255, 0)
		self.display.addcolour("18", 153, 255, 0)
		self.display.addcolour("19", 204, 255, 0)
		self.display.addcolour("20", 255, 255, 0)
		self.display.addcolour("21", 255, 204, 0)
		self.display.addcolour("22", 255, 153, 0)
		self.display.addcolour("23", 255, 102, 0)
		self.display.addcolour("24", 255, 51, 0)
		self.display.addcolour("25", 255, 0, 0)



	# -------------------------------------------------------------------
	# Adds images
	# -------------------------------------------------------------------
	def setupimages(self):

		self.display.addimage("test", None, "test", True)



	# ==========================================================================================
	# Perform Actions
	# ==========================================================================================



	# -------------------------------------------------------------------
	# Updates all elements of the screen, flips the display, then
	# removes embellishments from the field ready for the next cycle
	# -------------------------------------------------------------------

	def refreshscreen(self, currenttime, controls, scheduler, boilercontroller):

		self.drawrunway(currenttime, scheduler, boilercontroller)
#
# 		self.updatemiscanimation()
#
# 		if game.cycledisplay(control) == True:
# 			self.paintdefendersandenemies(defenderarmy, enemyarmy, field, control)
# 			self.paintstats(game)
# 			self.paintnewwaveplaque(enemyarmy, control)
# 			self.paintmanagedefenderplaque(control, defenderarmy)
# 			self.paintbuttons(control)
# 			#
		self.display.updatescreen()
# 			#
# 			self.erasebuttons(control)
# 			self.erasemanagedefenderplaque(control, field)
# 			self.erasenewwaveplaque(control, field)
# 			self.erasestats()
# 			self.erasedefendersandenemies()
#
#
#
# 	# -------------------------------------------------------------------
# 	# Replaces image with field background
# 	# -------------------------------------------------------------------
#
# 	def erase(self, position, dimensions, field):
#
# 		origin = field.convertpixeltoblock(position)
# 		offsetrange = Vector.add(field.convertpixeltoblock(dimensions), Vector.createfromvalues(1, 1))
# 		offset = Vector.createblank()
# 		for offsetx in range(0, offsetrange.getx()):
# 			for offsety in range(0, offsetrange.gety()):
# 				offset.setfromvalues(offsetx, offsety)
# 				block = Vector.add(offset, origin)
# 				if field.issingleblockonboard(block) == True:
# 					self.display.drawimage(field.getgroundtype(block), field.convertblocktopixel(block))
# 				else:
# 					self.display.drawbox(field.convertblocktopixel(block), field.getpixelblockratio(), "Black")
#
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
#
#
#
# 	# -------------------------------------------------------------------
# 	# Erases the button groups
# 	# -------------------------------------------------------------------
#
# 	def erasebuttons(self, control):
#
# 		for buttonname in self.buttonlist:
#
# 			if control.getbuttonstate(buttonname) != "Hidden":
# 				self.display.drawrectangle(control.getbuttonposition(buttonname), control.getbuttonsize(buttonname),
# 																										"Black", "", 0)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Gets a list of all defenders and ammo to paint
# 	# -------------------------------------------------------------------
#
# 	def preparedefenders(self, defenderarmy, field):
#
# 		for defenderunit in defenderarmy.units:
# 			self.actorlist.additem(defenderunit.getdisplayframereference(), defenderunit.getdisplaylocation(),
# 											defenderunit.getdisplaysize(), defenderunit.getdisplayzorder(), -999, field)
# 			if defenderunit.getammodisplaystatus() == True:
# 				self.actorlist.additem(defenderunit.getammodisplayframereference(),
# 										defenderunit.getammodisplaylocation(), defenderunit.getammodisplaysize(),
# 										defenderunit.getammodisplayzorder(), -999, field)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Prepares field selection overlay(s), if necessary
# 	# -------------------------------------------------------------------
#
# 	def preparefieldselection(self, control, field):
#
# 		displaymode = control.getfieldselectionoverlay()
# 		if displaymode != "":
# 			self.actorlist.additem(DisplayFunction.getfieldoverlayimagename(displaymode),
# 															control.getselectiondisplaylocation(),
# 															control.getselectiondisplaysize(), 100000004, -999, field)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Gets a list of all enemies to paint
# 	# -------------------------------------------------------------------
#
# 	def prepareenemies(self, enemyarmy, field):
#
# 		for enemyunit in enemyarmy.units:
# 			if enemyunit.getinplaystatus() == True:
# 				self.actorlist.additem(enemyunit.getdisplayframereference(), enemyunit.getdisplaylocation(),
# 								enemyunit.getdisplaysize(), enemyunit.getdisplayzorder(), enemyunit.gethealth(), field)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Draws defender/ammo/enemy overlay for each actor in list
# 	# -------------------------------------------------------------------
#
# 	def paintactors(self):
#
# 		for actor in self.actorlist.actors:
# 			self.display.drawimage(actor.actorname, actor.coordinates)
# 			if actor.health > -1:
# 				self.drawenemyhealth(actor.coordinates, actor.dimensions, actor.health)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Draws defender/ammo/enemy overlays
# 	# -------------------------------------------------------------------
#
# 	def paintdefendersandenemies(self, defenderarmy, enemyarmy, field, control):
#
# 		# Get list of enemies
# 		self.prepareenemies(enemyarmy, field)
#
# 		# Get list of defenders
# 		self.preparedefenders(defenderarmy, field)
#
# 		# Add selection overlays
# 		self.preparefieldselection(control, field)
#
# 		# Order defenders & enemies to give correct 3D view
# 		self.actorlist.orderactors()
#
# 		# Paint defenders & enemies
# 		self.paintactors()
#
# 		#Clear-up overhaging actors on the right of the screen
# 		self.display.drawrectangle(self.overhanglocation, self.overhangsize, "Black", "", 0)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Erases defender/ammo/enemy overlays
# 	# -------------------------------------------------------------------
#
# 	def erasedefendersandenemies(self):
#
# 		# Erase from field
# 		for block in self.actorlist.blocks:
# 			self.display.drawimage(block.blockname, block.coordinates)
#
# 		# Clear list of defenders & enemies
# 		self.actorlist.clearlists()
#

	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

 	def drawrunway(self, currenttime, scheduler, boilercontroller):


		self.display.drawrectangle(Vector.createfromvalues(0, 0), Vector.createfromvalues(480, 50), "Black", "", 0)
		self.display.drawline(Vector.createfromvalues(self.runwaystartline, 0),
													Vector.createfromvalues(self.runwaystartline, 48), "Grey", 1, "")
		currenttemp = boilercontroller.getdesiredtemperature()
		self.display.drawtext(str(currenttemp), Vector.createfromvalues(self.runwaystartline - 3, -5), "Right",
													DisplayFunction.gettemperaturecolour(currenttemp), "Desired Temp")
		lasthour = currenttime.gethour()
		offsetpixels = int(self.runwaytimescale * ((currenttime.getminute() * 60) + currenttime.getsecond()) / 3600)
		self.drawrunwaytimings(currenttime, lasthour, offsetpixels)
		self.drawrunwayinstructions(currenttime, lasthour, offsetpixels, scheduler)



	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwaytimings(self, currenttime, lasthour, offsetpixels):

		for hourindex in range(1, 12):
			hourmarker = self.runwaystartline + (hourindex * self.runwaytimescale) - offsetpixels
			hourlabel = str(Clock.convert24hourtohuman(hourindex + lasthour))
			self.display.drawline(Vector.createfromvalues(hourmarker, 0), Vector.createfromvalues(hourmarker, 15),
																										"Grey", 1, "")
			self.display.drawtext(hourlabel, Vector.createfromvalues(hourmarker + 3, 1),
																					"Left", "Grey", "Timeline Hours")
			for subindex in range(1, 4):
				pixelposition = hourmarker - int(subindex * self.runwaytimescale / 4)
				if self.runwaystartline < pixelposition:
					lineheight = 3 * ((subindex + 1) % 2)
					self.display.drawline(Vector.createfromvalues(pixelposition, 0),
													Vector.createfromvalues(pixelposition, lineheight), "Grey", 1, "")



	# -------------------------------------------------------------------
	# Paints the scheduled settings at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwayinstructions(self, currenttime, lasthour, offsetpixels, scheduler):

		scheduledtimes = scheduler.getscheduledtimes()
		for scheduledtime in scheduledtimes:
			scheduledtimevalue = scheduledtime.getvalue()
			if scheduledtimevalue < currenttime.getvalue():
				scheduledtimevalue = scheduledtimevalue + (24 * 3600)
			houroffset = scheduledtimevalue - (3600 * lasthour)
			pixelposition = self.runwaystartline + int(houroffset * self.runwaytimescale / 3600) - offsetpixels

			self.display.drawline(Vector.createfromvalues(pixelposition, 18),
								  Vector.createfromvalues(pixelposition, 48),
								  "Grey", 1, "")
			tempvalue = scheduler.getscheduledinstruction(scheduledtime)
			self.display.drawtext(str(tempvalue), Vector.createfromvalues(pixelposition + 3, 19), "Left",
													DisplayFunction.gettemperaturecolour(tempvalue), "Timeline Temps")

#
#
#
# 	# -------------------------------------------------------------------
# 	# Displays the game stats such as wave, coins and crystals
# 	# -------------------------------------------------------------------
#
# 	def paintstats(self, game):
#
# 		# Wave
# 		self.display.drawtext("Wave " + str(game.getwave()), Vector.createfromvalues(621, 52), "Left", "Yellow", "20")
#
# 		# Crystals
# 		self.display.drawimage("Crystal - " + DisplayFunction.getcrystalanimationframe(self.miscanimationclock, game),
# 																					Vector.createfromvalues(621, 76))
# 		self.display.drawtext(str(game.getcrystalcount()), Vector.createfromvalues(654, 82), "Left",
# 																	DisplayFunction.getcrystalcountcolour(game), "20")
#
# 		# Coins
# 		self.display.drawimage("Coin - " + DisplayFunction.getcoinanimationframe(self.miscanimationclock, game),
# 																					Vector.createfromvalues(621, 106))
# 		self.display.drawtext(str(game.getcoincount()), Vector.createfromvalues(654, 112), "Left",
# 																	DisplayFunction.getcoincountcolour(game), "20")
#
#
#
# 	# -------------------------------------------------------------------
# 	# Displays the game stats such as wave, coins and crystals
# 	# -------------------------------------------------------------------
#
# 	def erasestats(self):
#
# 		self.display.drawrectangle(Vector.createfromvalues(620, 50), Vector.createfromvalues(100, 100), "Black", "", 0)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Displays the new wave plaque
# 	# -------------------------------------------------------------------
#
# 	def paintnewwaveplaque(self, enemyarmy, control):
#
# 		if control.getbetweenwavestate() == True:
# 			self.display.drawimage("Plaque", DisplayFunction.getwaveplaqueposition(0, 0))
# 			self.display.drawtext("Next Wave!", DisplayFunction.getwaveplaqueposition(100, 17),
# 																							"Centre", "Yellow", "20")
# 			self.display.drawcircle(DisplayFunction.getwaveplaqueposition(100, 97), 46, "Dirty Purple", "", 0)
# 			self.display.drawimage(enemyarmy.getname() + " - S" +
# 													DisplayFunction.getplaqueanimationframe(self.miscanimationclock),
# 													DisplayFunction.getwaveplaqueposition(68, 66))
# 			self.display.drawtext(enemyarmy.getname(), DisplayFunction.getwaveplaqueposition(100, 162),
# 																							"Centre", "Yellow", "20")
# 			self.display.drawtext(enemyarmy.getinitialhealth(), DisplayFunction.getwaveplaqueposition(100, 192),
# 																							"Centre", "Yellow", "20")
#
#
#
# 	# -------------------------------------------------------------------
# 	# Erases the new wave plaque
# 	# -------------------------------------------------------------------
#
# 	def erasenewwaveplaque(self, control, field):
#
# 		if control.getbetweenwavestate() == True:
# 			self.erase(DisplayFunction.getwaveplaqueposition(0, 0), Vector.createfromvalues(210, 310), field)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Displays manage defender plaque
# 	# -------------------------------------------------------------------
#
# 	def paintmanagedefenderplaque(self, control, defenderarmy):
#
# 		if control.getbuttonstate("Cancel") != "Hidden":
#
# 			overlayposition = control.getmanagedefenderoverlayposition()
# 			overlaytitle = control.getfieldselectionoverlay() + " Defender"
#
# 			self.display.drawimage("Manage", DisplayFunction.getdefenderplaqueposition(overlayposition, 0, 0))
# 			self.display.drawtext(overlaytitle, DisplayFunction.getdefenderplaqueposition(overlayposition, 100, 17),
# 																							"Centre", "Yellow", "20")
#
#
#
#
# 			#self.display.drawimage("Coin - 0", Vector.createfromvalues(621, 210))
# 			#self.display.drawtext(str(defenderarmy.getdefenderupgradecost()), Vector.createfromvalues(654, 210),
# 			#																					"Left", "Yellow", "20")
#
# #			self.draw.circle(Vector.createfromvalues(303, 230), 46, "Dirty Purple")
# #			self.draw.image(enemyarmy.getname() + " - S" + self.getplaqueanimationframe(), Vector.createfromvalues(271, 199))
# #			self.draw.text(enemyarmy.getname(), Vector.createfromvalues(303, 295), "Centre", "Yellow")
# #			self.draw.text(enemyarmy.getinitialhealth(), Vector.createfromvalues(303, 325), "Centre", "Yellow")
#
#
#
# 	# -------------------------------------------------------------------
# 	# Erases the add or upgrade defender plaque
# 	# -------------------------------------------------------------------
#
# 	def erasemanagedefenderplaque(self, control, field):
#
# 		if control.getbuttonstate("Cancel") != "Hidden":
#
# 			overlayposition = control.getmanagedefenderoverlayposition()
#
# 			self.erase(DisplayFunction.getdefenderplaqueposition(overlayposition, 0, 0),
# 																		Vector.createfromvalues(210, 210), field)
#
#
#
# 	# -------------------------------------------------------------------
# 	# Paints the whole field background
# 	# -------------------------------------------------------------------
#
# 	def paintwholefield(self, field):
#
# 		currentposition = Vector.createblank()
# 		screenrange = field.getblocksize()
# 		for currentpositionx in range(0, screenrange.getx()):
# 			for currentpositiony in range(0, screenrange.gety()):
# 				currentposition.setfromvalues(currentpositionx, currentpositiony)
# 				self.display.drawimage(field.getgroundtype(currentposition), field.convertblocktopixel(currentposition))
#
#
#
# 	# -------------------------------------------------------------------
# 	# Updates the misc item animation clock
# 	# -------------------------------------------------------------------
#
# 	def updatemiscanimation(self):
#
# 		# Deplete the clock, and recharge if it is at zero
# 		if self.miscanimationclock.deplete(1) == True:
# 			self.miscanimationclock.recharge()
#
#
#
#
# 	# ==========================================================================================
# 	# Get Information
# 	# ==========================================================================================
#
