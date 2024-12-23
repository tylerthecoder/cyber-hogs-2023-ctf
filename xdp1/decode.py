def xor_decrypt(encrypted_data, key):
    decrypted = ""
    for i in range(len(encrypted_data)):
        decrypted += chr(ord(encrypted_data[i]) ^ ord(key[i % len(key)]))
    return decrypted

# Replace 'encrypted_password_base64' with the actual Base64 encoded password from the registry
encrypted_password_base64 = "IQQZGgBUSlxAQkRC"  # Base64 encoded encrypted password
encrypted_password = encrypted_password_base64.decode('base64')  # Base64 decode
decrypted_password = xor_decrypt(encrypted_password, "securexor")
print(decrypted_password)
