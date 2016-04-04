from choose_play import LoadWords, ChoosePlay

if __name__ == '__main__':
    load_word = LoadWords()
    # loads the word list.
    word_list = load_word.load_words()
    choose_play = ChoosePlay()
    # human/computer plays the game.
    choose_play.play_game(word_list)