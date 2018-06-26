
# ---------------------------------------------------------
# Converts a decimal string representation of an octet,
# without any prefix, into an integer decimal
# ---------------------------------------------------------

def convertstringtodec(rawdec):

	try:
		outcome = sanitiseoctet(int(rawdec))
	except:
		outcome = -999

	return outcome



# ---------------------------------------------------------
# Converts a hexadecimal string representation of an octet,
# without the 0x prefix, into an integer decimal
# ---------------------------------------------------------

def converthextodec(rawhex):

	try:
		outcome = sanitiseoctet(int(rawhex, 16))
	except:
		outcome = -999

	return outcome



# ---------------------------------------------------------
# Converts a decimal integer representation of an octet,
# into a hexadecimal string without the 0x prefix
# ---------------------------------------------------------

def convertdectohex(rawdec):

	if isvalidoctet(rawdec) == True:
		outcome = (hex(rawdec))[2:]
		if len(outcome) == 1:
			outcome = "0" + outcome
	else:
		outcome = "??"

	return outcome



# ---------------------------------------------------------
# Determines whether an integer decimal is between 0 & 255
# ---------------------------------------------------------

def isvalidoctet(decimalvalue):

	outcome = False
	if decimalvalue > -1:
		if decimalvalue < 256:
			outcome = True

	return outcome



# ---------------------------------------------------------
# Returns decimal integer octet value passed in, if 0-255,
# otherwise returns -999
# ---------------------------------------------------------

def sanitiseoctet(decimalvalue):

	if isvalidoctet(decimalvalue) == True:
		outcome = decimalvalue
	else:
		outcome = -999

	return outcome



# ---------------------------------------------------------
# Returns a string representation of an address (IP or MAC)
# ---------------------------------------------------------

def createaddressstring(partaddresslist, addresslength, delimitercharacter, addressbase):

	# Start with a blank overall string
	outcome = ""
	
	# Loop over the 4/6 octets
	for x in range(0, addresslength):
	
		# Only process if the octet is valid (0-255)
		if isvalidoctet(partaddresslist[x]) == True:
			
			# Convert to variable length decimal string
			if addressbase == "dec":
				convertedpartaddress = str(partaddresslist[x])
			
			# Convert to fixed length hexidecimal string
			elif addressbase == "hex":
				convertedpartaddress = convertdectohex(partaddresslist[x])
			
			# Error
			else:
				convertedpartaddress = "?????"
				print "Invalid Address Base - ", addressbase
		
		# Otherwise add a question mark
		else:
			convertedpartaddress = "??"
		
		# If its not the first octet, delimit with a .
		if x > 0:
			outcome = outcome + "."
		
		# Add the latest octet to the overall string
		outcome = outcome + convertedpartaddress

	return outcome
