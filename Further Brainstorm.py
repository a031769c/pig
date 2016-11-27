
import platform
return platform.system()
# value is either "Darwin","Windows","SunOS","Linux"
# Store this as value1

# if value1 = "Windows"
	return platform.release()
	# value 10/8.1/8(?)/8/7/Vista(?)




<Computer>
<Family>"Windows"</Family> # return platform.system()
<Version>"10"</Version> # return platorm.release()		} Combine logic to id
<IsServer>True</IsServer> # ?							} server or desktop version

<Computer>
<Family>"Darwin"</Family> # return platform.system()
<Version>"10.10.5"</Version> # return platform.mac_ver()

<Computer>
<Family>"Linux"</Family>
<Distribution>"Kali"</Distribution> , <Distribution>"Ubuntu"</Distribution> , <Distribution>"CentOS Linux"</Distribution> # return platform.linux_distribution first field
<Version>"kali-rolling"</Version> , <Version>"14.04"</Version> , <Version>"7.2.1511"</Version>  # return platform.linux_distribution second field

<Computer>
<Family>"SunOS"</Family> # return platform.system()
<Version>"11.3"</Version> # return platform.version()





import platform

def OS():
	return platform.system()
	print str
	return;


def OS():
	return platform.system()
	if str is "Darwin":
		return ("OS X or macOS")
	elif str is "SunOS":
		return ("Solaris")
	elif str is "Windows":
		return ("Windows")
	elif str is "Linux":
		return ("Linux")
	Family = str
	print Family()








