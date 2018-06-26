from date_subcomponent import date_module as Date
from time_subcomponent import time_module as Time
from . import datetime_privatefunctions as DateTimeFunction

# ===========================================================================================================
# This class captures all date-time combinations. It should be used even when just a date or time are
# required. It uses the Date and Time classes which should not be directly called.
# ===========================================================================================================

class DefineDateTime:

	def __init__(self):
		
		# The time component, stored as a Time object
		self.timecomponent = Time.createfromiso("999999")

		# The date component, stored as a Date object
		self.datecomponent = Date.createfromiso("99999999")
		


# ===========================================================================================================
# Basic Value Setters
# ===========================================================================================================

# ---------------------------------------------------------
# Sets the datetime using another DateTime object
# ---------------------------------------------------------

	def setfromobject(self, datetimeobject):

		self.timecomponent.setfromobject(datetimeobject.timecomponent)
		self.datecomponent.setfromobject(datetimeobject.datecomponent)



# ---------------------------------------------------------
# Sets the datetime using a
# Day-Month-Year-Hour-Minute-Second sextuplet of integers
# ---------------------------------------------------------

	def setfromsextuplet(self, day, month, year, hour, minute, second):

		self.timecomponent.setfromtriplet(hour, minute, second)
		self.datecomponent.setfromtriplet(day, month, year)



# ---------------------------------------------------------
# Sets the datetime using a YYYYMMDDHHMMSS string
# ---------------------------------------------------------

	def setfromiso(self, isostring):
	
		datestring, timestring = DateTimeFunction.separatedatetimeisocomponents(isostring)
		self.datecomponent.setfromiso(datestring)
		self.timecomponent.setfromiso(timestring)

	
	
# ===========================================================================================================
# Object Processing
# ===========================================================================================================
	
# ---------------------------------------------------------
# Sets the datetime to the current system clock value
# ---------------------------------------------------------
	
	def settonow(self):
		
		isodatestring, isotimestring = DateTimeFunction.getcurrentdatetime()
		self.timecomponent.setfromiso(isotimestring)
		self.datecomponent.setfromiso(isodatestring)
	
	
	
# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of seconds (+ve or -ve)
# ---------------------------------------------------------	
	
	def adjustseconds(self, secondsdelta):

		dayoffset = self.timecomponent.adjustseconds(secondsdelta)
		self.datecomponent.adjustdays(dayoffset)



# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of minutes (+ve or -ve)
# ---------------------------------------------------------	

	def adjustminutes(self, minutesdelta):

		self.adjustseconds(60 * minutesdelta)



# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of hours (+ve or -ve)
# ---------------------------------------------------------	

	def adjusthours(self, hoursdelta):

		self.adjustminutes(60 * hoursdelta)



# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of days (+ve or -ve)
# ---------------------------------------------------------	

	def adjustdays(self, daysdelta):

		self.datecomponent.adjustdays(daysdelta)



# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of months (+ve or -ve)
# ---------------------------------------------------------	

	def adjustmonths(self, monthsdelta):

		self.datecomponent.adjustmonths(monthsdelta)



# ---------------------------------------------------------
# Adjusts the datetime by specified
# number of years (+ve or -ve)
# ---------------------------------------------------------	

	def adjustyears(self, yearsdelta):

		self.datecomponent.adjustyears(yearsdelta)



# ---------------------------------------------------------
# Adjusts the date ONLY by DateDuration (object)
# ---------------------------------------------------------

	def adjustdate(self, durationdelta):

		self.datecomponent.adjustdate(durationdelta)
	
	
	
# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# Returns the datetime as a sextuplet of
# Day-Month-Year-Hour-Minute-Second integers
# ---------------------------------------------------------

	def getsextuplet(self):

		day, month, year = self.datecomponent.gettriplet()
		hour, minute, second = self.timecomponent.gettriplet()
		return day, month, year, hour, minute, second



# ---------------------------------------------------------
# Returns the datetime as a YYYYYMMDDHHMMSS string
# ---------------------------------------------------------

	def getiso(self):

		return self.datecomponent.getiso() + self.timecomponent.getiso()



# ---------------------------------------------------------
# Returns the date component as an integer
# ---------------------------------------------------------

	def getdatecomponent(self):

		return self.datecomponent



# ---------------------------------------------------------
# Returns the date component as an integer
# ---------------------------------------------------------

	def gettimecomponent(self):

		return self.timecomponent



# ---------------------------------------------------------
# Returns the datetime as a readable string
# ---------------------------------------------------------

	def getreadabledate(self, timeformat, secondsflag, dayflag, dateflag, monthflag, yearflag, separator):

		timecomponent = self.gettimecomponent()
		datecomponent = self.getdatecomponent()

		outcome = timecomponent.getreadabletime(timeformat, secondsflag) + " "
		outcome = outcome + datecomponent.getreadabledate(dayflag, dateflag, monthflag, yearflag, separator)
		return outcome



# ---------------------------------------------------------
# Returns the fractional now time - DOESNT USE THE CLASS!!!
# ---------------------------------------------------------

	def getdummynowfraction(self, secondsmodeflag):

		if secondsmodeflag == True:
			outcome = DateTimeFunction.getcurrentsecondfraction()
		else:
			outcome = DateTimeFunction.getcurrentsubsecondfraction()

		return outcome
