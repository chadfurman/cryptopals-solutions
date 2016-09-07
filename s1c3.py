import crypto
import sys
import binascii

in_string = sys.argv[1]
for byte in range(0,256):
    xor_result = crypto.xor(bytearray(binascii.a2b_hex(in_string)), bytearray([byte]))
    score = crypto.score_plaintext(xor_result)
    if score > 1:
        print(in_string + " bytekey:" + str(byte) + " score:" + str(score))
        print(bytes(xor_result).decode())

