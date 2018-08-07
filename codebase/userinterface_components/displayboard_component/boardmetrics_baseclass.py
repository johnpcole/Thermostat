from ...common_components.vector_datatype import vector_module as Vector
from ...common_components.clock_datatype import clock_module as Clock
from .. import display_sharedfunctions as DisplayFunction



class DefineBoardMetrics:

	def __init__(self):

		self.temperaturetop = 40

		self.offtemperatureorigin = 260

		self.ontemperatureorigin = 310

		self.degreesoffset = Vector.createfromvalues(100, 35)

		self.celciusoffset = Vector.add(Vector.createfromvalues(10, 0), self.degreesoffset)

		self.flameposition = Vector.createfromvalues(30, 71)

		self.snoozeoffset = Vector.add(Vector.createfromvalues(78, 15), self.flameposition)



	def calculatetemperaturemetrics(self, temperature, transitionfraction):

		integerpart = int(temperature)
		fractionpart = abs(temperature - float(integerpart))
		colour = DisplayFunction.gettemperaturecolour(integerpart)

		positionoffset = DisplayFunction.gettwowaytransitionposition(self.offtemperatureorigin,
																		self.ontemperatureorigin, transitionfraction)

		currentposition = Vector.createfromvalues(positionoffset, self.temperaturetop)


		return integerpart, fractionpart, colour, currentposition



	def calculateflameframe(self, flameversion):

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



	def calculateflametransition(self, transitionfraction):

		flamesize = int((transitionfraction - 0.2) * 16.24)
		if (Clock.getnow().getvalue() % 2) == 0:
			direction = "L"
		else:
			direction = "R"
		return ("flame_" + str(flamesize) + direction)

