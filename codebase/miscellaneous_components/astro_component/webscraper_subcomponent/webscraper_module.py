from . import webscraper_class as WebScraperClass



def createscraper(locationname, longitude, latitude, timeshift):

	return WebScraperClass.DefineScraper(locationname, longitude, latitude, timeshift)
