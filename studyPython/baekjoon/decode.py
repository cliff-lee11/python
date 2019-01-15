import struct, hashlib, time
import binascii
import os
from Crypto.Cipher import AES


def decrypt_file(key, in_filename, out_filename, chunksize=24 * 1024):
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        #iv = infile.read(16)
        iv = '51d194c898c6dddbd3eb54fc290a83a7'
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)




def main():
    #password = make_pass()
    #key = hashlib.sha256(password).digest()
    #print binascii.hexlify(bytearray(key))
    #in_filename = 'PER_PUBLIC_201807261500.csv.enc'
    #encrypt_file(key, in_filename, out_filename='output')
    #print 'Encrypte Done !'

    #delete original file

    #decrypt
    key = 'e9a815ab6f761a1360f535f4ff70254506a9ed6115bd6d2191a10df16fb42297'
    decrypt_file(key, in_filename='PER_PUBLIC_201807261500.csv.enc', out_filename='PER_PUBLIC_201807261500.csv')

   #outfile = open('original.hwp')
   # magic = outfile.read(8)

   # print 'Magic Number : ' + magic.encode('hex')
   # if magic.encode('hex') == 'd0cf11e0a1b11ae1':
   #     print 'This document is a HWP file.'
   #     
