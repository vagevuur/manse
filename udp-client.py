import socket

msgFromClient = " Inhoud van het bericht van de client... "
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("172.16.89.131", 1234)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Bericht van de server {}".format(msgFromServer[0])
print(msg)
