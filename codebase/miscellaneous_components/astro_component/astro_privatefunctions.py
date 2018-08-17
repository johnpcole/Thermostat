from ...common_components.datetime_datatypes import datetime_module as DateTime
import time as SystemTime



def calculatedatevalues(storeddate):

	lastday, lastmonth, lastyear, dummy1, dummy2, dummy3 = storeddate.getsextuplet()

	todaydatetime = DateTime.getnow()
	nowday, nowmonth, nowyear, dummy1, dummy2, dummy3 = todaydatetime.getsextuplet()
	nowdst = determinedststate(nowday, nowmonth, nowyear)

	tomorrowdatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	tomorrowdatetime.adjustdays(1)
	tomday, tommonth, tomyear, dummy1, dummy2, dummy3 = tomorrowdatetime.getsextuplet()
	tomdst = determinedststate(tomday, tommonth, tomyear)

	yesterdaydatetime = DateTime.createfromsextuplet(nowday, nowmonth, nowyear, 0, 0, 0)
	yesterdaydatetime.adjustdays(-1)
	yesday, yesmonth, yesyear, dummy1, dummy2, dummy3 = yesterdaydatetime.getsextuplet()
	yesdst = determinedststate(yesday, yesmonth, yesyear)

	if ((nowday != lastday) or (nowmonth != lastmonth)) or (nowyear != lastyear):
		differenceflag = True
	else:
		differenceflag = False

	return nowday, nowmonth, nowyear, nowdst, tomday, tommonth, tomyear, tomdst, yesday, yesmonth, yesyear, yesdst, differenceflag



def determinedststate(day, month, year):

	dsttesttime = SystemTime.mktime((year,month,day,3,2,1,-1,-1,-1))

	dsttestresult = SystemTime.localtime(dsttesttime).tm_isdst

	if dsttestresult == 1:
		nowdst = True
	elif dsttestresult == 0:
		nowdst = False
	else:
		x = 1/0

	return nowdst
