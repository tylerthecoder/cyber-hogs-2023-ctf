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

    # Attempt to reverse the initial loop
    # This part is speculative and may not accurately retrieve the original input
    possible_inputs = []
    for i in range(10):
        possible_input_byte = (value >> (7 * (9 - i))) & 0xff
        possible_inputs.append(possible_input_byte)
        value ^= possible_input_byte << (7 * (9 - i))

    return possible_inputs

SBOX = generate_sbox()
hash_hex = "b8c162bb09db49834032"
possible_inputs = reverse_hash(hash_hex, SBOX)

print("Possible input bytes:", possible_inputs)
print("Possible input string:", ''.join(chr(byte) for byte in possible_inputs if 0 <= byte < 128))

