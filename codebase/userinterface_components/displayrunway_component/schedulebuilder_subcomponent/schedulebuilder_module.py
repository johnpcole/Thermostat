from . import schedulebuilder_class as ScheduleBuilderClass

def createschedulebuilder(boilercontroller, currenttime):
	return ScheduleBuilderClass.DefineScheduleBuilder(boilercontroller, currenttime)