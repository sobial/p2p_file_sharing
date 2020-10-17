import binascii
class raw_pdu:
    def __init__(self, data='', t='' , bin_pdu=''):
        print(bin_pdu)
        if bin_pdu == '':
            self.t = t
            self.data = data
            self.bin = self.pdu_to_binary()
        else :
            
            self.bin = bin_pdu
            self.t , self.data = self.binary_to_pdu()


    def binary_to_pdu (self):
        n = int(str(self.bin), 2)

        recieved_message = binascii.unhexlify('%x' % n)
        res = (recieved_message[0] , recieved_message[1:] )

        return res

    def binary_to_char (self , binar):
        print(binar)
        n = int(str(binar), 2)

        recieved_message = binascii.unhexlify('%x' % n)
        return recieved_message


    def pdu_to_binary (self):
        res = bin(int(binascii.hexlify(self.t + self.data), 16))
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

r = R_type(bin_data= '101001001100100011001110110011001101000011001110110101001101000011010110110110001101010011001100110100001100111011001100110010001110011011001100110011101101000')
print(r.ip)
print(r.port)