from . import ipaddress_class as IPAddressClass



# ---------------------------------------------------------
# Creates the IP Address using a x.x.x.x string
# ---------------------------------------------------------

def createfromstring(fulladdressstring):

	newaddress = IPAddressClass.DefineIPAddress()
	newaddress.setfromstring(fulladdressstring)
	return newaddress



# ---------------------------------------------------------
# Creates the IP Address using another IP Address object
# ---------------------------------------------------------

def createfromobject(macobject):

	newaddress = IPAddressClass.DefineIPAddress()
	newaddress.setfromobject(macobject)
	return newaddress



# ---------------------------------------------------------
# Compares two IP Addresses, returning True if
# they are identical
# ---------------------------------------------------------

def compare(first, second):

	if first.getvalue() == second.getvalue():
		outcome = True
	else:
		outcome = False
	return outcome
