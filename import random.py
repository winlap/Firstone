import random
import string

def hangman():
    words = ["php", "java", "get", "python", "string"]
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # display the partially guessed word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ''.join(word_list))

        # display the letters the user has already guessed
        print("Used letters: ", ' '.join(used_letters))

        # get user input
        user_letter = input("Guess a letter: ").upper()

        # check if input is valid
        if user_letter not in alphabet:
            print("Invalid input. Please try again.")
            continue

        # check if letter has already been guessed
        if user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")
            continue

        # check if letter is in the word
        if user_letter in word_letters:
            print("Good guess!")
            word_letters.remove(user_letter)
        else:
            print("Oops! That letter is not in the word.")
            lives -= 1

        used_letters.add(user_letter)

    # game over
    if lives == 0:
        print("Sorry, you ran out of lives. The word was", word)
    else:
        print("Congratulations, you guessed the word", word, "with", lives, "lives remaining!")

# call the hangman function to start the game
hangman()
