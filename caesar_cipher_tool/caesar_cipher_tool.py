from input_module import get_input
from encryptor import encrypt
from decryptor import decrypt
from display import display_output
from file_writer import save_to_file

def main():
    mode, text, key = get_input()
    if mode == 'E':
        encrypted = encrypt(text, key)
        decrypted = decrypt(encrypted, key)
    elif mode == 'D':
        decrypted = decrypt(text, key)
        encrypted = encrypt(decrypted, key)
    else:
        print("Invalid mode selected.")
        return

    display_output(encrypted, decrypted)
    save_to_file(encrypted)

if __name__ == "__main__":
    main()
