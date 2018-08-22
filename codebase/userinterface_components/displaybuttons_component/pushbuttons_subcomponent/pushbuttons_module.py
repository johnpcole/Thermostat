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
