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

		# The current buttons display definition
		self.artefacts = {}


	# -------------------------------------------------------------------
	# Build the Buttons
	# -------------------------------------------------------------------

	def buildbuttons(self, boilercontroller, usercontrols):

		self.artefacts = {}

		# Display current desired temperature
		newitems = self.drawmodaloverlay(usercontrols)
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons A"))

		# Draw upcoming desired temperatures (from schedule)
		newitems = self.drawstartmenu(usercontrols, boilercontroller.getcurrentdesiredtemperature())
		self.artefacts.update(DisplayFunction.prefixdictionarykeys(newitems, "Buttons B"))

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

						temp, boxposition, boxsize, boxcentre, boxfont = self.calcslidermetrics(temperature, slidervalue)

						outcome["Slider Background " + temp] = ("Box", boxposition, boxsize, temp, "", 0)

						if (temperature == slidervalue) or (temperature == int(currentdesiredtemperature)):
							outcome["Slider Text " + temp] = ("Text", temp, boxcentre, "Centre", "Black", boxfont)
							#outcome["Slider Highlight " + temp] = ("Box", boxposition, boxsize, "", "Black", 1)

						if temperature == 3:
							outcome["Slider Outline"] = ("Image", "slider_outline", Vector.add(boxposition, self.slideroutlineoffset))

				else:

					buttonlocation, buttonsize, buttonoverlaylocation, buttonoverlaysize, imagename, buttoncolour = self.calcbuttonmetrics(control, buttonname, selectorvalue)

					outcome[buttonname + " Logo"] = ("Image", imagename, buttonlocation)
					outcome[buttonname + " Fill"] = ("Box", buttonoverlaylocation, buttonoverlaysize, buttoncolour, "", 0)
					outcome[buttonname + " Outline"] = ("Image", "button_outline", buttonlocation)

		return outcome

