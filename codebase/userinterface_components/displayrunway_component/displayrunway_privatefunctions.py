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



def gettimeshiftervalue(indexer, dateobject):

	multiplier = indexer * 24

	if determinedststate(dateobject) == True:
		multiplier = multiplier + 24

	return (multiplier * 60 * 60)



def getdateshift(currentdate, astroitemdate):

	outcome = -999

	if DateTime.areidentical(currentdate, astroitemdate) == True:
		outcome = 0
	else:
		yesterdaydate = DateTime.createfromobject(currentdate)
		yesterdaydate.adjustdays(-1)
		if DateTime.areidentical(yesterdaydate, astroitemdate) == True:
			outcome = -1
		else:
			tomorrowdate = DateTime.createfromobject(currentdate)
			tomorrowdate.adjustdays(1)
			if DateTime.areidentical(tomorrowdate, astroitemdate) == True:
				outcome = 1

	return outcome



def determinedststate(dateobject):

	year, month, day, dummy1, dummy2, dummy3 = dateobject.getsextuplet()

	dsttesttime = SystemTime.mktime((year,month,day,3,2,1,-1,-1,-1))

	dsttestresult = SystemTime.localtime(dsttesttime).tm_isdst

	if dsttestresult == 1:
		outcome = True
	elif dsttestresult == 0:
		outcome = False
	else:
		outcome = 1/0

	return outcome

