from game import *

class Play:
    
    def __init__(self):
        self.game = Game()
    
    def play_hand(self, hand, wordList, n):
        """
        Allows the user to play the given hand, as follows:
    
        * The hand is displayed.
        * The user may input a word or a single period (the string ".")
          to indicate they're done playing
        * Invalid words are rejected, and a message is displayed asking
          the user to choose another word until they enter a valid word or "."
        * When a valid word is entered, it uses up letters from the hand.
        * After every valid word: the score for that word is displayed,
          the remaining letters in the hand are displayed, and the user
          is asked to input another word.
        * The sum of the word scores is displayed when the hand finishes.
        * The hand finishes when there are no more unused letters or the user
          inputs a "."
    
          hand: dictionary (string -> int)
          wordList: list of lowercase strings
          n: integer (HAND_SIZE; i.e., hand size required for additional points)
        """
        should_break = False
        total_points = 0
        while self.game.calculate_hand_len(hand) > 0:
            print "Current hand: ",
            self.game.display_hand(hand)
            user_input = raw_input("Enter word, or a '.'' to indicate that you are finished:")
            if user_input == ".":
                print "Goodbye! Total score: " + str(total_points) +  " points."
                break
            else:
                if not self.game.is_valid_word(user_input, hand, wordList):
                    print "Invalid word, please try again."
                else:
                    score = self.game.get_word_score(user_input, n)
                    total_points += score
                    print str(user_input) + " earned " + str(score) + " points. " + "Total: " + str(total_points) + " points."
                    hand = self.game.update_hand(hand, user_input)
                    should_break = True
        if should_break:
            print "Run out of letters. Total score: " + str(total_points) + " points."


    def play_game(self, wordList):
        """
        Allow the user to play an arbitrary number of hands.
    
        1) Asks the user to input 'n' or 'r' or 'e'.
          * If the user inputs 'n', let the user play a new (random) hand.
          * If the user inputs 'r', let the user play the last hand again.
          * If the user inputs 'e', exit the game.
          * If the user inputs anything else, tell them their input was invalid.
    
        2) When done playing the hand, repeat from step 1
        """
        called_hand = None
        user_input = ""
        while(True):
            user_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if user_input == "n":
                called_hand = self.game.deal_hand(GAME_HAND_SIZE)
                self.play_hand(called_hand, wordList,GAME_HAND_SIZE)
            elif user_input == "r":
                if called_hand == None:
                    print "You have not played a hand yet. Please play a new hand first!"
                else:
                    self.play_hand(called_hand, wordList, GAME_HAND_SIZE)
            elif user_input == "e":
                break;
            else:
                print "Invalid command."