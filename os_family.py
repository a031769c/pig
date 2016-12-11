import platform

def os_family():
	# v 0.1 initial solution
	# Evaluates the returned string and 'beautifies' (Darwin <---> Apple Family)
	# it before presenting it the next round of modules
	# TO DO: Other BSDs, OpenIndiana?
	if platform.system() == "Darwin":
		Family = "Apple"
	elif platform.system() == "SunOS":
		Family = "Solaris"
	elif platform.system() == "Windows":
		Family = "Windows"
	elif platform.system() == "Linux":
		Family = "Linux"
	elif platform.system() == "FreeBSD":
		Family = "FreeBSD"
	return Family