from . import oldnewtransition_class as OldNewTransitionClass
from . import updowntransition_class as UpDownTransitionClass


def createoldnewtransition(prescalesize, postscalesize, initialvalue):
	
	return OldNewTransitionClass.DefineOldNewTransition(prescalesize, postscalesize, initialvalue)


def createupdowntransition(prescalesize, postscalesize, initialvalue):

	return UpDownTransitionClass.DefineUpDownTransition(prescalesize, postscalesize,  initialvalue)
