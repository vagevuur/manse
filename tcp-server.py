import socket
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(5)

bericht = "TCP-server luistert op poort {}!".format(port)
print(bericht)

while True:
    clientsocket, address = s.accept()
    bericht = ("Connectie vanaf {0} is geaccepteert").format(address)
    print(bericht)
    clientsocket.send(bytes("Bericht van de server!", "utf-8"))

