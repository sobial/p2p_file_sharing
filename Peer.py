import binascii
import socket                                           
import select

## create UDP socket in order to connect to central server
serverAddressPort   = ("127.0.0.2", 20001)
bufferSize          = 1024

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

# msgFromClient       = "\nThis is Major Tom to Ground Control\nI'm stepping through the door"
# bytesToSend         = str.encode(msgFromClient)

# Send to server using created UDP socket
# UDPClientSocket.sendto(make_pdu( "R", bytesToSend), serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# msg = "Message from Server {}".format(msgFromServer[0])
# print(msg)


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
command = 'R'
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
        pass

    elif command == 'L':
        pass

    elif command == 'R':
        # file_name = raw_input("enter file name\n")
        file_name = 'fdsgfh.mkv'
       
        my_addr = str(socket.gethostbyname(socket.gethostname()))

        pdu = make_pdu('R', file_name + my_addr)
        bin_pdu = pdu_to_binary (pdu)

        UDPClientSocket.sendto(bin_pdu, serverAddressPort)
        
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

        msg = "Message from Server: {}".format(msgFromServer[0])
        print(msg)
        break

    if command == 'U':
        pass

    if command == 'E':
        ## remove all registered files
        exit()
