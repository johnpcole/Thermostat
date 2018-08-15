from . import astro_class as AstroClass



def createlocation(locationname, longitude, latitude, timeshift):

	return AstroClass.DefineAstro(locationname, longitude, latitude, timeshift)
