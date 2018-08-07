from . import meteo_class as MeteoClass



def createlocation(locationname, longitude, latitude, timeshift):

	return MeteoClass.DefineMeteo(locationname, longitude, latitude, timeshift)
