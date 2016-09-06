import string

class PlaintextScore:
    """ a utility class for scoring plaintext"""
    simple_words = ["the", "and", "a", "is", "that", "this", "are", "he", "she", "it"]
    punctuation_marks = [".",",","\"","'","!","?"]

    def __init__(self):
        self.plaintext_score = 0
        self.has_space = False
        self.has_punctuation = False
        self.has_numbers = False
        self.current_word_has_vowel = False
        self.words_without_vowels = 0
        self.words_with_vowels = 0
        self.longest_word_length = 0
        self.current_word_length = 0
        self.simple_word_count = 0
        self.non_printable_count = 0
        self.current_word = ""
        self.last_word = ""
        self.longest_word = ""
        self.words = []

    def simple_word_check(self, word):
        word = word.lower()
        if (word in self.simple_words):
            return True
        return False

    def char_is_printable(self, char):
        ordinal = ord(char)
        return ordinal >= 32 and ordinal <= 126

    def char_is_space(self, char):
        return ord(char) == 32

    def end_word(self):
        if self.simple_word_check(self.current_word):
            self.simple_word_count += 1
        if self.current_word_length > self.longest_word_length:
            self.longest_word_length = self.current_word_length
            self.longest_word = self.current_word
        if not self.current_word_has_vowel:
            self.words_without_vowels += 1
        else:
            self.words_with_vowels += 1
        self.words.append(self.current_word)
        self.last_word = self.current_word
        self.current_word = ""
        self.current_word_length = 0

    def add_word_char(self, char):
        self.current_word += char
        self.current_word_length += 1
        if (char in "aeiou"):
            self.current_word_has_vowel = True

    def parse(self, plaintext):
        self.plaintext = plaintext
        for char in plaintext:
            # First, check characters that signify end of word
            if (not type(char) == str):
                self.non_printable_count += 1 # non-string chars might as well be non-printables at this point, digits are still string chars!
                continue

            if (not char in string.printable):
                self.non_printable_count += 1
                continue

            if (char in string.whitespace):
                self.has_space = True
                self.end_word()

            if (char in string.punctuation):
                self.has_punctuation = True
                self.end_word()

            if (char in string.digits):
                self.has_numbers = True
                self.end_word()

            if (char not in string.ascii_letters):
                self.end_word() # for good measure, any non-ascii characters end a word

            self.add_word_char(char)

        self.end_word()

    def calculate(self):
        self.plaintext_score = 0
        if self.has_numbers:
            self.plaintext_score += 1
        if self.has_punctuation:
            self.plaintext_score += 1
        if self.simple_word_count:
            self.plaintext_score += 10 * self.simple_word_count
        if self.words_with_vowels:
            self.plaintext_score += 5 * self.words_with_vowels
        if self.words_without_vowels:
            self.plaintext_score -= 5 * self.words_without_vowels
        if self.non_printable_count:
            self.plaintext_score -= 10 * self.non_printable_count


    def score(self, plaintext):
        self.parse(plaintext)
        self.calculate()
        return self.plaintext_score

