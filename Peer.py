import binascii
import socket                                           
import select
from pdu import R_type, raw_pdu , A_type , O_type

## create UDP socket in order to connect to central server
serverAddressPort   = ("127.0.0.2", 20001)
bufferSize          = 1024

TCP_port = 7777

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

## create PDU
def make_pdu (type , data):
    pdu = type + data
    return pdu

def binary_to_pdu (binary_pdu):
    pass

def pdu_to_binary (pdu):
    res = bin(int(binascii.hexlify(pdu), 16))
    return res

def select_file_name():
    pass

## remove a file from central server
def remove_file(filename):
    pass


## download file from another peer
def download_file(filename, ip, port):
    ## create TCP connection
    ## request download (D type PDU)
    ## recieve file (E,C or L type PDUs)
    pass


## create TCP socket listening to other peers requesting files in this peer
## port must be available (not in used by the others sockets)
## random port number? ask user? your choice!

## one socket for all other peers? one socket per peer? one socket per file? your choice!

## one socket for all peers approach:
## listen to other peers infinitely
## put this function in seperate thread? process? your choice!
def download_socket ():
    ## infinite service loop
    ## use select 
    pass


## main driver 
## ask user for input and answers user's requests according to input
# command = raw_input("enter your command:\n")
# print(command)
command = 'O'
while True:

    ## based on user input:
    ## O -> get files list from central server -> ask user for a file -> download that file
    ## L -> get local files 
    ## R -> register a new file on central server
    ## U -> remove a registered file from central server
    ## E -> exit program


    if command == 'O':
        ## fetch files list from server
        ## ask user for specific file
        ## fetch that file's address from server
        ## download that file from the owner peer 

        pdu = O_type()
        #sending O_type pdu in binary
        UDPClientSocket.sendto(pdu.bin.encode(), serverAddressPort)

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0]

        pass

    elif command == 'L':
        pass

    elif command == 'R':

        file_name = 'sobhani.mkv'
       
        my_ip = str(socket.gethostbyname(socket.gethostname()))

        #making R_type pdu to send
        pdu = R_type(ip=my_ip, port=str(TCP_port), file_name=file_name)

        #sending R_type pdu in binary
        UDPClientSocket.sendto(pdu.bin.encode(), serverAddressPort)
        
        #waiting for ack
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0]

        #revieved pdu from server A_type or E_type        
        rcv_pdu = raw_pdu(bin_pdu=msgFromServer.decode())

        break

    if command == 'U':
        pass

    if command == 'E':
        ## remove all registered files
        exit()
