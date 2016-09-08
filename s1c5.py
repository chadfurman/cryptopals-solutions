import crypto
import binascii
import base64

in_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

xor_result = crypto.xor(bytearray(in_string.encode()), bytearray(key.encode()))
print(base64.b16encode(xor_result))
