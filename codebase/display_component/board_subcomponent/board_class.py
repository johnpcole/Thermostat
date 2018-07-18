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

		self.snoozeoffset = Vector.add(Vector.createfromvalues(78, 15), self.flameposition)

		# Data for capturing the animation of the current temperature
		self.boilerstate = Transition.createupdowntransition(500, 1500, False)

		self.flamestate = "Hidden"



	def updateboardlayout(self, boilerstatus):

		if (boilerstatus[:2] == "On") or (boilerstatus[-10:] == "n Override"):
			outcome = True
		else:
			outcome = False

		self.boilerstate.updatevalue(outcome)

		self.updateflamemode(boilerstatus)



	def drawcurrenttemperature(self, currenttemperature):

		outcome = {}

		integerpart, fractionpart, colour, currentposition = self.gettemperaturecomponents(currenttemperature)

		# Draw current temperature
		outcome["Integer"] = ("Text", str(integerpart), currentposition, "Right", colour, "Actual Temp")
		outcome["Fraction"] = ("Text", (str(fractionpart))[1:3], currentposition, "Left", colour, "Actual Temp")
		outcome["Degree"] = ("Text", "O", Vector.add(currentposition, self.degreesoffset), "Left", colour, "Timeline Hours")
		outcome["Celcius"] = ("Text", "C", Vector.add(currentposition, self.celciusoffset), "Left", colour, "Timeline Temps")

		return outcome



	def drawflame(self, snoozetimer):

		outcome = {}

		flamemode = self.flamestate

		if flamemode != "Hidden":
			outcome["Flame Base"] = ("Image", "flame_base", self.flameposition)
			if flamemode == "Snooze":
				outcome["Flame 1"] = ("Image", "flame_disable", self.flameposition)
				outcome["Overlay Clock"] = ("Image", "flame_snooze", self.flameposition)
				if snoozetimer < 1:
					outcome["Overlay Text"] = ("Text", str(abs(snoozetimer)), self.snoozeoffset, "Centre", "Snooze", "Snooze")
			elif flamemode == "On":
				frame = self.getflameframe()
				outcome["Flame 1"] = ("Image", "flame_" + str(frame + 3), self.flameposition)
				outcome["Flame 2"] = ("Image", "flame_" + str(frame), self.flameposition)
			elif flamemode == "Transitioning":
				outcome["Flame 1"] = ("Image", self.getflametransition(), self.flameposition)
			elif flamemode == "Forced":
				frame = self.getflameframe()
				outcome["Flame 1"] = ("Image", "flame_" + str(frame + 1), self.flameposition)
				outcome["Overlay Clock"] = ("Image", "flame_snooze", self.flameposition)
				if snoozetimer < 1:
					outcome["Overlay Text"] = ("Text", str(abs(snoozetimer)), self.snoozeoffset, "Centre", "Snooze", "Snooze")

		return outcome



	def gettemperaturecomponents(self, temperature):

		integerpart = int(temperature)
		fractionpart = abs(temperature - float(integerpart))
		colour = DisplayFunction.gettemperaturecolour(integerpart)

		transitionfraction = self.boilerstate.gettransitionfraction()

		positionoffset = DisplayFunction.gettwowaytransitionposition(self.offtemperatureorigin,
																		self.ontemperatureorigin, transitionfraction)

		currentposition = Vector.createfromvalues(positionoffset, self.temperaturetop)


		return integerpart, fractionpart, colour, currentposition



	def getflameframe(self):

		frame = (Clock.getnow().getvalue() % 4)
		if frame == 3:
			frame = 1
		return frame



	def getflametransition(self):

		transitionfraction = self.boilerstate.gettransitionfraction()

		return ("flame_" + str(int((transitionfraction - 0.2) * 7.49)))



	def updateflamemode(self, boilerstatus):

		transitionfraction = self.boilerstate.gettransitionfraction()

		outcome = self.flamestate
		if transitionfraction > 0.2:
			if boilerstatus[-10:] == "f Override":
				outcome = "Snooze"
			else:
				if transitionfraction == 1.0:
					if boilerstatus[-10:] == "n Override":
						outcome = "Forced"
					else:
						outcome = "On"
						if self.flamestate == "Snooze":
							self.boilerstate.resettransition()
				else:
					if self.flamestate != "Snooze":
						outcome = "Transitioning"
		else:
			if transitionfraction > 0:
				outcome = "Off"
			else:
				outcome = "Hidden"

		self.flamestate = outcome

		return self.flamestate