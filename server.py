import socket
import select
import json

def getClientStuff(ClientData):
   jsond = json.loads(ClientData)
   return jsond

# server for multiple clients, taken from intro to python sockets half day

HOST =''
PORT = 9001

master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
master_socket.setblocking(0)
master_socket.bind((HOST, PORT))
master_socket.listen(1)
sockets = []
sockets.append(master_socket)

while True:
    (readable, writable, exceptional) = select.select(sockets, [], sockets)
    for s in readable:
        if s is master_socket:
            (client, _) = master_socket.accept()
            client.setblocking(0)
            sockets.append(client)
        else:
            data = s.recv(1024).decode("utf-8")
            if data == '':
                s.shutdown(socket.SHUT_RDWR)
                s.close()
                sockets.remove(s)
            else:
                stuff = getClientStuff(data)
                print "\n"
                print "IP Address:",client.getpeername()[0]
                print "Hostname:",stuff['Hostname']
                print "Operating System:",stuff['Operating System']
                print "CPU Name:",stuff['CPU']
                print "Architecture:",stuff['ARCH']
                print "\n"
            if s in writable:
                s.sendall(data)


