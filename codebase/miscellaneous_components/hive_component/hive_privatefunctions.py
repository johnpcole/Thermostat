import time as TimeFunctions

def sanitiseunixdate(integervalue):

	return TimeFunctions.strftime('%Y-%m-%d %H:%M:%S', TimeFunctions.localtime(integervalue / 1000))



def getvalue(dictionary):

	return dictionary['displayValue']



def getpolltime(dictionary):

	return sanitiseunixdate(dictionary['reportReceivedTime'])



def getchangetime(dictionary):

	return sanitiseunixdate(dictionary['reportChangedTime'])



def identifydevice(deviceattributes):

	if 'nodeType' in deviceattributes:
		rawdevicetype = getvalue(deviceattributes['nodeType'])
	else:
		rawdevicetype = 'Cannot find node type'
	devicetype = "OTHER"
	if rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostatui.json#':
		devicetype = "Thermostat"
	elif rawdevicetype == 'http://alertme.com/schema/json/node.class.hub.json#':
		devicetype = "Home Hub"
	elif rawdevicetype == 'http://alertme.com/schema/json/node.class.thermostat.json#':
		if 'powerSupply' in deviceattributes:
			devicetype = "Boiler Switch"
		elif 'schedule' in deviceattributes:
			devicetype = "Controller"

	return devicetype
