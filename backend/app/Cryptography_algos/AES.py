from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
import base64
import easygui
# for getting the password for en/decription 
def get_pass():
    password = input("give me the pass")
    return password

def encryption(intput_file,output_file,password):
    salt = get_random_bytes(16)
    key = PBKDF2(password.encode('utf-8'),salt,dkLen=32 , count = 1000000)
    iv  =os.urandom(16)
    cypher = AES.new(key , AES.MODE_CBC, iv)


    try:
        with open(intput_file,'rb') as inputFile , open(output_file,'wb') as outputFile:
            outputFile.write(salt)
            outputFile.write(iv)
            
            while True:
                chunk = inputFile.read(4096)
                if len(chunk) == 0:
                    break
                if len(chunk) < 4096:
                    chunk = pad(chunk , 16)
                cypher_text = cypher.encrypt(chunk)
                outputFile.write(cypher_text)
                
                
    except FileNotFoundError:
        print("err file not found ")
def decryption(input_file,output_file,password):
    try:
        #read the enc file and read the first 32byte : 16 for salt , 16 for the IV
        with open(input_file ,'rb') as inputFile:
            salt = inputFile.read(16)
            if len(salt) != 16:
                raise ValueError("Invalid file : salt is incomplete or missing ")
            iv = inputFile.read(16)
            if len(iv) != 16:
                raise ValueError("iv incomplete")
            #Drive the 32 byte AES using PBKDF2 with the password and salt
            key = PBKDF2(password.encode('utf-8') , salt , dkLen=32 , count = 1000000)
            #initilize a AES chipher in cbc mode with the key and iv 
            AESchiper = AES.new(key , AES.MODE_CBC , iv)
            #Read the remaining data in chunks
            with open(output_file , 'wb') as output_file:
              while True:
                chunk = inputFile.read(4096)
                #end of the file    
                if len(chunk) ==  0 :
                       break
                #decrypt the chunk of file 
                decrypted_chunk = AESchiper.decrypt(chunk)
                #decrypt each chunk removing PKC7 padding from the final chunk
                if inputFile.tell() == os.path.getsize(input_file):
                    decrypted_chunk = unpad(decrypted_chunk,16)
                    
                output_file.write(decrypted_chunk)
                        
                        
    except FileNotFoundError:
        print("File not found ! ")
    except ValueError as e :
         print(f"Decryption err {e}")
         raise SystemExit(1)
     
def main():
    choice = input("enter 'e' for encryption or 'd ' for decryption: ").lower()
    password = get_pass()
    if choice == 'e' :
        
        input_file1 = "amir.bin"
        output_file1 = "isAmirkoni.txt"
        encryption(input_file1 , output_file1 , password)
        print(f"File {input_file1} has been encrypted to {output_file1}")
      # Bug: os.remove("Test.txt")
    elif choice =='d' : 
        input_file1 = easygui.fileopenbox()
        output_file1 = "theTest.text"
        decryption(input_file1 , output_file1 , password)
        print(f"File{input_file1} has beend decrypted to {output_file1 }")
        #no need for deleting this / if yo9-قفu wanted to have new key i have to make another function that gets decrypt the file and encrypt it with a diffrent key
        #this probably happens when changing master password
    else:
        print("invalid try again !!")
        SystemExit(1)
    
    
    
if __name__ == "__main__" :
    main()