from ...common_components.vector_datatype import vector_module as Vector
#from ...common_components.clock_datatype import clock_module as Clock
#from ...common_components.transition_datatype import transition_module as Transition
#from .. import display_privatefunctions as DisplayFunction


class DefineButtons:

	def __init__(self, controls):

		self.startmenubuttons = controls.getbuttoncollection("Set Temp")

		self.textoffset = Vector.createfromvalues(25, 5)

		self.filloffset = Vector.createfromvalues(1, 1)

		self.fillresize = Vector.createfromvalues(-2, -2)

		self.sliderposition = Vector.createfromvalues(40, 25)

		self.slidersize = Vector.createfromvalues(400, 78)

		self.sliderstepsize = Vector.createfromvalues(self.slidersize.getx() / 25, 0)
		self.slidertextoffset = Vector.createfromvalues(0, 19)

		self.slidercurrenttextoffset = Vector.createfromvalues(0, 33)


	def drawmodaloverlay(self, control):

		outcome = {}

		if control.getbuttonstate("Start Menu") == "Hidden":
			outcome["Background Overlay"] = ("Image", "start_disabled", Vector.createorigin())

		return outcome



	def drawstartmenu(self, control, currentdesiredtemperature):

		outcome = {}

		for buttonname in self.startmenubuttons:
			if control.getbuttonstate(buttonname) != "Hidden":

				if buttonname == "Temp Slider":

					outcome["Slider Outline"] = ("Image", "slider_outline", Vector.add(self.sliderposition, Vector.createfromvalues(0, -1)))

					for temperature in range(3, 28):

						temp, boxposition, boxsize, boxcentre, boxfont = self.calcslidermetrics(temperature, control.getslidervalue())

						outcome["Slider Background " + temp] = ("Box", boxposition, boxsize, temp, "", 0)

						if (temperature == control.getslidervalue()) or (temperature == int(currentdesiredtemperature)):
							outcome["Slider Text " + temp] = ("Text", temp, boxcentre, "Centre", "Black", boxfont)
							#outcome["Slider Highlight " + temp] = ("Box", boxposition, boxsize, "", "Black", 1)

						if temperature == 3:
							outcome["Slider Outline"] = ("Image", "slider_outline", Vector.add(boxposition, Vector.createfromvalues(0, -1)))



				else:
					buttonlocation = control.getbuttonposition(buttonname)
					buttonsize = control.getbuttonsize(buttonname)
					buttonoverlaylocation = Vector.add(buttonlocation, self.filloffset)
					buttonoverlaysize = Vector.add(buttonsize, self.fillresize)

					if buttonname[:9] == "Override ":
						timing = buttonname[9:]
						textlocation = Vector.add(buttonlocation, self.textoffset)
						outcome[buttonname + " Logo"] = ("Image", "egg_timer", buttonlocation)
						outcome[buttonname + " Text"] = ("Text", timing, textlocation, "Left", "Black", "Snooze")


					outcome[buttonname + " Fill"] = ("Box", buttonoverlaylocation, buttonoverlaysize, "Dark Grey", "", 0)
					outcome[buttonname + "Outline"] = ("Image", "button_outline", buttonlocation)

		return outcome



	def calcslidermetrics(self, displaytemp, selectedtemp):

		if displaytemp > selectedtemp:
			step = displaytemp - 2
		else:
			step = displaytemp - 4

		if displaytemp == selectedtemp:
			boxwidth = self.sliderstepsize.getscaled(3)
		else:
			boxwidth = self.sliderstepsize

		boxsize = Vector.createfromvalues(boxwidth.getx(), self.slidersize.gety())
		boxposition = Vector.add(self.sliderposition, self.sliderstepsize.getscaled(step))
		centreoffset = Vector.add(boxposition, boxwidth.getscaled(0.5))

		if displaytemp == selectedtemp:
			boxcentre = Vector.add(centreoffset, self.slidertextoffset)
			font = "Button Temps"
		else:
			boxcentre = Vector.add(centreoffset, self.slidercurrenttextoffset)
			font = "Snooze"

		return str(displaytemp), boxposition, boxsize, boxcentre, font


