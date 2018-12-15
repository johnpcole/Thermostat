import os as OperatingSystem
import shutil as FileSystem


# ---------------------------------------------
# Reads a file from disk and returns a list,
# where each list item is a line in the file
# ---------------------------------------------

def readfromdisk(filename):

	newfilelist = []

	try:
		# Open the file for the duration of this process
		with open(filename, 'r') as fileobject:

			# Loop over all lines in the file
			for fileline in fileobject.readlines():

				# Only process if the line isn't blank
				if fileline != "":
					newfilelist.append(fileline.rstrip('\r\n'))

	except:
		# Print an error if the file cannot be read
		print("Cannot read file - ", filename)

	return newfilelist

	
	

# ---------------------------------------------
# Returns a list items found in the specified
# folderpath, with File/Folder/Unknown designations
# ---------------------------------------------

def getfolderlisting(folderpath):

	outcome = {}

	try:
		listing = OperatingSystem.listdir(folderpath)

		for listitem in listing:
			fullitempath = OperatingSystem.path.join(folderpath, listitem)
			if OperatingSystem.path.isfile(fullitempath) == True:
				itemtype = "File"
			elif OperatingSystem.path.isdir(fullitempath) == True:
				itemtype = "Folder"
			else:
				itemtype = "Unknown"
			outcome[listitem] = itemtype

	except:
		print("Cannot access folder - ", folderpath)

	return outcome



# ---------------------------------------------
# Returns a path based on a root and a subitem
# ---------------------------------------------

def concatenatepaths(path1, path2):

	return OperatingSystem.path.join(path1, path2)



# ---------------------------------------------
# Returns whether a path (file or folder) exists
# ---------------------------------------------

def doesexist(fullpath):

	return OperatingSystem.path.exists(fullpath)



# ---------------------------------------------
# Returns a file's extension
# ---------------------------------------------

def getextension(filename):

	if "." in filename:
		filenamesplit = filename.split(".")
		outcome = filenamesplit[len(filenamesplit) - 1]
	else:
		outcome = ""

	return outcome



# ---------------------------------------------
# Returns a file's name
# ---------------------------------------------

def getname(filename):

	extension = getextension(filename)

	if extension == "":
		if filename[-1:] == ".":
			outcome = filename[:-1]
		else:
			outcome = filename
	else:
		extensionlength = 0 - len(extension) - 1
		outcome = filename[:extensionlength]

	return outcome



# ---------------------------------------------
# Writes a file to disk from a list
# ---------------------------------------------

def writetodisk(filename, outputlist):

	newlist = []
	for originalitem in outputlist:
		newlist.append(originalitem)
		newlist.append("\n")

	try:
		# Open the file for the duration of this process
		with open(filename, 'w') as targetfile:

			# Print out all items in list
			targetfile.writelines(newlist)

	except:
		# Print an error if the file cannot be written
		print("Cannot write file - ", filename)



# ---------------------------------------------
# Copies a file from source to destination
# ---------------------------------------------

def copyfile(fullsourcepath, fulldestinationpath):

	outcome = True

	try:
		FileSystem.copy2(fullsourcepath, fulldestinationpath)

	except:
		print("Cannot copy file - ", fullsourcepath, fulldestinationpath)
		outcome = False

	return outcome



# ---------------------------------------------
# Makes a folder
# ---------------------------------------------

def makefolder(fullpath):

	outcome = True

	try:
		OperatingSystem.mkdir(fullpath)

	except:
		print("Cannot create folder - ", fullpath)
		outcome = False

	return outcome



# ---------------------------------------------
# Deletes a folder
# ---------------------------------------------

def deletefolder(fullpath):

	outcome = True

	try:
		FileSystem.rmtree(fullpath)

	except:
		print("Cannot delete folder - ", fullpath)
		outcome = False

	return outcome


