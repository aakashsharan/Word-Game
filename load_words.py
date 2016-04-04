import random
import string

WORD_VOWELS = 'aeiou'
WORD_CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
GAME_HAND_SIZE = 7

#letter scores
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "C:\Users\Aakash\Documents\GitHub\mitx.6.00.1x\week_4\pset_4\words.txt"

class LoadWords:
    
    def __init__(self):
        self.word_list = WORDLIST_FILENAME
    
    def get_word_list(self):
        return self.word_list
    
    def load_words(self):
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        It reads the words from the file.
        """
        print "Loading word list from file..."
        # inFile: file
        inFile = open(self.word_list, 'r', 0)
        # wordList: list of strings
        wordList = []
        for line in inFile:
            wordList.append(line.strip().lower())
        print "  ", len(wordList), "words loaded."
        return wordList
    
    def get_frq_dict(self, sequence):
        """
        Returns a dictionary where the keys are elements of the sequence
        and the values are integer counts, for the number of times that
        an element is repeated in the sequence.
    
        sequence: string or list
        return: dictionary
        """
        # freqs: dictionary (element_type -> int)
        freq = {}
        for x in sequence:
            freq[x] = freq.get(x,0) + 1
        return freq