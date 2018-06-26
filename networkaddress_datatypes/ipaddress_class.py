from . import networkaddressing_privatefunctions as AddressFunction

# ===========================================================================================================
# This class captures each device and its ports within a single object.
# ===========================================================================================================

class DefineIPAddress:

	def __init__(self):

		# The IP address, stored as a four member list of integers
		self.partaddress = [-999, -999, -999, -999]



# ===========================================================================================================
# Basic Value Setters
# ===========================================================================================================

# ---------------------------------------------------------
# Sets the IP Address using a x.x.x.x string
# ---------------------------------------------------------

	def setfromstring(self, fulladdressstring):

		# Split the string apart, using . as the delimiter
		rawpartaddresses = fulladdressstring.split(".")
		
		# Only process if there are four items
		if len(rawpartaddresses) == 4:
			
			# Loop over the four items
			for x in range(0, 4):
				
				# Store the integer, converted from string
				self.partaddress[x] = AddressFunction.convertstringtodec(rawpartaddresses[x])
		
		# Store a dummy address and print an error
		else:
			self.partaddress = [-999, -999, -999, -999]
			print "Invalid IP Address Format - ", fulladdressstring



# ---------------------------------------------------------
# Sets the IP Address using another IP Address object
# ---------------------------------------------------------

	def setfromobject(self, macobject):

		# Loop over the four octets
		for x in range(0, 4):
			
			# Copy over the integer values
			self.partaddress[x] = macobject.partaddress[x]



# ===========================================================================================================
# Get Information
# ===========================================================================================================

# ---------------------------------------------------------
# Returns the IP Address as a x.x.x.x string
# ---------------------------------------------------------

	def getvalue(self):

		return AddressFunction.createaddressstring(self.partaddress, 4, ".", "dec")


