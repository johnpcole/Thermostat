from ....common_components.datetime_datatypes import clock_module as Clock


def preparelocation(decimallocation):
	if decimallocation < 0.0:
		sign = -1
	else:
		sign = 1

	location = abs(decimallocation)

	degs = int(location)

	mins = int((location - float(degs)) * 60.0)

	return sign, degs, mins



def sanitisetime(textstring, defaultmode):

	hour = textstring[0:2]
	min = textstring[2:4]

	try:
		hourvalue = int(hour)
		minvalue = int(min)
		outcometime = Clock.createastime(hourvalue, minvalue, 0)
		outcomevalidity = True
	except:
		outcomevalidity = False
		if defaultmode == "Start":
			outcometime = Clock.createastime(0, 0, 0)
		else:
			outcometime = Clock.createastime(23, 59, 59)
		#print "Problems reading sunrise/sunset time: ", textstring

	return outcometime, outcomevalidity



def generatedummydata(day, datamode):

	if day == 16:
		dummyoffset = 5
	elif day == 17:
		dummyoffset = 3
	else:
		dummyoffset = 0
	if datamode == "Day":
		dummytime = 0 + dummyoffset
	elif datamode == "Civ":
		dummytime = 6 + dummyoffset
	elif datamode == "Nau":
		dummytime = 12 + dummyoffset
	elif datamode == "Ast":
		dummytime = 18 + dummyoffset
		#dummytime = -1
	else:
		datamode = 1 / 0
	if dummytime < 10:
		dummytext = "0" + str(dummytime)
	else:
		dummytext = str(dummytime)

	starttime, startvalidity = sanitisetime(dummytext + "00", "Start")
	endtime, endvalidity = sanitisetime(dummytext + "45", "End")

	return starttime, startvalidity, endtime, endvalidity


def getindexes(lookupday, lookupmonth):

	desiredlinestart = str(lookupday) + "  "
	if lookupday < 10:
		desiredlinestart = "0" + desiredlinestart

	desiredcolumn = (lookupmonth * 11) - 7

	return desiredlinestart, desiredcolumn



def extracttimings(dataline, columnindex):

	fulldata = dataline[(columnindex + 0):(columnindex + 9)]
	invalidrowone = "         "
	invalidrowtwo = "==== ===="
	if (fulldata == invalidrowone) or (fulldata == invalidrowtwo):
		rowvalidity = False
	else:
		rowvalidity = True

	starttext = dataline[(columnindex + 0):(columnindex + 4)]
	endtext = dataline[(columnindex + 5):(columnindex + 9)]

	starttime, startvalidity = sanitisetime(starttext, "Start")
	endtime, endvalidity = sanitisetime(endtext, "End")

	return rowvalidity, starttime, startvalidity, endtime, endvalidity

