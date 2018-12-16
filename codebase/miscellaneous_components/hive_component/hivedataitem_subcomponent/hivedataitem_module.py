from . import astroitem_class as AstroItemClass

def createitem(astrotype, starttime, endtime, date, startvalidity, endvalidity):
	return AstroItemClass.DefineItem(astrotype, starttime, endtime, date, startvalidity, endvalidity)