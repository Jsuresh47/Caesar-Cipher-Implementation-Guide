from encryptor import encrypt

def decrypt(text, key):
    return encrypt(text, -key)
