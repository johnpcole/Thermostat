from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from ...common_components.transition_datatype import transition_module as Transition
from .. import display_privatefunctions as DisplayFunction


class DefineBoard:

	def __init__(self):

		self.temperaturetop = 40

		self.offtemperatureorigin = 260

		self.ontemperatureorigin = 310

		self.degreesoffset = Vector.createfromvalues(100, 35)

		self.celciusoffset = Vector.add(Vector.createfromvalues(10, 0), self.degreesoffset)

		self.flameposition = Vector.createfromvalues(30, 71)

		# Data for capturing the animation of the current temperature
		self.boilerstate = Transition.createupdowntransition(500, 1500, False)




	def updateboardlayout(self, boilercontroller):

		self.boilerstate.updatevalue(self.getflamemode(boilercontroller.getstatus()))



	def drawcurrenttemperature(self, boilercontroller):

		outcome = {}

		integerpart, fractionpart, colour = self.gettemperaturecomponents(boilercontroller.getcurrenttemperature())

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



	def drawflame(self, boilercontroller):

		outcome = {}

		transitionfraction = self.boilerstate.gettransitionfraction()

		if transitionfraction > 0:
			outcome["Flame Base"] = ("Image", "flame_base", self.flameposition)
		if transitionfraction > 0.2:
			if (boilercontroller.getstatus())[-6:] == "Snooze":
				outcome["Flame 0"] = ("Image", "flame_snooze", self.flameposition)
			else:
				if transitionfraction == 1.0:
					frame = self.getflameframe()
					outcome["Flame 2"] = ("Image", "flame_" + str(frame), self.flameposition)
					if (boilercontroller.getstatus())[-6:] != "Extend":
						outcome["Flame 1"] = ("Image", "flame_" + str(frame + 3), self.flameposition)
					else:
						outcome["Overlay Clock"] = ("Image", "flame_extend", self.flameposition)
				else:
					outcome["Flame 3"] = ("Image", self.getflametransition(transitionfraction), self.flameposition)
		return outcome



	def gettemperaturecomponents(self, temperature):

		integerpart = int(temperature)
		fractionpart = abs(temperature - float(integerpart))
		colour = DisplayFunction.gettemperaturecolour(integerpart)

		return integerpart, fractionpart, colour



	def getflamemode(self, boilerstatus):

		if (boilerstatus[:2] == "On") or (boilerstatus[-6:] == "Extend"):
			return True
		else:
			return False


	def getflameframe(self):

		frame = (Clock.getnow().getvalue() % 4)
		if frame == 3:
			frame = 1
		return frame

	def getflametransition(self, fraction):

		return ("flame_" + str(int((fraction - 0.2) * 7.49)))