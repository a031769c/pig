import platform

def osx_ver():
	# v0.1.3 proposed solution (minor revision: trailing dots on version numbers readded to older version numbers)
	# evaluates the first string within "mac_ver" [0], looking for version number then 'beautifies' the string for output.
	# TO DO: tested and proven on Yosemite, El Capitan & Sierra. Need to test on Mavericks & older if possible.
	if "10.6." in platform.mac_ver()[0]:
		Version = "OS X Snow Leopard "+platform.mac_ver()[0]
	elif "10.7." in platform.mac_ver()[0]:
		Version = "OS X Lion "+platform.mac_ver()[0]
	elif "10.8." in platform.mac_ver()[0]:
		Version = "OS X Mountain Lion "+platform.mac_ver()[0]
	elif "10.9." in platform.mac_ver()[0]:
		Version = "OS X Mavericks "+platform.mac_ver()[0]
	elif "10.10." in platform.mac_ver()[0]:
		Version = "OS X Yosemite "+platform.mac_ver()[0]
	elif "10.11" in platform.mac_ver()[0]:
		Version = "OS X El Capitan "+platform.mac_ver()[0]
	elif "10.12" in platform.mac_ver()[0]:
		# trailing full stop(s) removed as not always a 10.12.1 version
		# this is unlikely to create ambiguity with either older or newer/future releases.
		Version = "macOS Sierra "+platform.mac_ver()[0]
	return Version
	print Version