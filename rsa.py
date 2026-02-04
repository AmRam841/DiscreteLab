#publickey module -
from Crypto.PublicKey import RSA

#from Crypto.PublicKey import PKCS1_OAEP
#binary to hexidecimal 
from binascii import hexlify


def RSA_Key():
 # new Rsa key 
 # GEnerating a RSA key pair 
 key = RSA.generate(1024)
 # Lets set the key to private key 
 private_key  = key 
 #Drive the public key from the private key 
 public_key  = key.public_key()
 
 
 
 
 
 
 






def Get_data():
    return 0 




 #ENCRYPTION
def RSA_ENC():
    return 0
 





































