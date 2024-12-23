from Crypto.Cipher import AES
import itertools
import string

def generate_sbox():
    sbox = [0] * 256
    for i in range(256):
        sbox[i] = (i * 7 + 13) & 0xff
    
    return sbox

ORDER = 66
SBOX = generate_sbox()

def decrypt_flag(key):
    encrypted = bytearray.fromhex("2655784d8bd73cd46f068ae7e2f9a5b26d7f92de54e4f3173a0892a8e90dde6c")
    iv = bytearray.fromhex("02f4d961ae10bca86a022dce226388ec")
    key = "".join(key).encode() + b"======"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted).decode()
    decrypted = decrypted[:-ord(decrypted[len(decrypted)-1:])]
    return decrypted

def run_hash(input):
    input = bytearray("".join(input).encode())
    input_len = len(input)
    value = 0
    for i in range(input_len):
        value <<= 7
        value ^= input[i]
    
    hash = []
    for i in range(10):
        hash.append(SBOX[((value & 0xff) + i * ORDER) & 0xff])
        value >>= 8
    
    for i in range(len(hash) - 1, -1, -1):
        hash[i] ^= hash[(i + 1) % len(hash)]
    
    return bytes(hash).hex()

def reset_input():
    global input, input_pos
    input = [" "] * 10
    input_pos = 0


# Provided functions (generate_sbox, decrypt_flag, run_hash)
# Assume these functions are defined as in your original code snippet

# Brute force attack
def brute_force_attack():
    characters = string.ascii_letters + string.digits  # Alphanumeric characters
    for item in itertools.product(characters, repeat=10):  # Iterating through all combinations of 10 characters
        attempt = ''.join(item)
        hash_result = run_hash(attempt)
        print(f"Attempt: {attempt}, Hash: {hash_result}")
        if hash_result == "b8c162bb09db49834032":
            return attempt
    return None

# def main():
#     found_key = brute_force_attack()
#     if found_key:
#         print(f"Found Key: {found_key}")
#         decrypted_flag = decrypt_flag(found_key)
#         print(f"Decrypted Flag: {decrypted_flag}")
#     else:
#         print("Valid key not found.")
#
# if __name__ == "__main__":
#     main()
#  "b8c162bb09db49834032"


def generate_sbox():
    sbox = [0] * 256
    for i in range(256):
        sbox[i] = (i * 7 + 13) & 0xff
    return sbox

def reverse_sbox_fn(sbox):
    reversed_sbox = [0] * 256
    for i in range(256):
        reversed_sbox[sbox[i]] = i
    return reversed_sbox


def reverse_hash(hash_hex, sbox):
    hash_bytes = bytearray.fromhex(hash_hex)
    reverse_sbox = reverse_sbox_fn(sbox)

    # Reverse the final XOR loop
    for i in range(len(hash_bytes) - 1, 0, -1):
        hash_bytes[i] ^= hash_bytes[i - 1]

    # Reverse the SBOX and addition
    value = 0
    for i, b in enumerate(reversed(hash_bytes)):
        sbox_value = reverse_sbox[b]
        sbox_original = (sbox_value - i * 66) & 0xff
        value |= sbox_original << (8 * i)

    return value

SBOX = generate_sbox()
hash_hex = "b8c162bb09db49834032"
reversed_value = reverse_hash(hash_hex, SBOX)

print(f"Reversed value (in hex): {hex(reversed_value)}")
