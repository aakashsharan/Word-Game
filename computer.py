from play import *

class Computer:
    
    def __init__(self):
        self.game = Game()
    
    
    def comp_choose_word(self, hand, wordList, n):
        """
        Given a hand and a wordList, find the word that gives
        the maximum value score, and return it.
    
        This word should be calculated by considering all the words
        in the wordList.
    
        If no words in the wordList can be made from the hand, return None.
    
        hand: dictionary (string -> int)
        wordList: list (string)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
    
        returns: string or None
        """
        # return the best word you found.
        max_score_initial = 0
        best_score_word = None
        for word in wordList:
            if self.game.is_valid_word(word, hand, wordList):
                this_score = self.game.get_word_score(word, n)
                if this_score >= max_score_initial:
                    max_score_initial = this_score
                    best_score_word = word
        return best_score_word


    def comp_play_hand(self, hand, wordList, n):
        """
        Allows the computer to play the given hand, following the same procedure
        as playHand, except instead of the user choosing a word, the computer
        chooses it.
    
        1) The hand is displayed.
        2) The computer chooses a word.
        3) After every valid word: the word and the score for that word is
        displayed, the remaining letters in the hand are displayed, and the
        computer chooses another word.
        4)  The sum of the word scores is displayed when the hand finishes.
        5)  The hand finishes when the computer has exhausted its possible
        choices (i.e. compChooseWord returns None).
    
        hand: dictionary (string -> int)
        wordList: list (string)
        n: integer (GAME_HAND_SIZE; i.e., hand size required for additional points)
        """
        should_break = False
        total_points = 0
        while self.game.calculate_hand_len(hand) > 0:
            print "Current hand: ",
            self.game.display_hand(hand)
            comp_input = self.comp_choose_word(hand, wordList, n)
            if comp_input == None:
                should_break = True
                break
            else:
                if not self.game.is_valid_word(comp_input, hand, wordList):
                    print "Invalid word, please try again."
                else:
                    score = self.game.get_word_score(comp_input, n)
                    total_points += score
                    print '"' +str(comp_input) + '"' + " earned " + str(score) + " points. " + "Total: " + str(total_points) + " points."
                    hand = self.game.update_hand(hand, comp_input)
                    should_break = True
        if should_break:
            print "Total score: " + str(total_points) + " points."
