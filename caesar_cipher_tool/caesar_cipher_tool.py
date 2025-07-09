from input_module import get_input
from encryptor import encrypt
from decryptor import decrypt
from display import display_output
from file_writer import save_to_file

def main():
    text, key = get_input()
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)
    display_output(encrypted, decrypted)
    save_to_file(encrypted)

if __name__ == "__main__":
    main()
