
import socket                                           
                                
## create UDP socket
                

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
