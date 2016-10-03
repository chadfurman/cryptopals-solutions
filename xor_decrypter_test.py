import unittest
import crypto
from xor_decrypter import XorDecrypter

class TestXorDecrypter(unittest.TestCase):
    def test_get_blocks(self):
        bytes = crypto.h2ba("1c0111001f010100061a024b53535009181c")
        xor_decrypter = XorDecrypter(bytes, 2, 40)
        blocks = xor_decrypter.get_blocks(12)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(len(blocks[0]), 12)
        self.assertEqual(len(blocks[1]), 12)
        self.assertEqual(len(blocks[2]), 12)

        bytes2 = crypto.h2ba("1c0111001f010100061a024b5353500918")
        xor_decrypter2 = XorDecrypter(bytes2, 2, 40)
        blocks = xor_decrypter.get_blocks(12)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(len(blocks[0]), 12)
        self.assertEqual(len(blocks[1]), 12)
        self.assertEqual(len(blocks[2]), 10)

    def test_transpose_blocks(self):
        xor_decrypter = XorDecrypter(bytearray([0]), 2, 40) # we dont use the constructor params for this test
        input = [bytearray([1,2,3]),bytearray([4,5,6])]
        output = [bytearray([1,4]), bytearray([2,5]), bytearray([3,6])]
        self.assertEqual()

    def test_decrypt_repeating_xor(self):
        bytes1 = crypto.h2ba("1c0111001f010100061a024b53535009181c")
        xor_decrypter = XorDecrypter(bytes1, 1, 40) # we dont use the constructor params for this test
        output = crypto.h2ba("1d0010011e000001071b034a52525108191d")
        self.assertEqual(xor_decrypter.decrypt_repeating_xor(), output)

        original_plain_text = "1111111111111111"
        original_key = "2222"
        ciphertext = crypto.xor(crypto.h2ba("1111111111111111"),crypto.h2ba("2122"))
        xor_decrypter2 = XorDecrypter(ciphertext, 1, 40) # we dont use the constructor params for this test
        self.assertEqual(xor_decrypter2.decrypt_repeating_xor(), original_plain_text)


    def test_guess_key_length(self):
        original_plain_text = "1111111111111111"
        original_key = "2222"

        ciphertext = crypto.xor(crypto.h2ba("1111111111111111"),crypto.h2ba("2122"))
        xor_decrypter = XorDecrypter(ciphertext, 2, 40) # we dont use the constructor params for this test
        output = 2
        self.assertEqual(xor_decrypter.guess_key_length(), output)

        ciphertext2 = crypto.xor(crypto.h2ba("1111111111111111"),crypto.h2ba("21222324"))
        xor_decrypter2 = XorDecrypter(ciphertext, 2, 40) # we dont use the constructor params for this test
        output = 4
        self.assertEqual(xor_decrypter.guess_key_length(), output)

    def test_get_single_byte_xor_histogram_score(self):
        block1 = crypto.xor(crypto.h2ba("Hello pretty city!"),crypto.h2ba("12"))
        block2 = crypto.xor(crypto.h2ba("Purple dogs are really neat, and I like them a bunch!"),crypto.h2ba("22"))
        block3 = crypto.xor(crypto.h2ba("Frogs jump really high sometimes and then fall like marshmallows onto big fluffy pillows."),crypto.h2ba("23"))
       blocks = [block1,block2,block3]
        get_single_byte_xor_histogram_scores(self, blocks)
