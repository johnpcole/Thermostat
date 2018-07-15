# from ..common_components.fileprocessing_framework import fileprocessing_module as File
from ..common_components.vector_datatype import vector_module as Vector
# from ..common_components.dataprocessing_framework import dataprocessing_module as Data

# -------------------------------------------------------------------
# Returns the colour of text for temperatures
# -------------------------------------------------------------------

def gettemperaturecolour(temp):

	limitedvalue = int(max(3, min(27, temp)))
	return str(limitedvalue)

# -------------------------------------------------------------------
# Returns the colour of the temperature for desired temp
# -------------------------------------------------------------------

def gettransitioncolour(temperature, transitionfraction):

	basecolour = gettemperaturecolour(temperature)
	if transitionfraction > 0:
		return basecolour
	else:
		return ("mix:" + basecolour + "/" + str(-transitionfraction) + "/Black")

# -------------------------------------------------------------------
# Returns the position of the temperature for desired temp
# -------------------------------------------------------------------

def gettransitionposition(anchor, startoffset, transitionfraction):

	if transitionfraction > 0:
		return (anchor + int(startoffset * (1.0 - transitionfraction)))
	else:
		return anchor


def gettimelinemarkers(zeroline, timescale, offset):

	outcome = []

	for hourindex in range(1, 14):

		# Position of hour marker line
		hourmarker = zeroline + (hourindex * timescale) - offset

		outcome.append(Vector.createfromvalues(hourmarker, 15))

		# Draw the half & quarter markers
		for subindex in range(1, 4):

			# Position of marker
			pixelposition = hourmarker - int(subindex * timescale / 4)

			# Only draw marker if it's to the right of the current time marker
			if zeroline < pixelposition:

				# Draw the marker line
				outcome.append(Vector.createfromvalues(pixelposition, 3 * ((subindex + 1) % 2)))

	return outcome


def getfuturetimevalue(scheduledtimevalue, currenttimevalue):

	if scheduledtimevalue <= currenttimevalue:
		return (scheduledtimevalue + (24 * 3600))
	else:
		return scheduledtimevalue


def getcolourpallette():
	colours = {}
	colours["27"] = (178, 0, 0)
	colours["26"] = (216, 0, 0)
	colours["25"] = (255, 38, 38)
	colours["24"] = (247, 73, 29)
	colours["23"] = (239, 108, 21)
	colours["22"] = (232, 144, 13)
	colours["21"] = (224, 180, 6)
	colours["20"] = (216, 216, 0)
	colours["19"] = (180, 224, 6)
	colours["18"] = (144, 232, 13)
	colours["17"] = (108, 239, 21)
	colours["16"] = (73, 247, 29)
	colours["15"] = (38, 255, 38)
	colours["14"] = (29, 242, 71)
	colours["13"] = (20, 229, 104)
	colours["12"] = (13, 216, 135)
	colours["11"] = (6, 204, 164)
	colours["10"] = (0, 191, 191)
	colours["9"] = (6, 164, 204)
	colours["8"] = (13, 135, 216)
	colours["7"] = (20, 104, 229)
	colours["6"] = (29, 71, 242)
	colours["5"] = (38, 38, 255)
	colours["4"] = (0, 0, 216)
	colours["3"] = (0, 0, 178)
	return colours

def getfontpallette():
	fonts = {}
	fonts["Timeline Hours"] = ("Font", 14)
	fonts["Timeline Temps"] = ("Font", 28)
	fonts["Desired Temp"] =  ("Font", 54)
	fonts["Actual Temp"] = ("Font", 148)
	return fonts

def getcurrenttemplayout(tempvalue, positionvector):

		degreeposition = Vector.add(positionvector, Vector.createfromvalues(100, 35))

		integervalue = int(tempvalue)
		colour = gettemperaturecolour(tempvalue)

		# Draw current temperature
		outcome = {}
		outcome["Integer"] = (str(integervalue), positionvector, "Right", colour, "Actual Temp")
		outcome["Fraction"] = ((str(tempvalue - float(integervalue)))[1:3], positionvector, "Left", colour, "Actual Temp")
		outcome["Degree"] = ("O", degreeposition, "Left", colour, "Timeline Hours")
		outcome["Celcius"] = ("C", Vector.add(degreeposition, Vector.createfromvalues(10, 0)), "Left", colour, "Timeline Temps")

		return outcome