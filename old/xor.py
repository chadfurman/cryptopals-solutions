from custom_crypto import *
from sys import argv,exit

if len(argv) < 3:
    print("Usage: python3 xor.py hex_string hex_string")
    exit(1)

binary_str1 = hex_string_to_binary(argv[1])
binary_str2 = hex_string_to_binary(argv[2])

print(binary_string_to_hex(xor_binary_strings(binary_str1, binary_str2)))

