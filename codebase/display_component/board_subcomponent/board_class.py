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



	def updateboardlayout(self, boilerswitchstatus, thermostatstatus):

		if (boilerswitchstatus == True) or (thermostatstatus == True):
			outcome = True
		else:
			outcome = False

		self.boilerstate.updatevalue(outcome)

		self.updateflamemode(boilerswitchstatus, thermostatstatus)



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
				if snoozetimer > 0:
					outcome["Overlay Text"] = ("Text", str(snoozetimer), self.snoozeoffset, "Centre", "Snooze", "Snooze")
			elif flamemode == "On":
				for flameversion in range(1,5):
					framename, flameframe = self.getflameframe(flameversion)
					if flameframe != "":
						outcome[framename] = ("Image", flameframe, self.flameposition)
			elif flamemode == "Transitioning":
				outcome["Flame 1"] = ("Image", self.getflametransition(), self.flameposition)
			elif flamemode == "Forced":
				outcome["Flame 1"] = ("Image", self.getflameframe(999), self.flameposition)
				outcome["Overlay Clock"] = ("Image", "flame_snooze", self.flameposition)
				if snoozetimer > 0:
					outcome["Overlay Text"] = ("Text", str(snoozetimer), self.snoozeoffset, "Centre", "Snooze", "Snooze")

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



	def getflameframe(self, flameversion):

		if flameversion == 999:
			flamemax = 10
		else:
			flamemax = 20

		flamesize = (Clock.getnow().getvalue() + (flameversion * 5)) % flamemax
		if flamesize < 13:
			flamename = "a" * (13 - flamesize)
			if (flameversion % 2) == 0:
				direction = "L"
			else:
				direction = "R"
			return ("Flame " + flamename), ("flame_" + str(flamesize) + direction)
		else:
			return "", ""



	def getflametransition(self):

		transitionfraction = self.boilerstate.gettransitionfraction()
		flamesize = int((transitionfraction - 0.2) * 16.24)
		if (Clock.getnow().getvalue() % 2) == 0:
			direction = "L"
		else:
			direction = "R"
		return ("flame_" + str(flamesize) + direction)



	def updateflamemode(self, boilerswitchstatus, thermostatstatus):

		transitionfraction = self.boilerstate.gettransitionfraction()

		outcome = self.flamestate
		if transitionfraction > 0.2:
			if (boilerswitchstatus == False) and (thermostatstatus == True):
				outcome = "Snooze"
			else:
				if transitionfraction == 1.0:
					if (boilerswitchstatus == True) and (thermostatstatus == False):
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
