import random
import time

print("\nWelcome to Hangman game!")
player_name = input("Enter your name: ")
print("Hello " + player_name + "! Good luck!")
time.sleep(1)
print("The game is about to start!\nLet`s play Hangman!")
time.sleep(1)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global final_word
    words_to_guess = ["january","border", "trainee", "image","film","promises","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    final_word = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''

def play_loop():
    global play_game
    play_game = input("How about another game? y=yes, n=no\n")
    while play_game not in ['y', 'n', 'Y', 'N']:
        play_game = input("How about another game? y=yes, n=no\n")
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print("Thanks for playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the word: " + display + "\nEnter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print("Invalid input, enter a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        occurences = word.count(guess)
        while occurences > 0:
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            occurences -= 1
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        already_guessed.extend([guess])
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  " _|_\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  " _|_\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  " _|_\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     \n"
                  "  |     \n"
                  " _|_\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  " _|_\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was: " + final_word + "\n")
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()
main()

hangman()

