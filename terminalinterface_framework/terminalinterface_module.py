import os as OperatingSystem



def clearscreen(debugmode):

	if debugmode == False:
		OperatingSystem.system('clear')



def scannetwork(filepath, debugmode):

	if debugmode == False:
		OperatingSystem.system('sudo arp-scan -l > ' + filepath)
