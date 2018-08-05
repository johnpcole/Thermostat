from switchtimings_subcomponent import switchtimings_module as SwitchTiming


class DefineBoilerSwitch:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self):

		self.switchstatus = False

		self.switchreliefbuffer = 120 # seconds

		self.lastontime = SwitchTiming.createswitchtiming()

		self.lastofftime = SwitchTiming.createswitchtiming()

	# =========================================================================================



	# -------------------------------------------------------------------
	# Updates the boiler switch
	# -------------------------------------------------------------------

	def updateboilerstatus(self, desiredswitchstatus):

		self.updateboilerclocks()

		if self.switchstatus != desiredswitchstatus:
			if self.getcurrentbufferstate() == 0:
				if desiredswitchstatus == True:
					self.turnboileron()
				else:
					self.turnboileroff()

		return self.switchstatus



	# -------------------------------------------------------------------
	# Returns the number of seconds requried before the switch can be
	# changed again
	# -------------------------------------------------------------------

	def getcurrentbufferstate(self):

		if self.switchstatus == False:
			lastswitchedseconds = self.lastontime.getsecondssincelastswitched()
		else:
			lastswitchedseconds = self.lastofftime.getsecondssincelastswitched()

		return max(0, (self.switchreliefbuffer - lastswitchedseconds))


	# -------------------------------------------------------------------
	# Updates the boiler clocks, based on current switch status
	# -------------------------------------------------------------------

	def updateboilerclocks(self):

		if self.switchstatus == True:
			self.lastontime.updateswitchedtime()
		else:
			self.lastofftime.updateswitchedtime()



	# -------------------------------------------------------------------
	# Turns the boiler physically on
	# -------------------------------------------------------------------

	def turnboileron(self):

		self.switchstatus = True
		self.updateboilerclocks()
		print "Boiler switched on at", self.lastontime.getlastswitchedtime().gettext()
		#CODE TO THROW RELAY



	# -------------------------------------------------------------------
	# Turns the boiler physically off
	# -------------------------------------------------------------------

	def turnboileroff(self):

		self.switchstatus = False
		self.updateboilerclocks()
		print "Boiler switched off at", self.lastofftime.getlastswitchedtime().gettext()
		#CODE TO THROW RELAY



	# ==========================================================================================
	# Get Information
	# ==========================================================================================

	def getswitchstatus(self):

		return self.switchstatus

	# =========================================================================================
