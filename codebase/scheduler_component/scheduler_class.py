from ..clock_datatype import clock_module as Clock


class DefineSchedule:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.scheduleditems = {}

	# =========================================================================================

	def getschedule(self):

		return self.scheduleditems

	# =========================================================================================

	def addscheduleditem(self, newtime, newinstruction):

		if self.doesscheduledtimeexist(newtime) == False:
			self.scheduleditems[newtime.getvalue()] = newinstruction
			return True

		else:
			return False

	# =========================================================================================

	def deletescheduleditem(self, timetodelete):

		if self.doesscheduledtimeexist(timetodelete) == True:
			del self.scheduleditems[timetodelete.getvalue()]
			return True

		else:
			return False

	# =========================================================================================

	def getscheduledinstruction(self, queriedtime):

		if self.doesscheduledtimeexist(queriedtime) == True:
			return self.scheduleditems[queriedtime.getvalue()]

		else:
			return -1000

	# =========================================================================================

	def doesscheduledtimeexist(self, queriedtime):

		if queriedtime.getvalue() in self.scheduleditems:
			return True

		else:
			return False

	# =========================================================================================

	def getnextscheduledtime(self, currenttime):

		if len(self.getscheduledtimeintegers()) > 0:
			sortedlist = self.getscheduledtimeintegers()
			outcome = -1000
			for scheduledtime in sortedlist:
				if scheduledtime > currenttime:
					if outcome == -1000:
						outcome = scheduledtime
			if outcome == -1000:
				outcome = sortedlist[0]
			return Clock.createasinteger(outcome)

		else:
			return -1000

	# =========================================================================================

	def getearliestscheduledtime(self):

		sortedlist = self.getscheduledtimeintegers()
		if len(sortedlist) > 0:
			return Clock.createasinteger(sortedlist[0])

		else:
			return -1000

	# =========================================================================================

	def getscheduledtimevalues(self):

		return sorted(self.scheduleditems.keys())

	# =========================================================================================

	def getscheduledtimes(self):

		sortedlist = self.getscheduledtimevalues()
		outcome = []
		for sorteditem in sortedlist:
			outcome.append(Clock.createasinteger(sorteditem))
		return outcome

	# =========================================================================================
