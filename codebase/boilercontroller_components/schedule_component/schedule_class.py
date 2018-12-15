from ...common_components.datetime_datatypes import clock_module as Clock


class DefineSchedule:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.scheduleditems = {}

		tt = Clock.getnow().getvalue() - 100
		ss = 3
		self.addscheduleditem(Clock.createastime(0, 10, tt), ss)
		self.addscheduleditem(Clock.createastime(0, 50, tt), ss + 2)
		self.addscheduleditem(Clock.createastime(0, 90, tt), ss + 4)
		self.addscheduleditem(Clock.createastime(0, 130, tt), ss + 6)
		self.addscheduleditem(Clock.createastime(0, 170, tt), ss + 8)
		self.addscheduleditem(Clock.createastime(0, 210, tt), ss + 10)
		self.addscheduleditem(Clock.createastime(0, 260, tt), ss + 12)
		self.addscheduleditem(Clock.createastime(0, 310, tt), ss + 14)
		self.addscheduleditem(Clock.createastime(0, 360, tt), ss + 16)
		self.addscheduleditem(Clock.createastime(0, 410, tt), ss + 18)
		self.addscheduleditem(Clock.createastime(0, 460, tt), ss + 20)
		self.addscheduleditem(Clock.createastime(0, 520, tt), ss + 22)
		self.addscheduleditem(Clock.createastime(0, 580, tt), ss + 24)
		self.addscheduleditem(Clock.createastime(0, 640, tt), 24)



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

	def getcurrentinstruction(self, currenttime):

		sortedlist = self.getscheduledtimevalues()
		if len(sortedlist) > 0:
			outcome = -1000
			currenttimevalue = currenttime.getsecondlessvalue()
			for scheduledtime in sortedlist:
				if scheduledtime <= currenttimevalue:
					outcome = scheduledtime
			if outcome == -1000:
				outcome = scheduledtime
			return self.scheduleditems[outcome]
		else:
			return -1000


