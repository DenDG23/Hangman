import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    
    return word.upper()

def lives_user_input() -> int:
    lives = input("Chose how many lives u want to have: ")
    try:
        lives = int(lives)
    except:
        print("You should enter number")
        return lives_user_input()
    return lives



def handman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    print("In this game you shoud guess the hidden word. You can choose how many lives you will have. Lives can be between 3 and 15.\n \
    Rules: you will pick one letter, if letter in word, you will see it in hidden word.\n \
    If letter isn't in word you will lose 1 live and can try again.")
    lives = lives_user_input()
    while lives > 15 or lives < 3:
        if lives > 15:
            print("You can have not more 15 lives")
            lives = lives_user_input()
        elif lives < 3:
            print("You can have not less 3 lives")
            lives = lives_user_input()

    
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} and you have used this letters : " , " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter isn't in the word.")


        elif user_letter in used_letters:
            print("You already used this character. Please try again")

        else:
            print("invalid character. Try again.")

    if lives == 0:
        print(f"You died. The word was: {word}")
    else:
        print(f"The word: {word}!\n Congrats!!!")


handman()