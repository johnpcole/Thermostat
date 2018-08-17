import astroitem_class as AstroItemClass

def createitem(astrotype, starttime, endtime, istomorrow, dstmode):
	return AstroItemClass.DefineItem(astrotype, starttime, endtime, istomorrow, dstmode)