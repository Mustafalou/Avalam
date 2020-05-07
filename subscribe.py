import json
def sendJSON(socket, data):
	msg = json.dumps(data).encode('utf8')
	total = 0
	while total < len(msg):
		sent = socket.send(msg[total:])
		total += sent
import socket
import sys
IP = '127.0.0.1'
port = 3001
s=socket.socket()

s.connect((IP,port))
if len(sys.argv) > 1:
    port=int(sys.argv[1])
else:
    port=9090

TCP = {
    "matricules" : ["17292"],
    "port" : port,
    "name" : "Mustafalou"
}


sendJSON(s, TCP)
