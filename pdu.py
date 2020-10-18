import binascii
class raw_pdu:
    def __init__(self, data='', t='' , bin_pdu=''):
        # print(bin_pdu)
        if bin_pdu == '':
            self.t = t
            self.data = data
            self.bin = self.pdu_to_binary()
        else :
            self.bin = bin_pdu
            # print(bin_pdu[:7])
            self.t = self.binary_to_char(binar=bin_pdu[:7])
            # print('******')
            # print(self.t)
            self.data = self.binary_to_char(binar=bin_pdu[8:])


    def binary_to_pdu (self):
        n = int(str(self.bin), 2)

        recieved_message = binascii.unhexlify('%x' % n)
        res = (recieved_message[0].decode() , recieved_message[1:])

        return res

    def binary_to_char (self , binar):
        # print('binar is: ', binar)
        # print(type(binar))
        n = int(str(binar), 2)

        recieved_message = binascii.unhexlify('%x' % n)
        return recieved_message.decode()


    def pdu_to_binary (self):
        # print(type(self.t + self.data))
        ingredients = self.t + self.data
        res = bin(int(binascii.hexlify(ingredients.encode()), 16))
        return res


class R_type(raw_pdu):
    def __init__(self, file_name='', port='', ip='', bin_data=''):
        if bin_data == '':
            super().__init__(t= 'R' , data= ip + port + file_name )
            self.ip = ip
            self.port = port
            self.file_name = file_name
        else:
            super().__init__(bin_pdu = bin_data)
            self.ip = self.binary_to_char(self.bin[8:39])
            self.port = self.binary_to_char(self.bin[40:55])
            self.file_name = self.binary_to_char(self.bin[56:])

class A_type(raw_pdu):
    def __init__(self, bin_data=''):
        if bin_data == '':
            super().__init__(t= 'A')
        else:
            super().__init__(bin_pdu = bin_data)

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


r = R_type(ip='1234578' , port='12345', file_name='fgdfhgdfbdf')
print(r.ip)
print(r.port)
