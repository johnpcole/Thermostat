from ...common_components.vector_datatype import vector_module as Vector
#from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.transition_datatype import transition_module as Transition
from .. import display_privatefunctions as DisplayFunction


class DefineBoard:

	def __init__(self):

		self.temperaturetop = 40

		self.offtemperatureorigin = 260

		self.ontemperatureorigin = 335

		self.degreesoffset = Vector.createfromvalues(100, 35)

		self.celciusoffset = Vector.add(Vector.createfromvalues(10, 0), self.degreesoffset)

		# Data for capturing the animation of the current temperature
		self.boilerstate = Transition.createupdowntransition(500, 500, False)




	def drawcurrenttemperature(self, boilercontroller):

		outcome = {}

		temperature = max(0, boilercontroller.getcurrenttemperature())

		integerpart = int(temperature)
		fractionpart = temperature - float(integerpart)
		colour = DisplayFunction.gettemperaturecolour(integerpart)
		self.boilerstate.updatevalue(boilercontroller.getboilerstatus())

		transitionfraction = self.boilerstate.gettransitionfraction()

		positionoffset = DisplayFunction.gettwowaytransitionposition(self.offtemperatureorigin,
																		self.ontemperatureorigin, transitionfraction)

		currentposition = Vector.createfromvalues(positionoffset, self.temperaturetop)

		# Draw current temperature
		outcome["Integer"] = ("Text", str(integerpart), currentposition, "Right", colour, "Actual Temp")
		outcome["Fraction"] = ("Text", (str(fractionpart))[1:3], currentposition, "Left", colour, "Actual Temp")
		outcome["Degree"] = ("Text", "O", Vector.add(currentposition, self.degreesoffset), "Left", colour, "Timeline Hours")
		outcome["Celcius"] = ("Text", "C", Vector.add(currentposition, self.celciusoffset), "Left", colour, "Timeline Temps")

		return outcome

