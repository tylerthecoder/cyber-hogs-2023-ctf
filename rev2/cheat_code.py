from readchar import readkey, key
from Crypto.Cipher import AES

def generate_sbox():
    sbox = [0] * 256
    for i in range(256):
        sbox[i] = (i * 7 + 13) & 0xff
    
    return sbox

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

    # Makes a single number with all the bits in it
    for i in range(input_len):
        value <<= 7
        value ^= input[i]

    
    hash = []
    for i in range(10):
        hash.append(SBOX[((value & 0xff) + i * 66) & 0xff])
        value >>= 8
    
    for i in range(len(hash) - 1, -1, -1):
        hash[i] ^= hash[(i + 1) % len(hash)]
    
    return bytes(hash).hex()

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
