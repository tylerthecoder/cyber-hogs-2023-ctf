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

def reverse_hash(hash_hex, sbox):
    hash_bytes = bytearray.fromhex(hash_hex)
    reversed_sbox = reverse_sbox(sbox)

    # Reconstruct the value variable
    value = 0
    for i, b in enumerate(reversed(hash_bytes)):
        # Reverse the SBOX transformation
        sbox_original = reversed_sbox[b]
        # Undo the addition and mask operation
        value_intermediate = (sbox_original - i * 66) & 0xff
        # Reconstruct the value by applying the shifts in reverse
        value |= value_intermediate << (8 * i)

    return value

SBOX = generate_sbox()
hash_hex = "79a3d9b2d292cac3724b"
reversed_value = reverse_hash(hash_hex, SBOX)

print(f"Reversed value (in hex): {hex(reversed_value)}")

