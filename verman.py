def str_to_bin(s):
    return ''.join(format(ord(c), '08b') for c in s)

def bin_to_str(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))

def vernam_encrypt(plaintext, key):
    bin_plaintext = str_to_bin(plaintext)
    bin_key = str_to_bin(key)
    
    # XOR the binary strings
    bin_ciphertext = ''.join(str(int(bin_plaintext[i]) ^ int(bin_key[i])) for i in range(len(bin_plaintext)))
    
    # Convert binary ciphertext back to string
    ciphertext = bin_to_str(bin_ciphertext)
    return ciphertext

def vernam_decrypt(ciphertext, key):
    return vernam_encrypt(ciphertext, key)  # Decryption is same as encryption

# Example usage
plaintext = "HELLO"
key = "XMCKL"  # The key must be the same length as the plaintext

ciphertext = vernam_encrypt(plaintext, key)
decrypted_text = vernam_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
