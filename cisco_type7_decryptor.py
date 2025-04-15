# Cisco Type 7 password decryption script with user input
def decrypt_type7(encoded):
    xlat = [
        0x64, 0x73, 0x66, 0x64, 0x3B, 0x6B, 0x66, 0x6F,
        0x41, 0x2C, 0x2E, 0x69, 0x79, 0x65, 0x77, 0x72,
        0x6B, 0x6C, 0x64, 0x4A, 0x4B, 0x44, 0x48, 0x53,
        0x55, 0x42
    ]

    result = ''
    index = int(encoded[:2])
    encoded = encoded[2:]

    for i in range(0, len(encoded), 2):
        b = int(encoded[i:i+2], 16)
        result += chr(b ^ xlat[index])
        index += 1

    return result

# Ask user for input
encoded_password = input("Enter Cisco Type 7 encoded password: ")
decoded_password = decrypt_type7(encoded_password)
print(f"🔓 Decrypted Password: {decoded_password}")
