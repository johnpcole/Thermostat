from ....common_components.vector_datatype import vector_module as Vector



class DefinePushButtons:

	def __init__(self):

		self.schedulebuttontempoffset = Vector.createfromvalues(0, 37)



	def calcschedulebuttonmetrics(self, buttonposition, buttonsize, selectordata, buttonname):

		timetext, temptext = selectordata.getbuttonmeaningbylabel(buttonname[-1:])

		timeposition = Vector.add(buttonposition, Vector.createfromvalues(int(buttonsize.getx() / 2), 0))

		tempposition = Vector.add(timeposition, self.schedulebuttontempoffset)

		return timetext.getsecondlesstext(), str(temptext), timeposition, tempposition
