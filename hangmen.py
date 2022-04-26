import random

hangman1 = [
"""
+---+
    |
    |
    |
    ===""","""
+---+
  | |
  0 |
    |
    ===""","""
+---+
  | |
  0 |
 /| |
    ===""","""
+---+
  | |
  0 |
 /| |
    ===""","""
+---+
  | |
  0 |
 /|\|
    ===""","""
+---+
  | |
  0 |
 /|\|
  |  ===
 /      ""","""
 +---+
  | |
  0 |
 /|\|
  |  ===
 / \    ""","""
 """
]

animals = ["hond", "gans", "paard", "koe", "varken", "schaap", "kip", "ezel", "geit"]

word = random.choice(animals).lower()
print(word)
guessed_correctly = []
guessed_incorrectly = []
tries = 7
hangman_count = -1
while tries > 0:
    output = ''
    for letter in word:
        print(letter)
        if letter in guessed_correctly:
            output += letter
        else: 
            output += "_ "

    if output == word:
        break

    print("Guess the word barn farm animals: ",output)
    print(tries," chances left")
    guess = input("geef een letter: ").lower()
    print(guess)
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in word:
        print("Awesome jop! you guessed a correct letter!")
        guessed_correctly.append(guess)
    else:
        print("sorry! you have quessed a wrong letter!")
        print(hangman_count)
        hangman_count = hangman_count + 1
        print(hangman_count)
        tries = tries-1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

if tries > 0:
    print("you guessed the word and you win")
else:
    print("sorry you guessed the wrong word")
