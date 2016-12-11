import platform

def isNumericVers():
	return any(char.isdigit() 
	for char in platform.linux_distribution()[1])

VersNum = isNumericVers()

def distribution():
	if platform.linux_distribution()[0] == '':
		dist = "Linux (Other)"
	elif VersNum == True:
		dist = str(platform.linux_distribution()[0]
			+' '+platform.linux_distribution()[1])
	return dist

# platform.linux_distribution()

# OpenSUSE 42
# ('openSUSE','42.2','x86_64')

# Fedora 25
# ('Fedora','25','Twenty Five')

# Mint 18
# ('LinuxMint','18','sarah')

# Ubuntu 14 LTS
# ('Ubuntu','14.04','trusty')

# Debian 8
# ('debian','8.6','')

# RHEL 7
# ('Red Hat Enterprise Linux Server','7.2','Maipo')

# CentOS 7
# ('CentOS Linux','7.2.1511','Core')

# Kali
# ('Kali','kali-rolling','kali-rolling')

