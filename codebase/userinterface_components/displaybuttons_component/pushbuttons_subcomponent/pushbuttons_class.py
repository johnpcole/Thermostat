from ....common_components.vector_datatype import vector_module as Vector



class DefinePushButtons:

	def __init__(self):

		self.schedulebuttontempoffset = Vector.createfromvalues(0, 37)



	def calcbuttonmetrics(self, control, buttonname, selectorvalue):

		buttonlocation = control.getbuttonposition(buttonname)
		buttonsize = control.getbuttonsize(buttonname)
		buttoncolour = "Grey"

		if buttonname[:9] == "Override ":
			timing = buttonname[9:]
			imagename = "timer_" + timing
			if selectorvalue == timing:
				buttoncolour = "Selected"
		elif buttonname[:5] == "Temp ":
			imagename = "c" + buttonname[6:]
		elif buttonname == "Exit":
			imagename = "return"
		elif buttonname[:16] == "Schedule Select ":
			imagename = "Hide"
		else:
			imagename = "configure"

		return buttonlocation, buttonsize, imagename, buttoncolour



	def calcschedulebuttonmetrics(self, buttonposition, buttonsize, selectordata, buttonname):

		timetext, temptext = selectordata.getbuttonmeaningbylabel(buttonname[-1:])

		timeposition = Vector.add(buttonposition, Vector.createfromvalues(int(buttonsize.getx() / 2), 0))

		tempposition = Vector.add(timeposition, self.schedulebuttontempoffset)

		return timetext.getsecondlesstext(), str(temptext), timeposition, tempposition
