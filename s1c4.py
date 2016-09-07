import crypto
import binascii

infile = open("s1c4.txt")

for line in infile:
    line = line.strip()
    if len(line) != 60:
        continue
    for byte in range(0,256):
        xor_result = crypto.xor(bytearray(binascii.a2b_hex(line)), bytearray([byte]))
        score = crypto.score_plaintext(xor_result)
        if score > 1:
            print(line + " bytekey:" + str(byte) + " score:" + str(score))
            print(bytes(xor_result).decode())
