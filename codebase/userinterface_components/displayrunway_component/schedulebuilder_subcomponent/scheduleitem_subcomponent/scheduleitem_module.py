from . import scheduleitem_class as ScheduleItemClass

def createitem(temperature, activestate):
	return ScheduleItemClass.DefineItem(temperature, activestate)