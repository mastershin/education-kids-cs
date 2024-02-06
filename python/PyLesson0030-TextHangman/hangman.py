import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'developer', 'algorithm']

# Select a random word from the list
word = random.choice(words)
guessed_letters = set()
wrong_letters = set()
attempts = 6  # Number of allowed wrong attempts

# Display the current state of the word
def display_word():
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Main game loop
while True:
    print(display_word())
    
    # Check if the game is won
    if set(word) == guessed_letters:
        print("Congratulations, you won!")
        break

    # Getting user input
    guess = input("Please guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in word:
        guessed_letters.add(guess)
        print("Good guess!")
    else:
        wrong_letters.add(guess)
        attempts -= 1
        print("Oops! Wrong guess. You have {} attempts left.".format(attempts))

    # Check if the game is lost
    if attempts == 0:
        print("Sorry, you lost! The word was: " + word)
        break