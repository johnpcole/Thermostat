import time as TimeFunctions

def sanitiseunixdate(integervalue):

	return TimeFunctions.strftime('%Y-%m-%d %H:%M:%S', TimeFunctions.localtime(integervalue / 1000))



def getvalue(dictionary):

	return dictionary['displayValue']



def getpolltime(dictionary):

	return sanitiseunixdate(dictionary['reportReceivedTime'])



def getchangetime(dictionary):

	return sanitiseunixdate(dictionary['reportChangedTime'])
