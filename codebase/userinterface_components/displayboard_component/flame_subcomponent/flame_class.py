from ....common_components.transition_datatype import transition_module as Transition
from ....common_components.enumeration_datatype import enumeration_module as Enumeration



class DefineFlame():

	def __init__(self):

		# Data for capturing the animation of the current temperature
		self.boilerstate = Transition.createupdowntransition(1000, 1500, False)

		self.flamestate = Enumeration.createenum(["Snooze", "Forced", "On", "Off", "Hidden", "Transitioning"], "Hidden")



	def updateflame(self, boilerswitchstatus, thermostatstatus):

		if (boilerswitchstatus == True) or (thermostatstatus == True):
			showflame = True
		else:
			showflame = False

		self.boilerstate.updatevalue(showflame)

		transitionfraction = self.boilerstate.gettransitionfraction()

		currentflamestate = Enumeration.copyexisting(self.flamestate)

		if transitionfraction > 0.2:
			if (boilerswitchstatus == False) and (thermostatstatus == True):
				self.flamestate.set("Snooze")
			else:
				if transitionfraction == 1.0:
					if (boilerswitchstatus == True) and (thermostatstatus == False):
						self.flamestate.set("Forced")
					else:
						self.flamestate.set("On")
						if currentflamestate.get("Snooze") == True:
							self.boilerstate.resettransition()
				else:
					if currentflamestate.get("Snooze") == False:
						self.flamestate.set("Transitioning")
		else:
			if transitionfraction > 0:
				self.flamestate.set("Off")
			else:
				self.flamestate.set("Hidden")

		return self.flamestate



	def getflamestate(self, label):

		return self.flamestate.get(label)



	def gettransitionfraction(self):

		return self.boilerstate.gettransitionfraction()
