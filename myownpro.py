
#This program is written by Shinichi Takebe, and I will write a program for a word-guessing game.

#I will provide my design, implement, and test explanation here, instead of reflection.pdf.

"""
This code is a simple word-guessing game. 
The program reads words from a file  "words1.txt",
selects a random word, jumbles its letters, and then asks
the user to guess the original word from the jumbled letters.
The user has 5 chances to guess the correct word. 
The program keeps track of the number of games played,
games won, and the winning percentage.
"""

#I will import random module.
from random import randint

"""
This is the main game loop. It initializes the game, won, and option variables,
and runs the game as long as the user wants to continue (by entering 'Y'). 
In each of the loop, the program chooses a random word, jumbles it,
and asks the user to guess the correct word. It also keeps track of the number
of games played, games won, and the winning percentage.
"""
def main():
    game, won, option = 0, 0, "Y"
    while option == "Y":
        word, jumbled_word = chooseWord()
        print(word)
        if userPlay(word, jumbled_word):
            won += 1
        game += 1
        average = won / game
        print(f"Rounds played: {game}, Rounds won: {won},winning percentage: {average * 100}%\n")
        option = input("Do you want to play again (Y/N): ")


"""
This function opens a file called "sample.txt" and reads all lines from it, 
storing them in the words list.
This function also chooses a random word from the words list, and then jumbles
its letters. It returns the original word and the jumbled word as a tuple.
"""
def chooseWord():
    fileobject = open("words1.txt", "r")
    words = fileobject.readlines()
    index=randint(0,len(words)-1)
    word=words[index].strip()
    original_word = word
    jumbled_word = ""
    while word:
        random_index=randint(0,len(word)-1)
        char = word[random_index]
        jumbled_word+=char
        word=word[:random_index]+word[random_index+1:]
    return original_word, jumbled_word
"""
This function prints the jumbled word and asks the user to guess
the original word. The user has 5 chances to guess the correct
word. If the user guesses correctly, the function returns True
; otherwise, it returns False.
"""
def userPlay(word,jumbled_word):
    print("Guess the  word from the jumbled letters: "+jumbled_word)
    for i in range(5, 0, -1):
        print(f"Enter your guess and press a button. You have {i} chances.")
        guess = input("make a guess: ").strip()
        if guess==word:
            print("You guessed the correct word.")
            return True
        else:
            print("Try again.")
    return False

if __name__ == "__main__":
    main()
