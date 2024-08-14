import random

def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "openai"]
    return random.choice(words)

def display_word(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

def hangman():
    word = get_random_word()
    guesses = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_word(word, guesses))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word:
            guesses.add(guess)
            print(f"Good guess: {display_word(word, guesses)}")
        else:
            guesses.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} tries left.")
            print(display_word(word, guesses))
        
        if all(letter in guesses for letter in word):
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
