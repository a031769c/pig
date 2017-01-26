import platform
import socket

def hostname():
    hostname = socket.gethostname()
    hostname = hostname.split('.')[0]
    return hostname

def os_family():
    if platform.system() == "Darwin":
        Family = "Apple"
    elif platform.system() == "SunOS":
        Family = "Solaris"
    elif platform.system() == "Windows" or platform.system() == "Microsoft":
        Family = "Windows"
    elif platform.system() == "Linux":
        Family = "Linux"
    elif platform.system() == "FreeBSD":
        Family = "FreeBSD"
    else:
        Family = "Unknown"
    return Family

def osx_ver():
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
        Version = "macOS Sierra "+platform.mac_ver()[0]
    return Version

def sol_ver():
    if platform.system() == "SunOS":
        Version = "Solaris "+platform.version()
    return Version

def lnx_ver():
    if platform.linux_distribution()[0] == '':
        Version = "Linux (Other)"
    elif platform.linux_distribution()[1] == '':
        Version = platform.linux_distribution()[0]
    elif platform.linux_distribution()[1][0].isdigit():
        Version = platform.linux_distribution()[0]\
        +' '+platform.linux_distribution()[1]
    elif platform.linux_distribution()[1][0].isdigit() == False:
        Version = platform.linux_distribution()[0]
    return Version

def win_ver():
    CurrentVersionKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
    "SOFTWARE\Microsoft\Windows NT\CurrentVersion")
    RawKeyValue = _winreg.QueryValueEx(CurrentVersionKey,"ProductName")
    Version = str(RawKeyValue[0])
    _winreg.CloseKey(CurrentVersionKey)
    return Version

# TO DO:  bsd_ver():

def osx_cpu():
    raw = subprocess.check_output(["sysctl","-n","machdep.cpu.brand_string"])
    CPU = raw.split('\n')[0]
    return CPU

def sol_cpu():
    raw = subprocess.check_output(["psrinfo","-pv"])
    raw = raw.split('\t')[-1]
    CPU = raw.split('\n')[0]
    return CPU

def lnx_cpu():
    proc = open('/proc/cpuinfo')
    for line in proc:
        if line.startswith('model name'):
            raw = line
    raw = raw.split('\t: ')[1]
    CPU = raw.split('\n')[0]
    return CPU

def win_cpu():
    CentralProcessorKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
    "HARDWARE\DESCRIPTION\System\CentralProcessor\\0")
    # That extra slash is important, otherwise the \0 will be considered a null byte
    RawKeyValue = _winreg.QueryValueEx(CentralProcessorKey,"ProcessorNameString")
    CPU = str(RawKeyValue[0])
    _winreg.CloseKey(CentralProcessorKey)
    return CPU

def bsd_cpu():
    raw = subprocess.check_output(["sysctl","hw.model"])
    raw = raw.split(': ')[1]
    CPU = raw.split('\n')[0]
    return CPU

def osx_arch():
    if "10.6." in platform.mac_ver()[0]:
        sysctl = subprocess.check_output(['sysctl','hw.cpu64bit_capable'])
        sysctl = sysctl.split(' ')[1]
        test64 = int(sysctl.split('\n')[0])
        if test64 == 0:
            arch = '32 Bit (Intel x86)'
    else:
        arch = '64 Bit (Intel EM-64T)'
    return arch

def sol_arch():
    isainfo = subprocess.check_output(['isainfo','-v'])
    isainfo = isainfo.split('\n')[0]
    isainfo = isainfo.split(' ')
    if 'Intel' in CPU_NAME:
        if '64' in isainfo[0]:
            arch = '64 Bit (Intel EM-64T)'
        elif '32' in isainfo[0]:
            arch = '32 Bit (Intel x86)'
    elif 'AMD' in CPU_NAME:
        if '64' in isainfo[0]:
            arch = '64 Bit (AMD64)'
        elif '32' in isainfo[0]:
            arch = '32 Bit (AMD x86)'
    elif "sparc" in isainfo[1]:
        if '64' in isainfo[0]:
            arch = '64 Bit (Sun SPARC)'
        elif '32' in isainfo[0]:
            arch = '32 Bit (Sun SPARC)'
    else:
        arch = "Unknown"
    return arch

def win_lnx_arch():
    if 'Intel' in CPU_NAME:
        if '64' in platform.architecture()[0]:
            arch = '64 Bit (Intel EM-64T)'
        elif '32' in platform.architecture()[0]:
            arch = '32 Bit (Intel x86)'
    elif 'AMD' in CPU_NAME:
        if '64' in platform.architecture()[0]:
            arch = '64 Bit (AMD64)'
        elif '32' in platform.architecture()[0]:
            arch = '32 Bit (AMD x86)'
    elif 'arm' in platform.machine.architecture()[0]:
        arch = 'ARM'
    else:
        arch = "Unknown"
    return arch

# TO DO: bsd_arch()

HOSTNAME = hostname()
OS_FAMILY = os_family()

if OS_FAMILY == "Apple":
    import subprocess
    OS_VERSION = osx_ver()
    CPU_NAME = osx_cpu()
    ARCH = osx_arch()
elif OS_FAMILY == "Solaris":
    import subprocess
    OS_VERSION = sol_ver()
    CPU_NAME = sol_cpu()
    ARCH = sol_arch()
elif OS_FAMILY == "Linux":
    OS_VERSION = lnx_ver()
    CPU_NAME = lnx_cpu()
    ARCH = win_lnx_arch()
elif OS_FAMILY == "Windows":
    import _winreg
    OS_VERSION = win_ver()
    CPU_NAME = win_cpu()
    ARCH = win_lnx_arch()
# elif OS_FAMILY == "FreeBSD":
#    import subprocess
#    OS_VERSION = bsd_ver()
#    CPU_NAME = bsd_cpu()
#    ARCH = bsd_arch()

output = {"HOST":HOSTNAME,"OS":OS_VERSION,"CPU":CPU_NAME,"ARCH":ARCH}
import json
json_output = json.dumps(output,ensure_ascii=False)
json_output = json_output.encode("utf-8")
# HOST = raw_input("Enter the IPv4 address of the central server e.g 192.168.1.1\n\n")
HOST = "192.168.2.16"
# Currently a hard coded server IP
PORT = 9001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(json_output)
print repr(json_output)

