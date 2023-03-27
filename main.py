import random
import hangman_art
import hangman_words
from replit import clear


play_again = True

while play_again == True:
    word_list = hangman_words.word_list
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    clear()
    print(hangman_art.logo)
    end_of_game = False
    lives = 6
    
    
    
    #Create blanks
    display = []
    #List for previous guesses
    guessed = []
    
    for _ in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")
    
    while not end_of_game:
        print(f"Previous Guesses: {' '.join(guessed)}") 
        guess = input("Guess a letter: ").lower()
        clear()
    
        if guess not in guessed:
            guessed += guess
        else:
            print(hangman_art.stages[lives])        
            print(f"{' '.join(display)}")                 
            print("You have already guessed that, please try a different letter.")
    
            continue
            
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
            
    
        if guess not in chosen_word:
            clear()
            print(hangman_art.stages[lives])
            print(f"{guess} is not in the solution, you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                clear()
                print(hangman_art.stages[lives])
                print(f"You have run out of lives, the correct solution was {chosen_word}.\nGAME OVER.")
    
        print(f"{' '.join(display)}")
    
        if "_" not in display:
            end_of_game = True
            clear()
            print(f"You have guessed the correct solution {chosen_word}, congratulations!")
    
    prompt = input("Do you want to play again? Y/N\n").lower()
    if prompt == "y":
        play_again = True
    else:
        play_again = False