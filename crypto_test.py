import unittest
import crypto


class TestCryptoMethods(unittest.TestCase):
    def test_h2ba(self):
        base16= "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        self.assertEqual(type(crypto.h2ba(base16)), bytearray)

    def test_b2base64(self):
        base16 = crypto.h2ba("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(crypto.b2base64(base16), b64)

    def test_xor_samelength(self):
        bytes1 = crypto.h2ba("1c0111001f010100061a024b53535009181c")
        bytes2 = crypto.h2ba("686974207468652062756c6c277320657965")
        output = crypto.h2ba("746865206b696420646f6e277420706c6179")
        self.assertEqual(crypto.xor(bytes1, bytes2), output)

    def test_xor_different_length(self):
        bytes1 = crypto.h2ba("1c0111001f010100061a024b53535009181c")
        bytes2 = crypto.h2ba("01")
        output = crypto.h2ba("1d0010011e000001071b034a52525108191d")
        self.assertEqual(crypto.xor(bytes1, bytes2), output)

    def test_edit_distance(self):
        self.assertEqual(crypto.edit_distance(bytearray([1]), bytearray([2])), 2)
        self.assertEqual(crypto.edit_distance(bytearray("this is a test".encode()), bytearray("wokka wokka!!!".encode())), 37)


if __name__ == '__main__':
    unittest.main()

