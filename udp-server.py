import socket

local_ip = "192.168.2.16"
port = 1234
bufferSize = 1024

berichtVanServer = " Hallo dit is de server over UDP... "
bytesToSend = str.encode(berichtVanServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# UDPServerSocket.connect((socket.gethostname(), port))

# Bind to IP
UDPServerSocket.bind((local_ip, port))

bericht = "UDP server luistert op poort {}".format(port)
print(bericht)

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Bericht van de client: {}   ".format(message)
    clientIP = "Client IP-adres: {}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)

