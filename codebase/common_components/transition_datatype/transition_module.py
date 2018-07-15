from . import transition_class as TransitionClass



def createtransition(prescalesize, postscalesize, initialvalue):
	
	return TransitionClass.DefineTransition(prescalesize, postscalesize, initialvalue)
