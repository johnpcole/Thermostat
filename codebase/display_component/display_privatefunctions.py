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