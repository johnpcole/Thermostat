class DefineAuditBook:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.audititems = {}

	# =========================================================================================

	def getschedule(self):

		return self.scheduleditems

	# =========================================================================================

	def addscheduleditem(self, newtime, newoutcome):

		if self.doesscheduledtimeexist(newtime) == False:
			self.scheduleditems[newtime.getvalue()] = newoutcome
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

	def getscheduleditem(self, queriedtime):

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

		if len(self.getscheduledtimes()) > 0:
			sortedlist = self.getscheduledtimes()
			outcome = -1000
			for scheduledtime in sortedlist:
				if scheduledtime > currenttime:
					if outcome == -1000:
						outcome = scheduledtime
			if outcome == -1000:
				outcome = sortedlist[0]
			return outcome

		else:
			return -1000

	# =========================================================================================

	def getearliestscheduledtime(self):

		if len(self.getscheduledtimes()) > 0:
			return min(self.scheduleditems.keys())

		else:
			return -1000

	# =========================================================================================

	def getscheduledtimes(self):

		return sorted(self.scheduleditems.keys())

	# =========================================================================================

	def getrollingscheduledtimes(self, currenttime, desiredlistlength):

		listlength = len(self.getscheduledtimes())
		if listlength > 0:
			originallist = self.getscheduledtimes()
			multiplier = 1 + int(desiredlistlength / listlength)
			outcome = []
			for scheduledtime in originallist:
				if scheduledtime > currenttime:
					outcome.append(scheduledtime)
			for index in range(0, multiplier):
				outcome = outcome + originallist
			return outcome

		else:
			return {}
