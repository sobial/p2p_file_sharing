import binascii
import socket                                     
from pdu import raw_pdu , A_type , R_type , O_type

#list of all files with their address. list of ditionaries   {  'file_ame': r_pdu.file_name,'port': r_pdu.port, 'ip': r_pdu.ip}
file_list = []

## create UDP socket
localIP     = "127.0.0.2"
localPort   = 20001
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# Listen for incoming datagrams
print("UDP server up and listening")




# pdu_type = "R"
while True:
    
    ## Recieve messages from client (UDP socket)
    ## convert recieved binary data to PDU
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    address = bytesAddressPair[1]
    bin_recived_message = bytesAddressPair[0].decode()

    print('recieved pdu from {}'.format(address))
   
    ##extract pdu_type
    # print(bin_recived_message[:8] , )
    # pdu = raw_pdu(bin_pdu=bin_recived_message)
    pdu_type = chr(int(bin_recived_message[:8] , 2))
    
   
    ## if the pair wants to register file
    if pdu_type == 'R':

        #making R_type pdu to extract file name, port and ip
        r_pdu = R_type(bin_data=bin_recived_message)

        #check if file doesn't exists in the list
        if (True):
            #registering in file_list
            file_list.append({  'file_ame': r_pdu.file_name,
                                'port': r_pdu.port,
                                'ip': r_pdu.ip
                            })
            print(file_list)
            #making A_type pdu (ack) to send back to peer
            a_pdu = A_type()
                
            #sending ack to peer
            UDPServerSocket.sendto(a_pdu.bin.encode(), address) 

        else:
            #sending E_type
            pass
        
        pass
        
    ## if the pait wants to remove a file
    elif pdu_type == 'U':
        pass
        
    ## if the pair wants to know the address of a specific file
    elif pdu_type == 'S':
        pass

    ## if pair wants to know the list of all files available in the network
    elif pdu_type == 'O':
        print('O received')
        pass
