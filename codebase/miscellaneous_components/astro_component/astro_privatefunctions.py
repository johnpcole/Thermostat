from ...common_components.datetime_datatypes import datetime_module as DateTime


def calculatedatevalues(storeddate):

	nowday, nowmonth, nowyear, dummy1, dummy2, dummy3 = DateTime.getnow().getsextuplet()
	lastday, lastmonth, lastyear, dummy1, dummy2, dummy3 = storeddate.getsextuplet()

	tomorrowdatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	tomorrowdatetime.adjustdays(1)
	tomday, tommonth, tomyear, dummy1, dummy2, dummy3 = tomorrowdatetime.getsextuplet()

	if ((nowday != lastday) or (nowmonth != lastmonth)) or (nowyear != lastyear):
		differenceflag = True
	else:
		differenceflag = False

	return nowday, nowmonth, nowyear, tomday, tommonth, tomyear, differenceflag



def calculatefilter(storeddate):

	nowday, nowmonth, nowyear, dummy1, dummy2, dummy3 = DateTime.getnow().getsextuplet()
	lastday, lastmonth, lastyear, dummy1, dummy2, dummy3 = storeddate.getsextuplet()

	yesterdaydatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	yesterdaydatetime.adjustdays(-1)
	yesday, yesmonth, yesyear, dummy1, dummy2, dummy3 = yesterdaydatetime.getsextuplet()

	if (nowday == lastday) and ((nowmonth == lastmonth) and (nowyear == lastyear)):
		todayflag = True
		tomorrowflag = True
	elif (yesday == lastday) and ((yesmonth == lastmonth) and (yesyear == lastyear)):
		todayflag = False
		tomorrowflag = True
	else:
		todayflag = False
		tomorrowflag = False

	return todayflag, tomorrowflag

