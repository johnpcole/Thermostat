#from ..common_components.scale_datatype import scale_module as Scale
from ..common_components.vector_datatype import vector_module as Vector
from ..common_components.appdisplay_framework import appdisplay_module as AppDisplay
#from displayactors_subcomponent import displayactors_module as DisplayActorList
from . import display_privatefunctions as DisplayFunction
from ..common_components.clock_datatype import clock_module as Clock


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

		self.display.addcolour("27", 178, 0, 0)
		self.display.addcolour("26", 216, 0, 0)
		self.display.addcolour("25", 255, 38, 38)
		self.display.addcolour("24", 247, 73, 29)
		self.display.addcolour("23", 239, 108, 21)
		self.display.addcolour("22", 232, 144, 13)
		self.display.addcolour("21", 224, 180, 6)
		self.display.addcolour("20", 216, 216, 0)
		self.display.addcolour("19", 180, 224, 6)
		self.display.addcolour("18", 144, 232, 13)
		self.display.addcolour("17", 108, 239, 21)
		self.display.addcolour("16", 73, 247, 29)
		self.display.addcolour("15", 38, 255, 38)
		self.display.addcolour("14", 29, 242, 71)
		self.display.addcolour("13", 20, 229, 104)
		self.display.addcolour("12", 13, 216, 135)
		self.display.addcolour("11", 6, 204, 164)
		self.display.addcolour("10", 0, 191, 191)
		self.display.addcolour("9", 6, 164, 204)
		self.display.addcolour("8", 13, 135, 216)
		self.display.addcolour("7", 20, 104, 229)
		self.display.addcolour("6", 29, 71, 242)
		self.display.addcolour("5", 38, 38, 255)
		self.display.addcolour("4", 0, 0, 216)
		self.display.addcolour("3", 0, 0, 178)



	# -------------------------------------------------------------------
	# Adds images
	# -------------------------------------------------------------------

	def setupimages(self):

		self.display.addimage("test", None, "test", True)



	# -------------------------------------------------------------------
	# Adds fonts
	# -------------------------------------------------------------------

	def setupfonts(self):

		self.display.addfont("Timeline Hours", "", "Font", 14)
		self.display.addfont("Timeline Temps", "", "Font", 28)
		self.display.addfont("Desired Temp", "", "Font", 54)
		self.display.addfont("Actual Temp", "", "Font", 148)



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


# 		self.updatemiscanimation()
#
# 		if game.cycledisplay(control) == True:
# 			self.paintdefendersandenemies(defenderarmy, enemyarmy, field, control)
# 			self.paintstats(game)
# 			self.paintnewwaveplaque(enemyarmy, control)
# 			self.paintmanagedefenderplaque(control, defenderarmy)
# 			self.paintbuttons(control)

 		# Refresh screen
		self.display.updatescreen()

		# Blank out area
		self.display.drawrectangle(Vector.createfromvalues(0, 0), Vector.createfromvalues(480, 240), "Black", "", 0)

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

	def drawboard(self, boilercontroller):

		xpos = 260
		ypos = 40
		degreeoffset = 100

		# Get current temperature
		tempvalue = max(0, boilercontroller.getcurrenttemperature())
		integervalue = int(tempvalue)
		fractionpart = str(tempvalue - float(integervalue))
		fractionpart = fractionpart[1:3]
		integerpart = str(integervalue)

		# Draw current temperature
		self.display.drawtext(integerpart,
							  Vector.createfromvalues(xpos, ypos),
							  "Right",
							  DisplayFunction.gettemperaturecolour(tempvalue),
							  "Actual Temp")

		self.display.drawtext(fractionpart,
							  Vector.createfromvalues(xpos, ypos),
							  "Left",
							  DisplayFunction.gettemperaturecolour(tempvalue),
							  "Actual Temp")

		self.display.drawtext("O",
							  Vector.createfromvalues(xpos+degreeoffset, ypos+35),
							  "Left",
							  DisplayFunction.gettemperaturecolour(tempvalue),
							  "Timeline Hours")

		self.display.drawtext("C",
							  Vector.createfromvalues(xpos+degreeoffset+10, ypos+35),
							  "Left",
							  DisplayFunction.gettemperaturecolour(tempvalue),
							  "Timeline Temps")






	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

 	def drawrunway(self, currenttime, scheduler, boilercontroller):


		# Display current desired temperature
		currenttemp = boilercontroller.getdesiredtemperature()
		self.display.drawtext(	str(currenttemp),
								Vector.createfromvalues(self.runwaystartline - 5, -3),
								"Right",
								DisplayFunction.gettemperaturecolour(currenttemp),
								"Desired Temp")

		# The current hour
		lasthour = currenttime.gethour()

		# Number of pixels markers are shifted left
		offsetpixels = int(self.runwaytimescale * ((currenttime.getminute() * 60) + currenttime.getsecond()) / 3600)

		# Draw hour/half/quarter markers
		self.drawrunwaytimings(currenttime, lasthour, offsetpixels)

		# Draw upcoming desired temperatures (from schedule)
		self.drawrunwayinstructions(currenttime, lasthour, offsetpixels, scheduler)

		# Draw the current time main marker
		self.display.drawline(Vector.createfromvalues(self.runwaystartline, 0),
								Vector.createfromvalues(self.runwaystartline, 48),
								"Grey",
								1,
								"")

		# Draw the runway edge
		#self.display.drawline(Vector.createfromvalues(0, 49),
		#						Vector.createfromvalues(480, 49),
		#						"Grey",
		#						1,
		#						"")



	# -------------------------------------------------------------------
	# Paints the timeline at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwaytimings(self, currenttime, lasthour, offsetpixels):

		# Display the current hour at the current time marker only if it's exactly on the clock
		if currenttime.getminute() == 0:
			self.display.drawtext(Clock.convert24hourtohuman(lasthour),
									Vector.createfromvalues(self.runwaystartline + 3, 1),
									"Left",
									"Grey",
									"Timeline Hours")

		# Print the hour/half/quarter markers for twelve hours
		for hourindex in range(1, 14):

			# Position of hour marker line
			hourmarker = self.runwaystartline + (hourindex * self.runwaytimescale) - offsetpixels

			# Draw hour marker line
			self.display.drawline(Vector.createfromvalues(hourmarker, 0),
									Vector.createfromvalues(hourmarker, 15),
									"Grey",
									1,
									"")

			# Draw hour marker number
			self.display.drawtext(Clock.convert24hourtohuman(hourindex + lasthour),
									Vector.createfromvalues(hourmarker + 3, 1),
									"Left",
									"Grey",
									"Timeline Hours")

			# Draw the half & quarter markers
			for subindex in range(1, 4):

				# Position of marker
				pixelposition = hourmarker - int(subindex * self.runwaytimescale / 4)

				# Only draw marker if it's to the right of the current time marker
				if self.runwaystartline < pixelposition:

					# Set height of marker lines
					lineheight = 3 * ((subindex + 1) % 2)

					# Draw the marker line
					self.display.drawline(Vector.createfromvalues(pixelposition, 0),
											Vector.createfromvalues(pixelposition, lineheight),
											"Grey",
											1,
											"")



	# -------------------------------------------------------------------
	# Paints the scheduled settings at the top of the screen
	# -------------------------------------------------------------------

	def drawrunwayinstructions(self, currenttime, lasthour, offsetpixels, scheduler):

		# Get list of scheduled times
		scheduledtimes = scheduler.getscheduledtimes()

		# Loop over scheduled times
		for scheduledtime in scheduledtimes:

			# Get integer schedule time value
			scheduledtimevalue = scheduledtime.getvalue()

			# If the scheduled time is earlier than current time, add 24 hours so it appears in the future
			if scheduledtimevalue <= currenttime.getvalue():
				scheduledtimevalue = scheduledtimevalue + (24 * 3600)

			# Position of marker
			houroffset = scheduledtimevalue - (3600 * lasthour)
			pixelposition = self.runwaystartline + int(houroffset * self.runwaytimescale / 3600) - offsetpixels

			# Draw marker
			self.display.drawline(Vector.createfromvalues(pixelposition, 18),
								 	Vector.createfromvalues(pixelposition, 48),
								 	"Grey",
								 	1,
								 	"")

			# Get desired temperature
			tempvalue = scheduler.getscheduledinstruction(scheduledtime)

			# Draw desired temperature number
			self.display.drawtext(str(tempvalue),
									Vector.createfromvalues(pixelposition + 3, 19),
									"Left",
									DisplayFunction.gettemperaturecolour(tempvalue),
									"Timeline Temps")

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
