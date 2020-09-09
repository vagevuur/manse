import socket

local_ip = "172.16.89.131"
port = 1234
bufferSize = 1024

berichtVanServer = " Hallo dit is over UDP... "
bytesToSend = str.encode(berichtVanServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to IP
UDPServerSocket.bind((local_ip, port))

print("UDP server up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Bericht van de client: {}   ".format(message)
    clientIP = "Client IP-adres: {}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)

