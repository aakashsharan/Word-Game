from play import LoadWords, Play

# this will play the game.

if __name__ == '__main__':
    load_word = LoadWords()
    # get the word list.
    word_list = load_word.load_words()
    play = Play()
    # human plays the game.
    play.play_game(word_list)