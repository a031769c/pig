# For OS X

def osx_cpu():
	import subprocess
	raw = subprocess.check_output(["sysctl","-n","machdep.cpu.brand_string"])
	CPU = raw.split('\n')[0]
	return CPU

# For Linux

def lnx_cpu():
	proc = open('/proc/cpuinfo')
	for line in proc:
		if line.startswith('model name'):
			raw = line
	raw = raw.split('\t: ')[1]
	CPU = raw.split('\n')[0]
	return CPU

# For Windows

def win_cpu():
	import _winreg
	CentralProcessorKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
	"HARDWARE\DESCRIPTION\System\CentralProcessor\\0")
	# That extra slash is important, otherwise the \0 will be considered a null byte
	RawKeyValue = _winreg.QueryValueEx(CentralProcessorKey,"ProcessorNameString")
	CPU = str(RawKeyValue[0])
	_winreg.CloseKey(CentralProcessorKey)
	return CPU

# For Solaris

def sol_cpu():
	import subprocess
	raw = subprocess.check_output(["psrinfo","-pv"])
	raw = raw.split('\t')[-1]
	CPU = raw.split('\n')[0]
	return CPU

# For *BSD's?

def bsd_cpu():
	import subprocess
	raw = subprocess.check_output(["sysctl","hw.model"])
	raw = raw.split(': ')[1]
	CPU = raw.split('\n')[0]
	return CPU