class DefineTransition:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self, prescalesize, postscalesize, initialvalue):

		self.prescalesize = -prescalesize

		self.postscalesize = postscalesize

		self.transitionstate = 0

		self.oldvalue = initialvalue

		self.newvalue = initialvalue

	# =========================================================================================

	def getswitchedvalue(self):

		if self.transitionstate < 0:
			return self.oldvalue
		else:
			return self.newvalue

	# =========================================================================================

	def gettransitionvalue(self):

		return self.transitionstate

	# =========================================================================================

	def gettransitionfraction(self):

		if self.transitionstate < 0:
			return (-float(self.transitionstate) / float(self.prescalesize))
		else:
			return (float(self.transitionstate) / float(self.postscalesize))

		return self.transitionstate

	# =========================================================================================

	def gettransitioningstate(self):

		if self.transitionstate < self.postscalesize:
			return True
		else:
			return False

	# =========================================================================================

	def updatevalue(self, newvalue):

		# If the transition hasn't already started, start it now
		if newvalue != self.newvalue:
			self.newvalue = newvalue
			self.transitionstate = self.prescalesize

		return self.updatetransition()

	# =========================================================================================

	def updatetransition(self):

		# If the transition hasn't finished, continue it
		if self.transitionstate < self.postscalesize:
			self.transitionstate = self.transitionstate + 1

		# Else set the old value to be the new value
		else:
			self.oldvalue = self.newvalue

		return self.transitionstate
