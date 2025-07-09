def save_to_file(text, filename="output.txt"):
    with open(filename, "w") as f:
        f.write(text)
    print(f"\nEncrypted text saved to: {filename}")
