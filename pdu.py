import binascii
class raw_pdu:
    def __init__(self, data='', t='' , bin_pdu=''):
       
        if bin_pdu == '':
            self.t = t
            self.data = data
            self.bin = self.pdu_to_binary()
        else :
            self.bin = bin_pdu
            self.t = self.binary_to_char(binar=bin_pdu[:8])
            self.data = self.binary_to_char(binar=bin_pdu[8:])


    def binary_to_char (self , binar):
      
        n = int(str(binar), 2)
        recieved_message = binascii.unhexlify('%x' % n)
        return recieved_message.decode()


    def pdu_to_binary (self):

        ingredients = self.t + self.data
        temp = ''
        for char in ingredients:
            o = ord(char)
            bina = format(o , '08b')
            temp += bina
        return temp

    #gets string and convert it to binary, char by char, returns str(binary)
    def char_to_binary (self , some_string):

        temp = ''
        for char in some_string:

            bina = format(ord(char) , '08b')
            temp += bina

        return temp 

  
#R_type pdu type[0:8] , ip[8:40] , port[40:56] , file_name[56:] 
class R_type(raw_pdu):

    def __init__(self, file_name='', port='', ip='', bin_data=''):

        #when making pdu for send 
        if bin_data == '':
            super().__init__(t='R' , data= ip + port + file_name )
            self.ip = ip
            self.ip_bin = self.ip_to_binary(ip)

            self.port = port
            self.port_bin = format(int(port) , '016b')

            self.file_name = file_name
            self.file_name_bin = self.char_to_binary(file_name)
            
            #for sending in UDP, send R_type.bin.encode()
            self.bin = '01010010' + self.ip_bin + self.port_bin + self.file_name_bin


        #when making pdu for receive
        else:
            super().__init__(bin_pdu = bin_data)
            self.ip = self.binary_to_ip(self.bin[8:40])

            self.port = str(int(self.bin[40:56] , 2))

            self.file_name = self.binary_to_char(self.bin[56:])

    #gets ip as string and convert it to 32-bit binary: '127.0.1.1' -> '01010101010'
    def ip_to_binary (self , ip ):
        range_arr = ip.split('.')
        bin_ip = ''
        for i in range_arr:
            bina = format(int(i) , '08b')
            bin_ip += bina
        return bin_ip

    #gets 32-bit binary in returns string ip: '1010101010101' -> '127.0.1.1'
    def binary_to_ip (self , bin_ip):
        ip = str(int(bin_ip[:8] , 2)) + '.' + str(int(bin_ip[8:16] , 2)) + '.' + str(int(bin_ip[16:24] , 2)) + '.' + str(int(bin_ip[24:32] , 2))
        return ip


class A_type(raw_pdu):
    def __init__(self, bin_data='0100000101000001'):
        if bin_data == '':
            super().__init__(t='A')
        else:
            super().__init__(bin_pdu = bin_data ,t= 'A')


class E_type(raw_pdu):
    def __init__(self, bin_data='' , error_msg=''):
        if bin_data == '':
            super().__init__(t= 'E' )
            self.error_msg = error_msg
        else:
            super().__init__(bin_pdu = bin_data)
            self.error_msg = self.binary_to_char(bin_data[8:])

class S_type(raw_pdu):
    def __init__(self, bin_data='', data=''):
        if bin_data == '':
            super().__init__(t= 'S' )
            self.data = data
        else:
            super().__init__(bin_pdu = bin_data)
            self.data = self.binary_to_char(bin_data[8:])

class D_type(raw_pdu):
    def __init__(self, bin_data='' , file_name=''):
        if bin_data == '':
            super().__init__(t= 'D' )
            self.file_name = file_name
        else:
            super().__init__(bin_pdu = bin_data)
            self.file_name = self.binary_to_char(bin_data[8:])

class F_type(raw_pdu):
    def __init__(self, bin_data='', data =''):
        if bin_data == '':
            super().__init__(t= 'F' )
            self.data = data
        else:
            super().__init__(bin_pdu = bin_data)
            self.data = bin_data[8:]

class L_type(raw_pdu):
    def __init__(self, bin_data='', data =''):
        if bin_data == '':
            super().__init__(t= 'L' )
            self.data = data
        else:
            super().__init__(bin_pdu = bin_data)
            self.data = bin_data[8:]

class O_type(raw_pdu):
    def __init__(self, bin_data='', data='01001111'):
        if bin_data == '':
            super().__init__(t= 'O' )
            self.data = data
        else:
            super().__init__(bin_pdu = bin_data)
            self.data = self.binary_to_char(bin_data[8:])


