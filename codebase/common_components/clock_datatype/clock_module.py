from . import clock_class as ClockClass
import datetime as PythonDateTime



def createastime(hours, minutes, seconds):
	
	return ClockClass.DefineClock(hours, minutes, seconds)



def createasinteger(timevalue):

	return ClockClass.DefineClock(0, 0, timevalue)



def createasclock(existingtime):
	return ClockClass.DefineClock(0, 0, existingtime.getvalue())



def getnow():

	currentdatetime = str(PythonDateTime.datetime.now())
	return ClockClass.DefineClock(int(currentdatetime[11:13]), int(currentdatetime[14:16]), int(currentdatetime[17:19]))



def timediff(timeone, timetwo):

	return ClockClass.DefineClock(0, 0, timeone.getvalue() - timetwo.getvalue())



def timeadd(timeone, timetwo):

	return ClockClass.DefineClock(0, 0, timeone.getvalue() + timetwo.getvalue())



def convert24hourtohuman(hour):

	rawhour = hour % 12
	if rawhour == 0:
		return str(12)
	else:
		return str(rawhour)

def getfuturetimevalue(scheduledtimevalue, currenttimevalue):

	if scheduledtimevalue <= currenttimevalue:
		return (scheduledtimevalue + (24 * 3600))
	else:
		return scheduledtimevalue
