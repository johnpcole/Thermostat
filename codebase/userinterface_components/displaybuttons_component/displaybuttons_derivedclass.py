from ...common_components.vector_datatype import vector_module as Vector
#from ....common_components.clock_datatype import clock_module as Clock
#from ....common_components.transition_datatype import transition_module as Transition
from .. import display_sharedfunctions as DisplayFunction
from . import buttonmetrics_baseclass as Metrics



class DefineButtons(Metrics.DefineButtonMetrics):

	def __init__(self, controls):

		# Get the metrics using baseclass method
		Metrics.DefineButtonMetrics.__init__(self)

		# The list of start menu buttons
		self.startmenubuttons = controls.getbuttoncollection("Set Temp")

		# The list of configure schedule buttons
		self.configuremenubuttons = controls.getbuttoncollection("Schedule Group")

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

						if temperature == 3:
							outcome["Slider Outline"] = ("Image", "slider_outline", Vector.add(boxposition, self.slideroutlineoffset))

					outcome["Options Link"] = ("Line", Vector.createfromvalues(30, 175), Vector.createfromvalues(450, 175), "White", 1, "")


				else:

					buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour, outline = self.calcbuttonmetrics(control, buttonname, selectorvalue)

					outcome[buttonname + " Logo"] = ("Image", imagename, buttonlocation)
					outcome[buttonname + " Fill"] = ("Box", buttonoverlaylocation, buttonoverlaysize, buttoncolour, "", 0)
					outcome[buttonname + " Outline"] = ("Image", outline, buttonlocation)

		return outcome



	def drawconfiguremenu(self, control, schedule):

		outcome = {}

		selectordata = control.gettimelineselectordata()
		slidervalue = selectordata.getsliderhourvalue()

		for buttonname in self.configuremenubuttons:
			if control.getbuttonstate(buttonname) != "Hidden":

				if buttonname == "Timeline Slider":

					outcome["Slider Outline"] = ("Image", "slider_outline", self.timesliderposition)

					for hourindex in range(0, 25):

						rangemin, rangemax = self.calculatemarkrange(hourindex, slidervalue)

						for subindex in range(rangemin, rangemax):

							markertop, markerbottom, labelposition, hourlabel, indexer, fontsize, colour = self.calctimeslidertimemetrics(hourindex, subindex, slidervalue)

							outcome["Slider Time Marker " + indexer] = ("Line", markertop, markerbottom, colour, 1, "")
							if fontsize != "Hide":
								outcome["Slider Time Label " + indexer] = ("Text", hourlabel, labelposition, "Left", colour, fontsize)

					for instructiontime in schedule.getscheduledtimes():

						markertop, markerbottom, labelposition, templabel, indexer, fontsize, colour = self.calctimeslidertempmetrics(instructiontime.getsecondlessvalue(), schedule.getscheduledinstruction(instructiontime), slidervalue)

						outcome["Slider Temp Marker " + indexer] = ("Line", markertop, markerbottom, colour, 1, "")

				else:

					buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour, outline = self.calcbuttonmetrics(control, buttonname, "")

					if imagename != "Hide":
						outcome[buttonname + " Logo"] = ("Image", imagename, buttonlocation)
					outcome[buttonname + " Fill"] = ("Box", buttonoverlaylocation, buttonoverlaysize, buttoncolour, "", 0)
					outcome[buttonname + " Outline"] = ("Image", outline, buttonlocation)

		return outcome


