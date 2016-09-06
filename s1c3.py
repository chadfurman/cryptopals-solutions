import crypto
import sys
import string
import base64
import binascii

in_string = sys.argv[1]
for byte in range(0,255):
    xor_result = str(crypto.xor(in_string.encode(), base64.b16encode(bytes([byte]))), 'utf-8')
    print(str(xor_result))
    score = crypto.score_plaintext(xor_result)
    print(str(byte) + ':' + str(score))
    if score > 1:
        print(xor_result)

