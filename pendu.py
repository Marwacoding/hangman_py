#coding=utf-8

###### Import module
import random 
import logging

######


##### Logging messages
logging.basicConfig(filename = "info_pendu.log", level= logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')
logging.info('This an info message')
logging.error('this action is an error')
#####



###### Reading file

logging.info('Reading file : start')
my_file = open("engmix.txt", "r") 
lines = my_file.readlines()
list_word = [elem.strip() for elem in lines]
logging.info('reading file : end')
my_file.close()


######

####### Variables

lives = 5

logging.info('Choosing random word : start')

chosen_word = list(random.choice(list_word))
#print(chosen_word)

logging.info('Choosing random word : end')


hidden_list=[]

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#######


###### Remplacing letter by "_"
def hidden_word(secretWord):

    logging.info('Remplacing letter by "_" : start')

    for i in secretWord:
        i = "_"
        hidden_list.append(i)
    print(hidden_list)
    logging.info('Remplacing letter by "_" : end')
    
    return hidden_list



###### asking to the user to guess a letter

def actual_game(secretWord, secret_list, game_step):

    lives_remaining = True
    
    logging.info('start of game')
    while lives_remaining:
        

        guess = raw_input("Choose a letter : ").lower()
        logging.info('user chose a letter')

        #checking if the user is only writing an input

        logging.info("forcing the user to write a letter")
        if guess.isdigit(): 
            print("You have to enter a letter")
            guess = raw_input("Choose a letter : ").lower()
        
            
        

        ### Creating blanks

        if guess in secret_list:
            print("You've already guessed %s" %guess)

        #### replacing the _ by the letter if the guess is correct
        logging.info('replacing the _ by the letter if the guess is correct : start')
        for i in range(len(secretWord)):
            letter = secretWord[i]
            if guess==letter:
                secret_list[i] = letter
        logging.info('replacing the _ by the letter if the guess is correct : end')

        
        #Will display the correct answer whithout the list format
        print(" ".join(secret_list))
        logging.info('transforming the list to a string')


        #If there's no more underscore and lives != 0, then user win
        logging.info('if user guess all the right letters, no more game step, he wins : end')

        if "_" not in secret_list:
            lives_remaining = False #remaining list, but end of game, the user win
            print("You win :) !")

        logging.info('if user guess all the right letters, no more game step, he wins : end')
        
        #### if guess not correct, removing a life
        logging.info('if statement : guess is not correct, game step - 1 : start')
        
        if guess not in secretWord:
            game_step -= 1 
            print(" %s is not in the word. You loose a life" %guess)
            print(game_step)
            print(HANGMANPICS[game_step])
        
        
        logging.info('if statement : guess is not correct, game step - 1 : end')
        logging.info('display the wrong letter')


        ### end of game if life == 0

        logging.info('if statement : if game_step = 0, ending game : start')
        
        if game_step == 0:
            lives_remaining = False
            print("you just lost :( ")

     
        #print(game_step)
        
        logging.info('if statement : if game_step = 0, ending game : end')    

underscore_list = hidden_word(chosen_word)          
actual_game(chosen_word, underscore_list, lives)