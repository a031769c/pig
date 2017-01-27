import socket
import select
import json
import sqlite3
import time

def getClientStuff(ClientData):
   jsond = json.loads(ClientData)
   return jsond

def create_db():
    sqlite_file = '/tmp/pig.db'
    # the database path & name (pig.db)
    conn = sqlite3.connect(sqlite_file)
    # the connection to the db
    c = conn.cursor()
    # check operating system, 
    # create directory for server config
    c.execute('''CREATE TABLE IF NOT EXISTS clients
        (PK_ID integer PRIMARY KEY,
        UUID text NOT NULL,
        TIME_STAMP text NOT NULL,
        HOST text NOT NULL,
        IP text NOT NULL,
        OS text NOT NULL,
        ARCH text NOT NULL,
        CPU text NOT NULL
        )''');
    conn.commit()
    conn.close()

def insert_record():
    sqlite_file = '/tmp/pig.db'
    # the database path & name (pig.db)
    conn = sqlite3.connect(sqlite_file)
    conn.text_factory = sqlite3.OptimizedUnicode
    c = conn.cursor()
    values = stuff.items()
    list_of_vals = []
    for i in values:
        value = i[1]
        list_of_vals.append(value)
    print "New client connected from "+client.getpeername()[0]+". Added to DB..."
    c.execute('INSERT INTO clients(UUID,TIME_STAMP,HOST,IP,OS,ARCH,CPU) VALUES (?,?,?,?,?,?,?)', list_of_vals)
    conn.commit()
    conn.close()

# server for multiple clients, taken from intro to python sockets half day

HOST =''
PORT = 9001
CREATE_DB = create_db()

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
                stuff['TIME_STAMP'] = str(time.time())
                stuff['IP'] = client.getpeername()[0]
                insert_record()               
            if s in writable:
                s.sendall(data)
