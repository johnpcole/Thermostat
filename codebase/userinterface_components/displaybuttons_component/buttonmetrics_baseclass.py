from ...common_components.vector_datatype import vector_module as Vector
from tempslider_subcomponent import tempslider_module as TempSlider
from scheduleslider_subcomponent import scheduleslider_module as ScheduleSlider
from instructionslider_subcomponent import instructionslider_module as InstructionSlider
from pushbuttons_subcomponent import pushbuttons_module as PushButtons


class DefineButtonMetrics:

	def __init__(self, controls):

		self.tempslider = TempSlider.createslider(controls.getbuttonposition("Temp Slider"),
															controls.getbuttonsize("Temp Slider"))

		self.scheduleslider = ScheduleSlider.createslider(controls.getbuttonposition("Timeline Slider"),
															controls.getbuttonsize("Timeline Slider"))

		self.instructionslider = InstructionSlider.createslider(controls.getbuttonposition("Instruction Slider Hour"),
																controls.getbuttonsize("Instruction Slider Hour"),
																controls.getbuttonposition("Instruction Slider Min"),
																controls.getbuttonsize("Instruction Slider Min"),
																controls.getbuttonposition("Instruction Slider Temp"),
																controls.getbuttonsize("Instruction Slider Temp"))

		self.pushbuttons = PushButtons.createpushbuttons()

		self.origin = Vector.createorigin()



	def calcinstructionslidermetrics(self, mode, index, slidervalue):

		return self.instructionslider.calcslidermetrics(mode, index, slidervalue)



	def calcinstructionsliderrange(self, mode):

		return self.instructionslider.calculatesliderrange(mode)



	def calctimeslidermarkrange(self, hourindex, sliderhourvalue):

		return self.scheduleslider.calculatemarkrange(hourindex, sliderhourvalue)



	def calctimeslidertimemetrics(self, hourindex, subindex, sliderhour):

		return self.scheduleslider.calcslidertimemetrics(hourindex, subindex, sliderhour)



	def calctimeslidertempmetrics(self, instructiontime, instructiontemp, sliderhour):

		return self.scheduleslider.calcslidertempmetrics(instructiontime, instructiontemp, sliderhour)



	def calctempslidermisc(self):

		return self.tempslider.calcslidermisc()



	def calctempslidermetrics(self, displaytemp, selectedtemp):

		return self.tempslider.calcslidermetrics(displaytemp, selectedtemp)



	def calcbuttonmetrics(self, control, buttonname, selectorvalue):

		return PushButtons.calcbuttonmetrics(control, buttonname, selectorvalue)



	def calcschedulebuttonmetrics(self, buttonposition, buttonsize, selectordata, buttonname):

		return self.pushbuttons.calcschedulebuttonmetrics(buttonposition, buttonsize, selectordata, buttonname)



	def calcroundedcorneranchors(self, topleft, bottomright, index):

		return PushButtons.calcroundedcorneranchors(topleft, bottomright, index)



	def calcroundedcorneroffsets(self, mode):

		return PushButtons.calcroundedcorneroffsets(mode)

