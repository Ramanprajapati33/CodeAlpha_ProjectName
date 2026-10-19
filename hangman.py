import random

WORDS = ["python", "computer", "developer", "keyboard", "program"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=== Hangman Game ===")
    print(f"Guess the hidden word. You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_word = " ".join(
            letter if letter in guessed_letters else "_" for letter in word
        )
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"You win! The word was '{word}'.")
                return
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.")

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
