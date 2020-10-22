import binascii
class raw_pdu:
    def __init__(self, data='', t='' , bin_pdu=''):
        # print(bin_pdu)
        # bin_pdu = bin_pdu.decode()
        # print(bin_pdu)
        if bin_pdu == '':
            self.data_bin = ''
            self.t = t
            self.data = data
            self.bin = self.pdu_to_binary()
        else :
            self.bin = bin_pdu
            print(bin_pdu[:8])
            self.t = self.binary_to_char(binar=bin_pdu[:8])
            # print('******')
            # print(self.t)
            self.data = self.binary_to_char(binar=bin_pdu[8:])


    def binary_to_pdu (self):
        n = int(str(self.bin), 2)

        recieved_message = binascii.unhexlify('%x' % n)
        res = (recieved_message[0].decode() , recieved_message[1:])

        return res

    def binary_to_char (self , binar):
        print('binar is: ', binar)
        print(type(binar))
        n = int(str(binar), 2)
        print('n is ' , n)
        recieved_message = binascii.unhexlify('%x' % n)
        print('recv msg is ' ,recieved_message)
        return recieved_message.decode()


    def pdu_to_binary (self):
        # print(type(self.t + self.data))
        ingredients = self.t + self.data
        # print('pdu 2 binary :' , ingredients)
        # hex_msg = binascii.hexlify(ingredients.encode())
        # res = "{0:b}".format(int(hex_msg.decode(), 16))
        # print('res is: ' , type(res))
        # res = "{0:b}".format((int(binascii.hexlify(ingredients.encode()).decode(), 16)))

        print('ingredients are: ' , ingredients)
        temp = ''
        for char in ingredients:
            o = ord(char)
            bina = format(o , '08b')
            # print(o , bina)
            temp += bina
            # print(temp)
        print( 'temp is: ',temp)
        return temp


    def char_to_binary (self , some_string):

        temp = ''
        for char in some_string:
            o = ord(char)
            bina = format(o , '08b')
            # print(o , bina)
            temp += bina
            # print(temp)
        print( 'temp is: ',temp)

        return temp 

    # def dec_to_binary(self , dec):

    #     temp = ''
    #     for char in some_string:
    #         o = ord(char)
    #         bina = format(o , '08b')
    #         # print(o , bina)
    #         temp += bina
    #         # print(temp)
    #     print( 'temp is: ',temp)

    #     return temp 
                   



class R_type(raw_pdu):
    def __init__(self, file_name='', port='', ip='', bin_data=''):
        if bin_data == '':
            super().__init__(t='R' , data= ip + port + file_name )
            print(self.t , ip , port , file_name)
            self.ip = ip
            print('ip: ' , ip)
            self.ip_bin = self.ip_to_binary(ip)
            print('ip bin: ' , self.ip_bin)
            self.port = port
            self.port_bin = format(int(port) , '016b')
            print('port bin: ' , self.port_bin)

            self.file_name = file_name
            self.file_name_bin = self.char_to_binary(file_name)
            print('file name bin: ' , self.file_name_bin)

            self.data_bin = '01010010' + self.ip_bin + self.port_bin + self.file_name_bin

        else:
            super().__init__(bin_pdu = bin_data)
            self.ip = self.binary_to_ip(self.bin[8:39])
            print(self.bin[8:39])
            print('ip is: ' , self.ip)
            self.port = self.binary_to_char(self.bin[40:56])
            self.file_name = self.binary_to_char(self.bin[56:])

    #gets ip as string and convert it to 32-bit binary: '127.0.1.1' -> '01010101010'
    def ip_to_binary (self , ip ):
        range_arr = self.ip.split('.')
        bin_ip = ''
        for i in range_arr:

            bina = format(int(i) , '08b')
            bin_ip += bina
        return bin_ip
    #gets 32-bit binary in returns string ip: '1010101010101' -> '127.0.1.1'
    def binary_to_ip (self , bin_ip):
        ip = str(int(bin_ip[:7] , 2)) + '.' + str(int(bin_ip[8:15] , 2)) + '.' + str(int(bin_ip[16:23] , 2)) + '.' + str(int(bin_ip[24:31] , 2))
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


# r = R_type(ip='1234578' , port='12345', file_name='fgdfhgdfbdf')
# print(r.ip)
# print(r.port)
