from base64 import b64encode,b16decode,b16encode
import binascii
from wordscore import PlaintextScore

def h2ba(hexstring):
    '''
    Convert given hex string to bytearray

    ;param hexstring: string
    ;return: bytearray
    '''
    return bytearray(binascii.a2b_hex(hexstring))

def b2base64(barray):
    '''
    Take given bytearray and return it as a base64 string

    ;param barray: bytearray
    ;return: string
    '''
    return b64encode(barray).decode()

def b2base16(barray):
    '''
    Take given bytearray and return it as a base16 string

    ;param barray: bytearray
    ;return: string
    '''
    return b16encode(barray).decode()

def xor(barray1, barray2):
    '''
    Take bytearray1 and XOR it, byte by byte, with
    bytearray2.  If bytearray2 is shorter than
    bytearray, then repeat bytearray2 to the proper
    length.

    ;param barray1: bytearray
    ;param barray2: bytearray
    ;return: byterray
    '''

    result = []
    b1len = len(barray1)
    b2len = len(barray2)
    for index in range(0,b1len):
        byte1 = barray1[index]
        byte2 = barray2[index % b2len]
        xor_byte = byte1^byte2
        result.append(xor_byte)
    return bytearray(result)

def score_plaintext(text):
    '''
    Given a bytearray, return the possibility that
    the string is actually plaintext.

    The more positive the score, the more likely
    that the bytearray is plaintext.  Likewise, the
    more negative the score, the less likely that
    the bytearray is plaintext.

    ;param text: bytearray
    ;return int
    '''
    text_scorer = PlaintextScore(text)
    return text_scorer.score()

def histogram_score_plaintext(text):
    '''
    Given a bytearray, calculate the distance from our base histogram

    ;param text: bytearray
    ;return: int
    '''
    text_scorer = PlaintextScore(text)
    return text_scorer.histogram_score(text_scorer.get_histogram())

def edit_distance(a, b):
    '''
    Given two byte arrays, find the number of differing bits

    :param a: bytearray
    :param b: bytearray
    :return: int
    '''
    distance = 0
    for i in range(0,len(a)):
        for mask in [1, 2, 4, 8, 16, 32, 64, 128]:
            a_bit = a[i] & mask
            b_bit = b[i] & mask
            if (a_bit ^ b_bit): distance += 1
    return distance
