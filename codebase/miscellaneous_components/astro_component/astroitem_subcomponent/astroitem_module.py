import astroitem_class as AstroItemClass

def createitem(astrotype, starttime, endtime, istomorrow):
	return AstroItemClass.DefineItem(astrotype, starttime, endtime, istomorrow)