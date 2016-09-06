from base64 import b64encode,b16decode,b16encode
import binascii
import struct
from wordscore import PlaintextScore

def base16_to_base64(base16_string):
    return b64encode(b16decode(base16_string, True))

def xor(bytes1raw, bytes2raw):
    bytes1 = memoryview(bytes1raw)
    bytes2 = memoryview(bytes2raw)
    result = []
    for index in range(0,len(bytes1)):
        byte1 = bytes1[index]
        byte2 = bytes2[0]
        xor_byte = byte1^byte2
        result.append(xor_byte)
    return bytes(result)

def score_plaintext(text):
    text_scorer = PlaintextScore()
    return text_scorer.score(text)
