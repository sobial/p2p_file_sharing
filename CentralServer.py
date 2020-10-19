import binascii
import socket                                     
import resource
from pdu import raw_pdu , A_type , R_type
            
file_list = []

## create UDP socket
localIP     = "127.0.0.2"
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

## create PDU 

## this function converts recieved binary data to PDU
def binary_to_pdu (binary_data):
    print(binary_data)
    n = int(binary_data, 2)

    recieved_message = binascii.unhexlify('%x' % n)

    return recieved_message

## this function converts PDU to binary data
## so we are able to send it through socket
def pdu_to_binary (pdu):
    pass

pdu_type = "R"
while True:
    
    ## Recieve messages from client (UDP socket)
    ## convert recieved binary data to PDU
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    # print('bin pdu after recv: ' , bytesAddressPair[0])
    bin_recived_message = bytesAddressPair[0].decode()
    # print(bin_recived_message)
    # print('here')
    # message = binary_to_pdu(bin_recived_message)

    address = bytesAddressPair[1]

    # clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)
    
    # print(clientMsg)
    # print(clientIP)

    # Sending a reply to client
    # UDPServerSocket.sendto(bytesToSend, address)   
    
    ##extract pdu_type
    pdu = raw_pdu(bin_pdu=bin_recived_message)
    pdu_type = pdu.t
    # print(pdu_type)

    ## if the pair wants to register file
    if pdu_type == 'R':
        r_pdu = R_type(bin_data=clientMsg)
        entry = (r_pdu.ip + r_pdu.port, r_pdu.file_name)
        file_list.append(entry)
        print('register message from client: ' , entry)
        a_pdu = A_type()
        UDPServerSocket.sendto(a_pdu.bin, address) 
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
