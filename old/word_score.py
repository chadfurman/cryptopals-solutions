import string

class PlaintextScore:
    """ a utility class for scoring plaintext"""
    simple_words = ["the", "and", "a", "is", "that", "this", "are", "he", "she", "it"]
    punctuation_marks = [".",",","\"","'","!","?"]

    def __init__(self):
        self.plaintext_score = 0
        self.has_space = false
        self.has_punctuation = false
        self.has_numbers = false
        self.current_word_has_vowel = false
        self.words_without_vowels = 0
        self.longest_word_length = 0
        self.current_word_length = 0
        self.simple_word_count = 0
        self.current_word = ""
        self.last_word = ""
        self.longest_word = ""
        self.words = []

    def simple_word_check(self, word):
        word = word.lower()
        if (word in simple_words):
            return true
        return false

    def char_is_printable(self, char):
        ordinal = ord(char)
        return ordinal >= 32 && ordinal <= 126

    def char_is_space(self, char):
        return ord(char) == 32

    def end_word(self):
        if simple_word_check(self.current_word):
            self.simple_word_count += 1
        if self.current_word_length > self.longest_word_length:
            self.longest_word_length = self.current_word_length
            self.longest_word = self.current_word
        if (!self.current_word_has_vowel):
            self.words_without_vowels += 1
        self.words.append(self.current_word)
        self.last_word = self.current_word
        self.current_word = ""
        self.current_word_length = 0

    def add_word_char(self, char):
        self.current_word += char
        self.current_word_length += 1
        if (char in "aeiou"):
            self.current_word_has_vowel = true

    def parse(self, plaintext):
        for char in plaintext:
            # First, check characters that signify end of word
            if (char not in string.printable):
                return -1 # possibly a binary string, but not english

            if (char in string.whitespace):
                self.has_space = true
                self.end_word()

            if (char in string.punctuation):
                self.has_punctuation = true
                self.end_word()

            if (char in string.digits):
                self.has_numbers = true
                self.end_word()

            if (char not in string.ascii_letters):
                self.end_word() # for good measure, any non-ascii characters end a word

            self.add_word_char(char)

        self.end_word()

    def calculate(self):
        """TODO: Check all class params and score this text"""

    def score(self, plaintext):
        self.parse(plaintext)
        self.calculate()
        return self.plaintext_score

