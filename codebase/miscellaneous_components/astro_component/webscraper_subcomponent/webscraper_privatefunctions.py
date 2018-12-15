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



def generatedummydata(datamode):

	outcome = "Dummy Data"

	if datamode == "Day":
		hourstart = 10
		hourend = 13
	elif datamode == "Civ":
		hourstart = 7
		hourend = 16
	elif datamode == "Nau":
		hourstart = 4
		hourend = 19
	else:
		hourstart = 1
		hourend = 22

	for day in range(1, 32):

		starttime = Clock.createastime(hourstart, 30, 0)
		endtime = Clock.createastime(hourend, 30, 0)

		starttimestring = starttime.getsecondlesstext()
		endtimestring = endtime.getsecondlesstext()

		timestring = "  " + starttimestring[:2] + starttimestring[-2:] + " " + endtimestring[:2] + endtimestring[-2:]

		daytext = "00" + str(day)
		outcome = outcome + "\n" + daytext[-2:]

		for month in range(1, 13):
			outcome = outcome + timestring

	outcome = outcome + "\nEnd of dummy data"

	return outcome



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

