from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import questionary


def get_pass() -> str:
    return input("give me the pass: ").strip()

def encryption(input_file, output_file, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password.encode('utf-8'), salt, dkLen=32, count=1000000)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
        with open(input_file, 'rb') as inputFile, open(output_file, 'wb') as outputFile:
            # write salt + iv at start of file
            outputFile.write(salt)
            outputFile.write(iv)

            # Use a one-chunk buffer so we can detect the final chunk and pad only that
            prev_chunk = None
            while True:
                chunk = inputFile.read(4096)
                if not chunk:
                    # EOF reached: if there's a prev_chunk, pad & encrypt it as last block
                    if prev_chunk is not None:
                        last = pad(prev_chunk, AES.block_size)
                        outputFile.write(cipher.encrypt(last))
                    break

                if prev_chunk is not None:
                    # Encrypt previous (non-final) chunk directly
                    outputFile.write(cipher.encrypt(prev_chunk))
                prev_chunk = chunk

    except FileNotFoundError:
        print("Error: input file not found:", input_file)
    except Exception as e:
        print("Encryption error:", e)
        raise

def decryption(input_file, output_file, password):
    try:
        with open(input_file, 'rb') as inputFile:
            salt = inputFile.read(16)
            if len(salt) != 16:
                raise ValueError("Invalid file: salt is incomplete or missing")
            iv = inputFile.read(16)
            if len(iv) != 16:
                raise ValueError("Invalid file: iv is incomplete or missing")

            key = PBKDF2(password.encode('utf-8'), salt, dkLen=32, count=1000000)
            cipher = AES.new(key, AES.MODE_CBC, iv)

            with open(output_file, 'wb') as outFile:
                prev_chunk = None
                while True:
                    chunk = inputFile.read(4096)
                    if not chunk:
                        # EOF: decrypt and unpad the last chunk
                        if prev_chunk is not None:
                            decrypted = cipher.decrypt(prev_chunk)
                            decrypted = unpad(decrypted, AES.block_size)
                            outFile.write(decrypted)
                        break

                    if prev_chunk is not None:
                        # decrypt previous (non-final) chunk and write as-is (no unpad)
                        outFile.write(cipher.decrypt(prev_chunk))
                    prev_chunk = chunk

    except FileNotFoundError:
        print("File not found:", input_file)
    except ValueError as e:
        print(f"Decryption error: {e}")
        raise SystemExit(1)
    except Exception as e:
        print("Decryption unexpected error:", e)
        raise

def write_file_name(prompt="name Please : "):
    name = input(prompt).strip()
    return name

#for autocompltion on 
def get_path_questionary() -> str:
    # questionary.path provides path entry with completion
    selected_path = questionary.path("Select file:").ask()
    return selected_path  # None if cancelled

def main():
    choice = input("enter 'e' for encryption or 'd' for decryption: ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid mode. Use 'e' or 'd'.")
        return

    password = get_pass()
    if not password:
        print("No password provided.")
        return

    input_file = get_path_questionary()
    if not input_file:
        print("No input file selected.")
        return

    output_file = write_file_name()
    if not output_file:
        # provide a default output name if user presses enter
        if choice == 'e':
            output_file = input_file + ".enc"
        else:
            output_file = input_file + ".dec"

    if choice == 'e':
        encryption(input_file, output_file, password)
        print(f"File {input_file} has been encrypted to {output_file}")
    else:
        decryption(input_file, output_file, password)
        print(f"File {input_file} has been decrypted to {output_file}")

if __name__ == "__main__":
    main()