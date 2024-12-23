def xor_strings(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def main():
    # Encoded string from the comparison in the C code
    encoded = "cvaatd}v`Sjyv_npbsiqheXsqosUg|"

    # Pattern strings for XOR
    pattern1 = "chickens"
    pattern2 = "fried"

    # Extend the patterns to match the length of the encoded string
    extended_pattern1 = (pattern1 * (len(encoded) // len(pattern1) + 1))[:len(encoded)]
    extended_pattern2 = (pattern2 * (len(encoded) // len(pattern2) + 1))[:len(encoded)]

    # Reverse the XOR operations
    first_xor = xor_strings(encoded, extended_pattern1)
    original_flag = xor_strings(first_xor, extended_pattern2)

    return original_flag

# Execute the main function and print the flag
if __name__ == "__main__":
    flag = main()
    print(f"Recovered flag: {flag}")

