def get_input():
    mode = input("Choose mode (E = Encrypt, D = Decrypt): ").strip().upper()
    text = input("Enter the text: ")
    key = int(input("Enter the shift key: "))
    return mode, text, key

