from base64 import b64encode,b16decode,b16encode
import binascii
import struct
import pdb
from wordscore import PlaintextScore

def h2ba(hexstring):
    '''
    Convert given hex string to bytearray

    Arguments:
    hexstring = string

    Returns:
    bytearray
    '''
    return bytearray(binascii.a2b_hex(hexstring))

def b2base64(barray):
    '''
    Take given bytearray and return it as a base64 string

    Arguments:
    barray = bytearray()

    Returns:
    string
    '''
    return b64encode(barray).decode()

def b2base16(barray):
    '''
    Take given bytearray and return it as a base16 string

    Arguments:
    barray = bytearray()

    Returns:
    string
    '''
    return b16encode(barray).decode()

def xor(barray1, barray2):
    '''
    Take bytearray1 and XOR it, byte by byte, with
    bytearray2.  If bytearray2 is shorter than
    bytearray, then repeat bytearray2 to the proper
    length.

    Arguments:
    barray1 = bytearray()
    barray2 = bytearray()

    Returns:
    byterray
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
    Given a bytestring, return the possibility that
    the string is actually plaintext.

    The more positive the score, the more likely
    that the bytestring is plaintext.  Likewise, the
    more negative the score, the less likely that
    the bytestring is plaintext.

    Arguments:
    text = bytes()

    Returns:
    int
    '''
    text_scorer = PlaintextScore()
    return text_scorer.score(text)
