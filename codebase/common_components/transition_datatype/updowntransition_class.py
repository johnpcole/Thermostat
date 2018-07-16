class DefineUpDownTransition:

	# ==========================================================================================
	# Object Setup
	# ==========================================================================================

	def __init__(self, prescalesize, postscalesize, initialvalue):

		self.prescalesize = -prescalesize

		self.postscalesize = postscalesize

		self.transitionstate = 0

		self.value = initialvalue

	# =========================================================================================

	def getswitchedvalue(self):

		if self.transitionstate < 0:
			return False
		else:
			return True

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

		if (self.transitionstate != self.postscalesize) and (self.transitionstate != self.prescalesize):
			return True
		else:
			return False

	# =========================================================================================

	def updatevalue(self, newvalue):

		# If the transition hasn't already started, start it now
		if newvalue != self.value:
			self.value = newvalue

		return self.updatetransition()

	# =========================================================================================

	def updatetransition(self):

		if (self.value == True) and (self.transitionstate < self.postscalesize):
			self.transitionstate = self.transitionstate + 1
		elif (self.value == False) and (self.transitionstate > self.prescalesize):
			self.transitionstate = self.transitionstate - 1

		return self.transitionstate
