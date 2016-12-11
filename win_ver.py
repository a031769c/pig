def win_ver():
    import _winreg
# Queries HKLM\SOFTWARE\Microsoft\Windows NT\CurrentConfig
# to determine the actual version name of the installed OS
    CurrentVersionKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
	"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
    RawKeyValue = _winreg.QueryValueEx(CurrentVersionKey,"ProductName")
    ProductName = str(RawKeyValue[0])
    _winreg.CloseKey(CurrentVersionKey)
    return ProductName