from ...common_components.datetime_datatypes import datetime_module as DateTime


def calculatedatevalues(storeddate):

	lastday, lastmonth, lastyear, dummy1, dummy2, dummy3 = storeddate.getsextuplet()

	todaydatetime = DateTime.getnow()
	nowday, nowmonth, nowyear, dummy1, dummy2, dummy3 = todaydatetime.getsextuplet()

	tomorrowdatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	tomorrowdatetime.adjustdays(1)
	tomday, tommonth, tomyear, dummy1, dummy2, dummy3 = tomorrowdatetime.getsextuplet()

	yesterdaydatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	yesterdaydatetime.adjustdays(1)
	yesday, yesmonth, yesyear, dummy1, dummy2, dummy3 = yesterdaydatetime.getsextuplet()


	if ((nowday != lastday) or (nowmonth != lastmonth)) or (nowyear != lastyear):
		differenceflag = True
	else:
		differenceflag = False

	return nowday, nowmonth, nowyear, tomday, tommonth, tomyear, yesday, yesmonth, yesyear, differenceflag

