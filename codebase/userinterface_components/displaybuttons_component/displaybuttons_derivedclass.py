from ...common_components.vector_datatype import vector_module as Vector
from .. import display_sharedfunctions as DisplayFunction
from . import buttonmetrics_baseclass as Metrics



class DefineButtons(Metrics.DefineButtonMetrics):

	def __init__(self, controls):

		# Get the metrics using baseclass method
		Metrics.DefineButtonMetrics.__init__(self, controls)

		# The list of start menu buttons
		self.startmenubuttons = controls.getbuttoncollection("Set Temp")

		# The list of configure schedule buttons
		self.configuremenubuttons = controls.getbuttoncollection("Schedule Group")

		# The list of configure instruction buttons
		self.instructionmenubuttons = controls.getbuttoncollection("Instruction Config")

		# The current buttons display definition
		self.artefacts = {}


	# -------------------------------------------------------------------
	# Build the Buttons
	# -------------------------------------------------------------------

	def buildbuttons(self, boilercontroller, usercontrols):

		self.artefacts = {}

		# Display the blanking out overlay
		newitems = self.drawmodaloverlay(usercontrols)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons A"))

		# Draw the main menu buttons
		newitems = self.drawstartmenu(usercontrols, boilercontroller.getcurrentdesiredtemperature())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons B"))

		# Draw the configuration menu buttons
		newitems = self.drawconfiguremenu(usercontrols, boilercontroller.getschedule())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons C"))

		# Draw the instruction menu buttons
		newitems = self.drawinstructionmenu(usercontrols)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons D"))

		return self.artefacts



	def drawmodaloverlay(self, control):

		outcome = {}

		if control.getbuttonstate("Start Menu") == "Hidden":
			outcome["Background Overlay"] = ("Image", "start_disabled", self.origin)

		return outcome



	def drawstartmenu(self, control, currentdesiredtemperature):

		outcome = {}

		selectordata = control.gettempselectordata()
		slidervalue = selectordata.getslidervalue()
		selectorvalue = selectordata.getselectedtime()

		for buttonname in self.startmenubuttons:
			if control.getbuttonstate(buttonname) != "Hidden":

				if buttonname == "Temp Slider":

					for temperature in range(3, 28):

						temp, boxposition, boxsize, boxcentre, boxfont = self.calctempslidermetrics(temperature, slidervalue)

						outcome["Slider Background " + temp] = ("Box", boxposition, boxsize, temp, "", 0)

						if (temperature == slidervalue) or (temperature == int(currentdesiredtemperature)):
							outcome["Slider Text " + temp] = ("Text", temp, boxcentre, "Centre", "Black", boxfont)
							#outcome["Slider Highlight " + temp] = ("Box", boxposition, boxsize, "", "Black", 1)


					linkstart, linkend = self.calctempslidermisc()
					outcome["Options Link"] = ("Line", linkstart, linkend, "White", 1, "")

				buttonlocation, buttonsize, imagename, buttoncolour = self.calcbuttonmetrics(control, buttonname, selectorvalue)
				outcome = self.drawgenericbuttonarea(outcome, buttonlocation, buttonsize, buttoncolour, "White", imagename, buttonname)

		return outcome



	def drawconfiguremenu(self, control, schedule):

		outcome = {}

		selectordata = control.gettimelineselectordata()
		slidervalue = selectordata.getsliderhourvalue()

		for buttonname in self.configuremenubuttons:
			if control.getbuttonstate(buttonname) != "Hidden":

				if buttonname == "Timeline Slider":

					for hourindex in range(0, 25):
						rangemin, rangemax = self.calctimeslidermarkrange(hourindex, slidervalue)

						for subindex in range(rangemin, rangemax):

							markertop, markerbottom, labelposition, hourlabel, indexer, fontsize, colour = self.calctimeslidertimemetrics(hourindex, subindex, slidervalue)
							outcome["Slider Time Marker " + indexer] = ("Line", markertop, markerbottom, colour, 1, "")
							if fontsize != "Hide":
								outcome["Slider Time Label " + indexer] = ("Text", hourlabel, labelposition, "Left", colour, fontsize)

					for instructiontime in schedule.getscheduledtimes():
						markertop, markerbottom, labelposition, templabel, indexer, fontsize, colour = self.calctimeslidertempmetrics(instructiontime.getsecondlessvalue(), schedule.getscheduledinstruction(instructiontime), slidervalue)
						outcome["Slider Temp Marker " + indexer] = ("Line", markertop, markerbottom, colour, 1, "")

				buttonlocation, buttonsize, imagename, buttoncolour = self.calcbuttonmetrics(control, buttonname, "")

				if buttonname[:16] == "Schedule Select ":
					timetext, temptext, timeposition, tempposition = self.calcschedulebuttonmetrics(buttonlocation, buttonsize, selectordata, buttonname)
					outcome[buttonname + " Text 1"] = ("Text", timetext, timeposition, "Centre", "White", "Button Temps")
					outcome[buttonname + " Text 2"] = ("Text", temptext, tempposition, "Centre", "White", "Button Temps")

				outcome = self.drawgenericbuttonarea(outcome, buttonlocation, buttonsize, buttoncolour, "White", "Hide", buttonname)

		return outcome



	def drawinstructionmenu(self, control):

		outcome = {}

		selectordata = control.getinstructionselectordata()

		for buttonname in self.instructionmenubuttons:
			if control.getbuttonstate(buttonname) != "Hidden":

				if buttonname[:19] == "Instruction Slider ":

					print selectordata.getslidervalue("Hour"), selectordata.getslidervalue("Min"), selectordata.getslidervalue("Temp")

				buttonlocation, buttonsize, imagename, buttoncolour = self.calcbuttonmetrics(control, buttonname, "")
				outcome = self.drawgenericbuttonarea(outcome, buttonlocation, buttonsize, buttoncolour, "White", imagename, buttonname)

		return outcome



	def drawgenericbuttonarea(self, existingdefinitionlist, position, size, backgroundcolour, linecolour, imagename, labelling):

		areadefinitions = {}

		topleft = Vector.createfromvector(position)
		bottomright = Vector.subtract(Vector.add(position, size), Vector.createfromvalues(1, 1))

		# Main Lines

		for index in ("First_and_Second", "Third_and_Fourth"):

			if index == "First_and_Second":
				lookup = Vector.createfromvector(topleft)
			else:
				lookup = Vector.createfromvector(bottomright)

			firststart = Vector.createfromvalues(topleft.getx() + 4, lookup.gety())
			firstend = Vector.createfromvalues(bottomright.getx() - 4, lookup.gety())
			areadefinitions[labelling + " Outline " + index + " 1"] = ("Line", firststart, firstend, linecolour, 1, "")

			secondstart = Vector.createfromvalues(lookup.getx(), topleft.gety() + 4)
			secondend = Vector.createfromvalues(lookup.getx(), bottomright.gety() - 4)
			areadefinitions[labelling + " Outline " + index + " 2"] = ("Line", secondstart, secondend, linecolour, 1, "")

		# Rounded Corners
		for index in ("topleft", "topright", "bottomleft", "bottomright"):

			xbase, xsign, ybase, ysign = self.calcroundedcorneranchors(topleft, bottomright, index)

			fourthstartandend = Vector.createfromvalues(xbase + xsign, ybase + ysign)
			areadefinitions[labelling + " Outline " + index + " corner"] = ("Line", fourthstartandend, fourthstartandend, "Black", 1, "")

			for mode in ("vertical", "horizontal"):

				startxoffset, startyoffset, endxoffset, endyoffset = self.calcroundedcorneroffsets(mode)

				thirdstart = Vector.createfromvalues(xbase + (xsign * startxoffset), ybase + (ysign * startyoffset))
				thirdend = Vector.createfromvalues(xbase + (xsign * endxoffset), ybase + (ysign * endyoffset))
				areadefinitions[labelling + " Outline " + index + " " + mode] = ("Line", thirdstart, thirdend, linecolour, 1, "")

		if imagename != "Hide":
			areadefinitions[labelling + " Logo"] = ("Image", imagename, position)

		if backgroundcolour != "None":
			fillposition = Vector.createfromvalues(position.getx() + 1, position.gety() + 1)
			fillsize = Vector.createfromvalues(size.getx() - 2, size.gety() - 2)
			areadefinitions[labelling + " Fill"] = ("Box", fillposition, fillsize, backgroundcolour, "", 0)

		outcome = existingdefinitionlist.copy()
		outcome.update(areadefinitions)

		return outcome
