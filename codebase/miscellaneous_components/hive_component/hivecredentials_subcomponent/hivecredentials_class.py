from ....common_components.fileprocessing_framework import fileprocessing_module as FileSystem


class DefineHiveCredentials:

	def __init__(self):

		credentials = FileSystem.readfromdisk('./data/hiveconnection.cfg')

		self.username = credentials[0]

		self.password = self.decodecredentials(credentials[1])



	def decodecredentials(self, encodedvalue):

		stringlength = len(encodedvalue)

		outcome = ""

		for stringindex in range(0, 50, 2):

			if (stringindex + 1) < stringlength:

				characternumber = int(encodedvalue[stringindex:stringindex+2])
				characternumber = (characternumber + 10000 - ((1 + int(stringindex / 2)) * 10)) % 100

				outcome = outcome + chr(characternumber + 31)

		return outcome
