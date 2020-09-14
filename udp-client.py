import socket

msgFromClient = " Inhoud van het bericht van de client... "
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("192.168.2.16", 1234)
bufferSize = 181

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Bericht van de server {}".format(msgFromServer[0])
print(msg)
