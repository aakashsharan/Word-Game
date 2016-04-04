from computer import *
from load_words import *

class ChoosePlay:
    
    def __init__(self):
        self.computer = Computer()
        self.play = Play()
        self.game = Game()
    
    def player_choice(self):
        user_message = "Enter u to have yourself play, c to have the computer play: "
        user_input = ""
        while(True):
            user_input = raw_input(user_message)
            if user_input=="u" or user_input=="c":
                break;
            else:
                print "Invalid command."
        return user_input

    def play_game(self, wordList):
        """
        Allow the user to play an arbitrary number of hands.
    
        1) Asks the user to input 'n' or 'r' or 'e'.
            * If the user inputs 'e', immediately exit the game.
            * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    
        2) Asks the user to input a 'u' or a 'c'.
            * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    
        3) Switch functionality based on the above choices:
            * If the user inputted 'n', play a new (random) hand.
            * Else, if the user inputted 'r', play the last hand again.
    
            * If the user inputted 'u', let the user play the game
              with the selected hand, using playHand.
            * If the user inputted 'c', let the computer play the
              game with the selected hand, using compPlayHand.
    
        4) After the computer or user has played the hand, repeat from step 1
    
        wordList: list (string)
        """
        called_hand = None
        while(True):
            game_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if game_input == "n":
                player = self.player_choice()
                called_hand = self.game.deal_hand(GAME_HAND_SIZE)
                assert player=="u" or player=="c"
                if player == "u":
                    self.play.play_hand(called_hand, wordList,GAME_HAND_SIZE)
                else:
                    self.computer.comp_play_hand(called_hand, wordList,GAME_HAND_SIZE)
    
            elif game_input == "r":
                if called_hand == None:
                    print "You have not played a hand yet. Please play a new hand first!"
                    continue
                else:
                    player = self.player_choice()
                    assert player=="u" or player=="c"
                    if player == "u":
                        self.play.play_hand(called_hand, wordList,GAME_HAND_SIZE)
                    else:
                        self.computer.comp_play_hand(called_hand, wordList,GAME_HAND_SIZE)
            elif game_input == "e":
                break;
            else:
                print "Invalid input."