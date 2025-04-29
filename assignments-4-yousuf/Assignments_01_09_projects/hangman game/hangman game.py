# projact 8 : Hangman Game in Python


import random
words = ['enum', 'python', 'collab', 'vscode',  'games']
word = random.choice(words)

guessed = []
attempts = 6

print("welcome to Hangman Game projact 8")
print("_" * len(word))


while attempts > 0:
   guess = input("\n guess the letter: ").lower()

   if len(guess) != 1 or not guess.isalpha():
        print("write a one alphabet only")
        continue
   if guess in guessed:
        print("this letter is already guessed choose another letter")
        continue
   guessed.append(guess)

   if guess in word:
        print("correct guess")
   else:
        attempts -= 1
        print(f"wrong {attempts} attempts.")

   displayed_word = " ".join([letter if letter in guessed else "_" for letter in word])
   print(displayed_word)

   if "_" not in displayed_word:
        print(f"congratulations the correct word is: {word}")
        break
   else:
        print(f"game over! the correct word is: {word}")