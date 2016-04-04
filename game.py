from load_words import *

class Game:
    
    def get_word_score(self,word, n):
        """
        Returns the score for a word. Assumes the word is a valid word.
    
        The score for a word is the sum of the points for letters in the
        word, multiplied by the length of the word, PLUS 50 points if all n
        letters are used on the first turn.
    
        Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
        worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    
        word: string (lowercase letters)
        n: integer (GAME_HAND_SIZE; i.e., hand size required for additional points)
        returns: int >= 0
        """
        count_n = 0
        total_score = 0
        for char in word:
            if char in SCRABBLE_LETTER_VALUES:
                total_score += SCRABBLE_LETTER_VALUES[char]
                count_n += 1
        total_score = total_score*len(word)
        if n==count_n:
            total_score = total_score + 50
        return total_score
    
    def display_hand(self, hand):
        """
        Displays the letters currently in the hand.
    
        For example:
        >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
        Should print out something like:
           a x x l l l e
        The order of the letters is unimportant.
    
        hand: dictionary (string -> int)
        """
        for letter in hand.keys():
            for j in range(hand[letter]):
                 print letter,              # print all on the same line
        print                               # print an empty line
    
    def deal_hand(self, n):
        """
        Returns a random hand containing n lowercase letters.
        At least n/3 the letters in the hand should be VOWELS.
    
        Hands are represented as dictionaries. The keys are
        letters and the values are the number of times the
        particular letter is repeated in that hand.
    
        n: int >= 0
        returns: dictionary (string -> int)
        """
        hand={}
        numVowels = n / 3
    
        for i in range(numVowels):
            x = WORD_VOWELS[random.randrange(0,len(WORD_VOWELS))]
            hand[x] = hand.get(x, 0) + 1
    
        for i in range(numVowels, n):
            x = WORD_CONSONANTS[random.randrange(0,len(WORD_CONSONANTS))]
            hand[x] = hand.get(x, 0) + 1
    
        return hand
    
    def update_hand(self, hand, word):
        """
        Assumes that 'hand' has all the letters in word.
        In other words, this assumes that however many times
        a letter appears in 'word', 'hand' has at least as
        many of that letter in it.
    
        Updates the hand: uses up the letters in the given word
        and returns the new hand, without those letters in it.
    
        Has no side effects: does not modify hand.
    
        word: string
        hand: dictionary (string -> int)
        returns: dictionary (string -> int)
        """
        hand_copy = hand.copy()
        for char in word:
            if char in hand:
                hand_copy[char] -= 1
                if hand_copy[char] < 0:
                    hand_copy[char] = 0
        return hand_copy
    
    def is_valid_word(self, word, hand, wordList):
        """
        Returns True if word is in the wordList and is entirely
        composed of letters in the hand. Otherwise, returns False.
    
        Does not mutate hand or wordList.
    
        word: string
        hand: dictionary (string -> int)
        wordList: list of lowercase strings
        """
        is_valid = True
        hand_copy = hand.copy()
        if word in wordList:
            for char in word:
                if char in hand:
                    hand_copy[char] -= 1
                else:
                    is_valid = False
                    break
            for key in hand_copy:
                if hand_copy[key] < 0:
                    is_valid = False
                    break
        else:
            is_valid = False
        return is_valid
    
    def calculate_hand_len(self, hand):
        """
        Returns the length (number of letters) in the current hand.
    
        hand: dictionary (string-> int)
        returns: integer
        """
        length_hand = 0
        for key in hand:
            if hand[key] > 0:
                length_hand += hand[key]
        return length_hand