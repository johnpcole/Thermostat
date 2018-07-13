from ..common_components.clock_datatype import clock_module as Clock


class DefineSchedule:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.scheduleditems = {}

		self.lastchecked = Clock.createasinteger(0) #Clock.getnow()

	# =========================================================================================

	def getschedule(self):

		return self.scheduleditems

	# =========================================================================================

	def addscheduleditem(self, newtime, newinstruction):

		if self.doesscheduledtimeexist(newtime) == False:
			self.scheduleditems[newtime.getsecondlessvalue()] = newinstruction
			return True

		else:
			return False

	# =========================================================================================

	def deletescheduleditem(self, timetodelete):

		if self.doesscheduledtimeexist(timetodelete) == True:
			del self.scheduleditems[timetodelete.getsecondlessvalue()]
			return True

		else:
			return False

	# =========================================================================================

	def getscheduledinstruction(self, queriedtime):

		if self.doesscheduledtimeexist(queriedtime) == True:
			return self.scheduleditems[queriedtime.getsecondlessvalue()]

		else:
			return -1000

	# =========================================================================================

	def doesscheduledtimeexist(self, queriedtime):

		if queriedtime.getsecondlessvalue() in self.scheduleditems:
			return True

		else:
			return False

	# =========================================================================================

	# def getnextscheduledtime(self, currenttime):
	#
	# 	sortedlist = self.getscheduledtimevalues()
	# 	if len(sortedlist) > 0:
	# 		outcome = -1000
	# 		for scheduledtime in sortedlist:
	# 			if scheduledtime > currenttime:
	# 				if outcome == -1000:
	# 					outcome = scheduledtime
	# 		if outcome == -1000:
	# 			outcome = sortedlist[0]
	# 		return Clock.createasinteger(outcome)
	#
	# 	else:
	# 		return -1000

	# =========================================================================================

	# def getlastscheduledtime(self, currenttime):
	#
	# 	sortedlist = self.getscheduledtimevalues()
	# 	if len(sortedlist) > 0:
	# 		outcome = -1000
	# 		for scheduledtime in sortedlist:
	# 			if scheduledtime <= currenttime:
	# 				outcome = scheduledtime
	# 		if outcome == -1000:
	# 			outcome = scheduledtime
	# 		return Clock.createasinteger(outcome)
	#
	# 	else:
	# 		return -1000

	# =========================================================================================

	# def getearliestscheduledtime(self):
	#
	# 	sortedlist = self.getscheduledtimeintegers()
	# 	if len(sortedlist) > 0:
	# 		return Clock.createasinteger(sortedlist[0])
	#
	# 	else:
	# 		return -1000

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

	def checkschedule(self, currenttime):

		lasttimechecked = self.lastchecked.getsecondlessvalue()
		outcome = -1000
		if lasttimechecked != currenttime.getsecondlessvalue():
			self.lastchecked = Clock.createasinteger(lasttimechecked + 60)
			print "Updated Schedule to", self.lastchecked.getsecondlesstext()
			outcome = self.getscheduledinstruction(self.lastchecked)
		return outcome