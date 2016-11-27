import platform

def sol_ver():
	# v0.1 initial solution
	# evaluates that is is Solaris family before 'beautifies' string with version number
	# TO DO:  Tested on Solaris 11.3, what about OpenIndiana or older versions?
	if platform.system() == "SunOS":
		Version = "Solaris "+platform.version()
	return Version
	print Version