def six_bits_to_base64(six_bits):
    if (not six_bits):
        return '='
    six_bits = six_bits.ljust(6,'0')
    return {
            '000000': 'A',
            '000001': 'B',
            '000010': 'C',
            '000011': 'D',
            '000100': 'E',
            '000101': 'F',
            '000110': 'G',
            '000111': 'H',
            '001000': 'I',
            '001001': 'J',
            '001010': 'K',
            '001011': 'L',
            '001100': 'M',
            '001101': 'N',
            '001110': 'O',
            '001111': 'P',
            '010000': 'Q',
            '010001': 'R',
            '010010': 'S',
            '010011': 'T',
            '010100': 'U',
            '010101': 'V',
            '010110': 'W',
            '010111': 'X',
            '011000': 'Y',
            '011001': 'Z',
            '011010': 'a',
            '011011': 'b',
            '011100': 'c',
            '011101': 'd',
            '011110': 'e',
            '011111': 'f',
            '100000': 'g',
            '100001': 'h',
            '100010': 'i',
            '100011': 'j',
            '100100': 'k',
            '100101': 'l',
            '100110': 'm',
            '100111': 'n',
            '101000': 'o',
            '101001': 'p',
            '101010': 'q',
            '101011': 'r',
            '101100': 's',
            '101101': 't',
            '101110': 'u',
            '101111': 'v',
            '110000': 'w',
            '110001': 'x',
            '110010': 'y',
            '110011': 'z',
            '110100': '0',
            '110101': '1',
            '110110': '2',
            '110111': '3',
            '111000': '4',
            '111001': '5',
            '111010': '6',
            '111011': '7',
            '111100': '8',
            '111101': '9',
            '111110': '+',
            '111111': '/',
    }[six_bits]

def hex_char_to_four_bits(x):
    return {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'a': '1010',
            'b': '1011',
            'c': '1100',
            'd': '1101',
            'e': '1110',
            'f': '1111'
    }[x.lower()]

def four_bits_to_hex_char(x):
    return {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'a',
            '1011': 'b',
            '1100': 'c',
            '1101': 'd',
            '1110': 'e',
            '1111': 'f'
    }[x.rjust(4,'0')]

def hex_string_to_binary(hex_string):
    binary_string = ""
    for char in hex_string:
        binary_string += hex_char_to_four_bits(char)
    return binary_string

def binary_string_to_hex(binary_string):
    hex_string = ""
    while (binary_string):
        four_bits = binary_string[:4]
        binary_string = binary_string[4:]
        hex_string += four_bits_to_hex_char(four_bits)
    return hex_string

def three_bytes_to_base64(three_bytes):
    char1 = six_bits_to_base64(three_bytes[0:6])
    char2 = six_bits_to_base64(three_bytes[6:12])
    char3 = six_bits_to_base64(three_bytes[12:18])
    char4 = six_bits_to_base64(three_bytes[18:24])
    return char1+char2+char3+char4

def binary_string_to_base64(binary_string):
    base64 = ""
    while (binary_string):
        three_bytes = binary_string[:24]
        binary_string = binary_string[24:]
        base64 += three_bytes_to_base64(three_bytes)
    return base64

def hex_string_to_base64(hex_string):
    return binary_string_to_base64(hex_string_to_binary(hex_string))

def xor_binary_char(binary_char1, binary_char2):
    if (not binary_char1):
        return ''
    if (not binary_char2):
        return binary_char1
    if (binary_char1 == '0' and binary_char2 == '1'):
        return '1'
    if (binary_char1 == '1' and binary_char2 == '0'):
        return '1'
    return '0'

def xor_binary_strings(binary_str1, binary_str2):
    xor_result = ""
    while (binary_str1):
        xor_result += xor_binary_char(binary_str1[0:1], binary_str2[0:1])
        binary_str1 = binary_str1[1:]
        binary_str2 = binary_str2[1:]
    return xor_result

