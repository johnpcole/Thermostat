from .scheduleitem_subcomponent import scheduleitem_module as ScheduleItem
from ....common_components.datetime_datatypes import clock_module as Clock

class DefineScheduleBuilder:

	def __init__(self, boilercontroller, currenttime):

		self.newschedule = {}

		schedule = boilercontroller.getschedule()
		scheduledtimes = schedule.getscheduledtimes()

		currenttimevalue = currenttime.getvalue()

		overridemode = boilercontroller.getoverridemode()
		if overridemode.get("Timed") == True:
			overridetimevalue = Clock.getfuturetimevalue(boilercontroller.getoverridetime().getvalue(), currenttimevalue)
			self.newschedule[overridetimevalue] = ScheduleItem.createitem(boilercontroller.getoverridereturntemperature(), True)
		elif overridemode.get("Lock") == True:
			overridetimevalue = 200000
		else:
			overridetimevalue = -99999

		for item in scheduledtimes:
			newitem = Clock.getfuturetimevalue(item.getvalue(), currenttimevalue)
			if newitem >= overridetimevalue:
				activestate = True
			else:
				activestate = False
			self.newschedule[newitem] = ScheduleItem.createitem(schedule.getscheduledinstruction(item), activestate)



	def gettimings(self):

		return sorted(self.newschedule.keys())



	def gettemp(self, timevalue):

		return self.newschedule[timevalue].gettemp()



	def getactive(self, timevalue):

		return self.newschedule[timevalue].getstatus()
