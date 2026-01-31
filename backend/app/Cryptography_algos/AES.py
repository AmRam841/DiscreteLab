from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
import base64
import questionary
#from ..MainMenu.main import interactive_Menu


def get_path_questionary() -> str:
    # questionary.path provides path entry with completion
    selected_path = questionary.path("Select file:").ask()
    return selected_path  # None if cancelled
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




# Writing the name of the file into a var 
#Instead of directly using input this is a more gracefull way
def Write_file_name(prompt= "Name Of the Output File pls : "):
    File_name_Output = input(prompt).strip()
    return File_name_Output
    
    
        
def main():
    choice = input("enter 'e' for encryption or 'd ' for decryption: ").strip().lower()
    password = get_pass()
    if choice == 'e' :
        
        input_file1 = get_path_questionary()
        output_file1 = Write_file_name()
        encryption(input_file1 , output_file1 , password)
        print(f"File {input_file1} has been encrypted to {output_file1}")
      # Bug: os.remove("Test.txt")
    elif choice =='d' :
        
        #orginal idea was to wrap it in str() so it alwaysreturns a string , but this is bad practice , what if it returns None ? then the output would be a file name "None" 
        #instead we fo this  : 1- check if string 2- check if none 
        # and for the output if the user clicks a defualt name should be given  
        input_file1 = get_path_questionary()
        if not input_file1:
            print("No input Detected")
        output_file1 = Write_file_name()
        if not output_file1:
            output_file1
            if choice == 'e':
                output_file1 = input_file1 + ".enc"
            else:
                output_file1 = input_file1 + ".dec"
            
        
        decryption(input_file1 , output_file1 , password)
        print(f"File{input_file1} has beend decrypted to {output_file1 }")
        
        

    else:
        print("invalid try again !!")
        SystemExit(1)
    
    
if __name__ == "__main__" :
    main()