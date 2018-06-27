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

		if len(self.getscheduledtimes) > 0:
			sortedlist = self.getscheduledtimes()
			sortedlist.append(sortedlist[0]
							  for scheduledtime in sortedlist:
			if ???????
			return self.getscheduledtimes[1]

		else:
			return -1000

	# =========================================================================================

	def getearliestscheduledtime(self):

		if len(self.getscheduledtimes) > 0:
			return min(self.scheduleditems.keys())

		else:
			return -1000

	# =========================================================================================

	def getscheduledtimes(self):

		return sorted(self.scheduleditems.keys())





















class DefineBoilerController:
	
	# ==========================================================================================
	# Object Setup
	# ==========================================================================================
	
	def __init__(self):
		
		self.boilerswitchstatus = False
		
		self.desiredtemperature = 1.0
		
		self.currenttemperature = 1.0
	
	# =========================================================================================
	
	def updateboilerswitch(self):
		
		if self.desiredtemperature > self.currenttemperature:
			self.turnboileron()
		else:
			self.turnboileroff()
		return self.getboilerstatus()
	
	# =========================================================================================
	
	def getboilerstatus(self):

		return self.boilerswitchstatus
	
	# =========================================================================================
	
	def setdesiredtemperature(self, temp):
		
		self.desiredtemperature = temp
		
		return self.getdesiredtemperature()
	
	# =========================================================================================
	
	def getdesiredtemperature(self):
		
		return self.desiredtemperature
	
	# =========================================================================================
	
	def setcurrenttemperature(self, temp):
		
		self.currenttemperature = temp
		
		return self.getcurrenttemperature()
	
	# =========================================================================================
	
	def getcurrenttemperature(self):
		
		return self.currenttemperature
	
	# =========================================================================================
	
	def turnboileron(self):
		
		self.boilerswitchstatus = True
		#CODE TO THROW RELAY
	
	# =========================================================================================
	
	def turnboileroff(self):
		
		self.boilerswitchstatus = False
		#CODE TO THROW RELAY
