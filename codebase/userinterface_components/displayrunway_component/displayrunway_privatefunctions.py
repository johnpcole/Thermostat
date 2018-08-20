import time as SystemTime
from ...common_components.datetime_datatypes import datetime_module as DateTime


def getsanitisedtimevalue(clockobject, validity, mode):

	if validity == True:
		outcome = clockobject.getsecondlessvalue()
	else:
		if mode == "Start":
			outcome = 0
		elif mode == "End":
			outcome = 24 * 3600
		else:
			outcome = 1/0

	return outcome



def getblocklabel(blocktype, indexer, counter):

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

	outcome = blocklabel + str(((indexer + 3) * 1000) + counter)

	return outcome



def gettimeshiftervalue(indexer, dateobject):

	multiplier = indexer * 24

	if determinedststate(dateobject) == True:
		multiplier = multiplier + 1
	return (multiplier * 60 * 60)



def getdateshift(currentdate, astroitemdate):

	outcome = -999

	if DateTime.areidentical(currentdate, astroitemdate) == True:
		outcome = 0
	else:
		if DateTime.areidentical(createcustomdate(currentdate, -1), astroitemdate) == True:
			outcome = -1
		else:
			if DateTime.areidentical(createcustomdate(currentdate, 1), astroitemdate) == True:
				outcome = 1

	return outcome



def determinedststate(dateobject):

	day, month, year = dateobject.getdatetriplet()

	dsttesttime = SystemTime.mktime((year,month,day,3,2,1,-1,-1,-1))

	dsttestresult = SystemTime.localtime(dsttesttime).tm_isdst

	if dsttestresult == 1:
		outcome = True
	elif dsttestresult == 0:
		outcome = False
	else:
		outcome = 1/0

	return outcome


def createcustomdate(currentdateobject, dayshift):

	outcome = DateTime.createfromobject(currentdateobject)
	outcome.adjustdays(dayshift)

	return outcome
