from ...common_components.vector_datatype import vector_module as Vector
from tempslider_subcomponent import tempslider_module as TempSlider
from scheduleslider_subcomponent import scheduleslider_module as ScheduleSlider
from pushbuttons_subcomponent import pushbuttons_module as PushButtons


class DefineButtonMetrics:

	def __init__(self):

		self.tempslider = TempSlider.createslider()

		self.scheduleslider = ScheduleSlider.createslider()

		self.pushbuttons = PushButtons.createpushbuttons()

		self.origin = Vector.createorigin()


	def calctimeslideroutline(self):

		return self.scheduleslider.calcslideroverall()



	def calctimeslidermarkrange(self, hourindex, sliderhourvalue):

		return self.scheduleslider.calculatemarkrange(hourindex, sliderhourvalue)



	def calctimeslidertimemetrics(self, hourindex, subindex, sliderhour):

		return self.scheduleslider.calcslidertimemetrics(hourindex, subindex, sliderhour)



	def calctimeslidertempmetrics(self, instructiontime, instructiontemp, sliderhour):

		return self.scheduleslider.calcslidertempmetrics(instructiontime, instructiontemp, sliderhour)



	def calctempslideroutline(self):

		return self.tempslider.calcslideroverall()



	def calctempslidermetrics(self, displaytemp, selectedtemp):

		return self.tempslider.calcslidermetrics(displaytemp, selectedtemp)



	def calcbuttonmetrics(self, control, buttonname, selectorvalue):

		return self.pushbuttons.calcbuttonmetrics(control, buttonname, selectorvalue)



	def calcschedulebuttonmetrics(self, buttonposition, buttonsize, selectordata, buttonname):

		return self.pushbuttons.calcschedulebuttonmetrics(buttonposition, buttonsize, selectordata, buttonname)



	def calcroundedcorneranchors(self, topleft, bottomright, index):

		return PushButtons.calcroundedcorneranchors(topleft, bottomright, index)



	def calcroundedcorneroffsets(self, mode):

		return PushButtons.calcroundedcorneroffsets(mode)

