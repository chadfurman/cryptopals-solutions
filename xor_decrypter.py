import "crypto"


class XorDecrypter:
    def __init__(self, ciphertext = "", min_key_guess = 1, max_key_guess = 40):
        '''
        Constructor for XorDecrypter.  Sets ciphertext for the instance, along with the minimum key length
        and maximum key length.

        :param ciphertext: bytearray
        :param min_key_guess: int
        :param max_key_guess: int
        '''
        try:
            min_key_guess = int(min_key_guess)
        except ValueError:
            min_key_guess = 1

        try:
            max_key_guess = int(max_key_guess)
        except ValueError:
            max_key_guess = 40

        if type(ciphertext) == str:
            ciphertext = bytearray(ciphertext.encode())

        if type(ciphertext) == bytes:
            ciphertext = bytearray(ciphertext)

        self.max_key_guess = max_key_guess if max_key_guess > min_key_guess else min_key_guess
        self.min_key_guess = min_key_guess if min_key_guess < max_key_guess else max_key_guess

        self.ciphertext = ciphertext

    def decrypt_repeating_xor(self):
        '''
        Operates on the ciphertext stored in the instance.  Returns the plaintext

        :return: bytearray
        '''

        # 1) get most likely key length via smallest edit distance
        key_length = self.guess_key_length()

        # 1a) Get all blocks of length key_length from the ciphertext
        blocks = self.get_blocks(key_length)

        # 2) transpose blocks
        transposed_blocks = self.transpose_blocks(blocks, key_length)

        # 3) find histograms of all single-character XORs on transposed blocks
        histogram_scores = self.get_single_byte_xor_histogram_scores(transposed_blocks)

        # 4) take the best scoring byte for each block and combine them to make the key
        key = bytearray()
        for block_index in histogram_scores.iterkeys():
            best_score = 9999999 # something really big so we can find the smallest
            for byte in histogram_scores.iterkeys():
                if histogram_scores[byte_index] < best_score:
                    best_score = histogram_scores[byte]
                    key[block_index] = byte

        # 5) return the plaintext
        return crypto.xor(self.ciphertext, key)

    def guess_key_length(self):
        '''
        Returns the key length between min_key_guess and max_key_guess that yields
        the smallest edit distance between block1 and block2

        :return: int
        '''
        smallest_edit_distance = max_key_guess * 8
        key_length = 0

        for key_length_guess in range(min_key_guess, max_key_guess + 1):
            blocks = self.get_blocks(key_length_guess)
            block1 = blocks[0]
            block2 = blocks[1]
            edit_distance = crypto.edit_distance(block1, block2)
            if (edit_distance > smallest_edit_distance): return
            smallest_edit_distance = edit_distance
            key_length = key_length_guess

        return key_length

    def get_single_byte_xor_histogram_scores(self, blocks):
        '''
        Given an array of blocks, calculate all single-byte XOR histogram scores.
        Return a 2-dimensional array of blocks and their byte scores

        :param blocks:
        :return: int scores[block][byte]
        '''
        histogram_scores = {}

        for block_index in blocks.iterkeys():
            histogram_scores[block_index] = {}
            for byte in range(0,256):
                block = blocks[block_index]
                xor_result = crypto.xor(block, bytearray([byte]))
                histogram_scores[block_index][byte] = crypto.histogram_score_plaintext(xor_result)
        return histogram_scores

    def get_blocks(self, key_length):
        '''
        Extract blocks of ciphertext with length key_length
        :param key_length: int
        :return: array(bytearray)
        '''
        blocks = []
        block_index = 0
        ciphertext = self.ciphertext
        while ciphertext:
            blocks[block_index] = ciphertext[:key_length]
            ciphertext = ciphertext[key_length:]
            block_index += 1
        return blocks

    def transpose_blocks(self, blocks):
        '''
        Takes in an array of bytearrays and returns their transposition

        :param blocks: array[bytearray]
        :return: array[bytearray]
        '''
        transposed_blocks = []
        # the first block should be one of the longest, use that for init
        for i in range(0, len(blocks[0])): 
            transposed_blocks.append(bytearray())
            
        for block_index in blocks.iterkeys():
            block = blocks[block_index]
            for char_index in block.iterkeys():
                # char_index = column , block_index = row
                if char_index not in transposed_blocks.keys():
                    transposed_blocks[char_index] = []
                if block_index not in transposed_blocks[char_index].keys():
                    transposed_blocks[char_index] = bytearray()
                transposed_blocks[char_index][block_index] = blocks[block_index][char_index]
        return transposed_blocks