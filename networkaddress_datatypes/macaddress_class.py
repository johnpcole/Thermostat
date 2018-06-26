from . import networkaddressing_privatefunctions as AddressFunction

# ===========================================================================================================
# This class captures each device and its ports within a single object.
# ===========================================================================================================

class DefineMacAddress:

	def __init__(self):

		# The Mac address, stored as a six member list of integers
		self.partaddress = [-999, -999, -999, -999, -999, -999]



# ===========================================================================================================
# Basic Value Setters
# ===========================================================================================================

# ---------------------------------------------------------
# Sets the Mac Address using a xx xx xx xx xx xx string
# ---------------------------------------------------------

	def setfromstring(self, fulladdressstring):

		# As there is no set delimiter, the string must be 17 characters long
		if len(fulladdressstring) == 17:
			
			# Loop over the six pairs of digits
			for x in range(0, 6):
				
				# Substring location of digit-pair
				addresslocation = x * 3
				
				# Store the integer, converted from string
				self.partaddress[x] = AddressFunction.converthextodec(fulladdressstring[addresslocation : addresslocation + 2])
		
		# Store a dummy address and print an error
		else:
			self.partaddress = [-999, -999, -999, -999, -999, -999]
			print "Invalid MAC Address Format - ", fulladdressstring



# ---------------------------------------------------------
# Sets the MAC Address using another MAC Address object
# ---------------------------------------------------------

	def setfromobject(self, macobject):

		# Loop over the six octets
		for x in range(0, 6):
		
			# Copy over the integer values
			self.partaddress[x] = macobject.partaddress[x]



# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# Returns the MAC Address as a xx:xx:xx:xx:xx:xx string
# ---------------------------------------------------------

	def getvalue(self):

		return AddressFunction.createaddressstring(self.partaddress, 6, ":", "hex")

