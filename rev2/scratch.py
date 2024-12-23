from readchar import readkey, key
from Crypto.Cipher import AES
from typing import List

def generate_sbox():
    sbox = [0] * 256
    for i in range(256):
        sbox[i] = (i * 7 + 13) & 0xff
    
    return sbox

def reverse_sbox(sbox):
    reversed_sbox = [0] * 256
    for i in range(256):
        reversed_sbox[sbox[i]] = i
    return reversed_sbox

SBOX = generate_sbox()
RSBOX = reverse_sbox(SBOX)

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

    print("Stage 1: ", hex(value), "Should be 0xe22a0667890b5596f152")
    
    hash = []
    for i in range(10):
        sb = SBOX[((value & 0xff) + i * 66) & 0xff]
        hash.append(sb)
        value >>= 8

    print("Stage 2: ", bytes(hash).hex(), "Should be 79a3d9b2d292cac3724b")
    # hash = "79a3d9b2d292cac3724b"
    
    # XOR in a cycle
    for i in range(len(hash) - 1, -1, -1):
        hash[i] ^= hash[(i + 1) % len(hash)]

    print("Stage 3: ", bytes(hash).hex(), "Should be b8c162bb09db49834032")
    
    return bytes(hash).hex()


def stage1(inp: str) -> int:
    input = bytearray("".join(inp).encode())
    input_len = len(input)
    value = 0

    for i in range(input_len):
        value <<= 7
        value ^= input[i]

    return value


def stage2(value: int):
    hash = []
    for i in range(10):
        sb = SBOX[((value & 0xff) + i * 66) & 0xff]
        hash.append(sb)
        value >>= 8

    return bytes(hash).hex()

def stage3(hash): 
    # Copy hash
    hash = hash.copy()
    for i in range(len(hash) - 1, -1, -1):
        hash[i] ^= hash[(i + 1) % len(hash)]
    return bytes(hash).hex()

def reverse_stage_1(value):
    rev_str = ""
    while value > 0:
        # Extract last 7 bits of value
        bits = value & 0b1111111
        rev_str += chr(bits)
        value >>= 7
    return rev_str[::-1]

def reverse_hex_value(hex_value):
    reversed_value = 0
    while hex_value:
        # Shift reversed_value to make room for the next byte
        reversed_value <<= 8
        # Add the next byte from hex_value
        reversed_value |= hex_value & 0xff
        # Shift hex_value to remove the byte we just processed
        hex_value >>= 8
        print(hex(reversed_value), hex(hex_value))
    return reversed_value

def reverse_stage_2(hash_bytes: bytearray) -> int:
    # Reconstruct the value variable
    value = 0
    for i, b in enumerate(hash_bytes):
        # Reverse the SBOX transformation
        sbox_original = RSBOX[b]
        # Undo the addition and mask operation
        value_intermediate = (sbox_original - i * 66) & 0xff
        # Reconstruct the value by applying the shifts in reverse
        value |= value_intermediate << (8 * i)

    return value

def reverse_stage_2c(hash_array: bytearray):
    # Convert the input hexadecimal string to a bytearray

    # Initialize the original value
    original_value = 0

    # Iterate over each byte in the original order (from most significant to least significant)
    for i in range(len(hash_array)):
        # Reverse the SBOX substitution
        pre_sbox_value = RSBOX[hash_array[i]]

        # Adjust for the addition in the original function
        # We subtract the added value (i * 66) and then shift to the left to its original position
        original_byte = (pre_sbox_value - i * 66) & 0xff
        original_value |= original_byte << (8 * (len(hash_array) - 1 - i))

    return original_value


def reverse_stage_3(hash_hex):
    hash_bytes = bytearray.fromhex(hash_hex)

    # Iterate forward through the hash array
    for i in range(len(hash_bytes)):
        if i == len(hash_bytes) - 1:
            # The last element is XOR'ed with the first
            hash_bytes[i] ^= hash_bytes[0]
        else:
            # Each element is XOR'ed with the next
            hash_bytes[i] ^= hash_bytes[i + 1]

    return hash_bytes

deseried_val = "b8c162bb09db49834032"

rev_stage_3 = reverse_stage_3(deseried_val)
print ("Stage 3:", rev_stage_3.hex(), "|", stage3(rev_stage_3),  "=", deseried_val)

rev_stage_2 = reverse_stage_2(rev_stage_3)

print("Stage 2:", hex(rev_stage_2), "|", stage2(rev_stage_2), "=", rev_stage_3.hex())

rev_stage_1 = reverse_stage_1(rev_stage_2)

print("Stage 1: ", rev_stage_1, "|", hex(stage1(rev_stage_1)), "=", hex(rev_stage_2))

print("Test input: ", run_hash(rev_stage_1))


def main():
    print("Welcome to the cantina. Want to unlock new characters? Enter the unlock code.")
    reset_input()
    while True:
        update_input()

def reset_input():
    global input, input_pos
    input = [" "] * 10
    input_pos = 0

def update_input():
    global input, input_pos
    code_text = "".join([f" [{c}]" for c in input])
    print("Enter code:" + code_text, end='\r')

    k = readkey()
    if k == key.BACKSPACE and input_pos > 0:
        input_pos -= 1
        input[input_pos] = " "
    elif k == key.ENTER:
        if input_pos == len(input):
            hash_result = run_hash(input)
            if hash_result == "b8c162bb09db49834032":
                print(f"Flag unlocked! {decrypt_flag(input)}" + (" " * 15))
            else:
                print("That doesn't seem to be a valid code!" + (" " * 15))
        else:
            print("Not enough characters!" + (" " * 30))
        
        reset_input()
    elif input_pos < len(input):
        is_alphanum = (k >= "a" and k <= "z") or (k >= "A" and k <= "Z") or (k >= "0" and k <= "9")
        if is_alphanum:
            input[input_pos] = k
            input_pos += 1

if __name__ == "__main__":
    main()
