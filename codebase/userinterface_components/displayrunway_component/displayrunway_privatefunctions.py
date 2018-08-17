
def getsanitisedtimevalue(clockobject):

	displayedtimevalue = clockobject.getsecondlessvalue()
	displayborder = True
	if clockobject.getsecond() != 0:
		displayborder = False
		if clockobject.gethour() == 23:
			if clockobject.getminute() == 59:
				displayedtimevalue = displayedtimevalue + 60

	return displayedtimevalue, displayborder



def getblocklabel(blocktype, indexer):

	if blocktype == "Day":
		blocklabel = "E"
	elif blocktype == "Civ":
		blocklabel = "D"
	elif blocktype == "Nau":
		blocklabel = "C"
	elif blocktype == "Ast":
		blocklabel = "B"
	else:
		blocklabel = "Z"

	outcome = blocklabel + str(indexer + 2)

	return outcome



def gettimeshiftervalue(indexer, dstmode):

	multiplier = indexer * 24

	if dstmode == True:
		multiplier = multiplier + 1

	return (multiplier * 3600)
