import pushbuttons_class as PushButtonsClass

def createpushbuttons():
	return PushButtonsClass.DefinePushButtons()


# Rounded Corners

def calcroundedcorneranchors(topleft, bottomright, index):

	if index[:3] == "top":
		ybase = topleft.gety()
		ysign = +1
	else:
		ybase = bottomright.gety()
		ysign = -1
	if index[-4:] == "left":
		xbase = topleft.getx()
		xsign = +1
	else:
		xbase = bottomright.getx()
		xsign = -1

	return xbase, xsign, ybase, ysign


def calcroundedcorneroffsets(mode):

	if mode == "vertical":
		startxoffset = 1
		startyoffset = 2
		endxoffset = 1
		endyoffset = 3
	else:
		startxoffset = 2
		startyoffset = 1
		endxoffset = 3
		endyoffset = 1

	return startxoffset, startyoffset, endxoffset, endyoffset



def calcbuttonmetrics(control, buttonname, selectorvalue):

	buttonlocation = control.getbuttonposition(buttonname)
	buttonsize = control.getbuttonsize(buttonname)
	buttoncolour = "Button"
	imagename = "Hide"

	if buttonname[-6:] == "Cancel":
		imagename = "cancel"
		buttoncolour = "Cancel"
	elif buttonname[-6:] == "Commit":
		imagename = "commit"
		buttoncolour = "Commit"
	elif buttonname[:9] == "Override ":
		timing = buttonname[9:]
		imagename = "timer_" + timing
		if selectorvalue == timing:
			buttoncolour = "Selected"
	elif buttonname == "Configure Schedule":
		imagename = "configure"
	elif buttonname == "Exit":
		imagename = "return"
	else:
		buttoncolour = "Black"

	return buttonlocation, buttonsize, imagename, buttoncolour
