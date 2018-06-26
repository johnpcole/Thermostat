from . import macaddress_class as MacAddressClass



# ---------------------------------------------------------
# Creates the MAC Address using a xx xx xx xx xx xx string
# ---------------------------------------------------------

def createfromstring(fulladdressstring):

	newaddress = MacAddressClass.DefineMacAddress()
	newaddress.setfromstring(fulladdressstring)
	return newaddress



# ---------------------------------------------------------
# Creates the MAC Address using another MAC Address object
# ---------------------------------------------------------

def createfromobject(macobject):

	newaddress = MacAddressClass.DefineMacAddress()
	newaddress.setfromobject(macobject)
	return newaddress



# ---------------------------------------------------------
# Compares two MAC Addresses, returning True if
# they are identical
# ---------------------------------------------------------

def compare(first, second):

	if first.getvalue() == second.getvalue():
		outcome = True
	else:
		outcome = False
	return outcome
