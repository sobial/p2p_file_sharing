
import socket                                           
                                
## create UDP socket
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "\nGround Control to Major Tom\nYou're off your course\nDirection's wrong"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)   

## create PDU 

## this function converts recieved binary data to PDU
def binary_to_pdu (binary_data):
    pass

## this function converts PDU to binary data
## so we are able to send it through socket
def pdu_to_binary (pdu):
    pass


while True:
    
    ## Recieve messages from client (UDP socket)
    ## convert recieved binary data to PDU
    
    ##extract pdu_type
 
    ## if the pair wants to register file
    if pdu_type == 'R':
        pass
        
    ## if the pait wants to remove a file
    elif pdu_type == 'U':
        pass
        
    ## if the pair wants to know the address of a specific file
    elif pdu_type == 'S':
        pass

    ## if pair wants to know the list of all files available in the network
    elif pdu_type == 'O':
        pass
