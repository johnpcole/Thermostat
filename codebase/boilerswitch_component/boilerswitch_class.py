from switchtimings_subcomponent import switchtimings_module as SwitchTiming


class DefineBoilerSwitch:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.actualswitchstatus = False

		self.desiredswitchstatus = False

		self.switchreliefbuffer = 20 # seconds

		self.lastontime = SwitchTiming.createswitchtiming()

		self.lastofftime = SwitchTiming.createswitchtiming()

	# =========================================================================================



	# -------------------------------------------------------------------
	# Updates the boiler switch
	# -------------------------------------------------------------------

	def updateboilerstatus(self):

		self.updateboilerclocks()

		if self.actualswitchstatus != self.desiredswitchstatus:
			if self.getcurrentbufferstate() == 0:
				if self.desiredswitchstatus == True:
					self.turnboileron()
				else:
					self.turnboileroff()

		return self.actualswitchstatus



	# -------------------------------------------------------------------
	# Returns the number of seconds requried before the switch can be
	# changed again
	# -------------------------------------------------------------------

	def getcurrentbufferstate(self):

		if self.actualswitchstatus == False:
			lastswitchedseconds = self.lastontime.getsecondssincelastswitched()
		else:
			lastswitchedseconds = self.lastofftime.getsecondssincelastswitched()

		return max(0, (self.switchreliefbuffer - lastswitchedseconds))


	# -------------------------------------------------------------------
	# Updates the boiler clocks, based on current switch status
	# -------------------------------------------------------------------

	def updateboilerclocks(self):

		if self.actualswitchstatus == True:
			self.lastontime.updateswitchedtime()
		else:
			self.lastofftime.updateswitchedtime()



	# -------------------------------------------------------------------
	# Turns the boiler physically on
	# -------------------------------------------------------------------

	def turnboileron(self):

		self.actualswitchstatus = True
		self.updateboilerclocks()
		print "Boiler switched on at", self.lastontime.getlastswitchedtime().gettext()
		#CODE TO THROW RELAY



	# -------------------------------------------------------------------
	# Turns the boiler physically off
	# -------------------------------------------------------------------

	def turnboileroff(self):

		self.actualswitchstatus = False
		self.updateboilerclocks()
		print "Boiler switched off at", self.lastofftime.getlastswitchedtime().gettext()
		#CODE TO THROW RELAY


	# =========================================================================================

	def setdesiredswitchstatus(self, desiredstatus):

		self.desiredswitchstatus = desiredstatus

		return self.desiredswitchstatus



	# ==========================================================================================
	# Get Information
	# ==========================================================================================

	def getactualswitchstatus(self):

		return self.actualswitchstatus

	# =========================================================================================
