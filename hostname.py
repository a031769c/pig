import socket

def hostname():
	hostname = socket.gethostname()
	hostname = hostname.split('.')[0]
	return hostname
