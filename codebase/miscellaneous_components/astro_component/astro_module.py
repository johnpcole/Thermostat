from . import astro_class as AstroClass



def createlocation(locationname, longitude, latitude, timeshift, connectionmode, currenttimeobject):

	return AstroClass.DefineAstro(locationname, longitude, latitude, timeshift, connectionmode, currenttimeobject)
