# from ..common_components.fileprocessing_framework import fileprocessing_module as File
# from ..common_components.vector_datatype import vector_module as Vector
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

def getonewaytransitionposition(anchor, startoffset, transitionfraction):

	if transitionfraction > 0:
		return (anchor + int(startoffset * (1.0 - transitionfraction)))
	else:
		return anchor


# -------------------------------------------------------------------
# Returns the position of the temperature for current temp
# -------------------------------------------------------------------

def gettwowaytransitionposition(offanchor, onanchor, transitionfraction):

	if transitionfraction > 0:
		return onanchor
	else:
		return int((offanchor * (-transitionfraction)) + (onanchor * (1 + transitionfraction)))


# -------------------------------------------------------------------
# Prefixes dictionary keys
# -------------------------------------------------------------------

def prefixdictionarykeys(dictionary, prefix):

	outcome = {}

	for item in dictionary:
		outcome[prefix + ": " + item] = dictionary[item]

	return outcome
