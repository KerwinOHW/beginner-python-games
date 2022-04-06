import random
import string

from words import wordlist

# todo 加入live值

def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(wordlist)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # print(word_letters)  # todo 调试用，待删

    # getting user input
    while len(word_letters) > 0:

        print(word_letters)
        # print(alphabet - word_letters)  # todo 待删
        # letters used
        print('You have used letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D) '-' means the letter that haven't guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    print(f'{word.title()} \nYay, you guessed the word, REJECT!!')

    # gets here when len(word_letters) == 0


hangman()
