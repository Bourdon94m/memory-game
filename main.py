import random 
import os
import time

# variables  
lenght = 4
score  = 1 
 

def game():
    global lenght #variabels global pour modifier a travers ma fonction
    global score #variabels global pour modifier a travers ma fonction
    
    while True:
        randomNumber = ''.join([str(random.randint(0, 9)) for i in range(lenght)])
        
        print('Retenez la séquence')
        print(randomNumber)
        time.sleep(3)
        os.system('cls')
        
        # Reponse utilisateur
        userAnswer = input('Entrez votre réponse : ')
        
        # Bonne réponse 
        if(userAnswer == randomNumber):
            print('Bonne réponse');
            time.sleep(2)
            score += 1;
            lenght += 1;
            
        # Mauvaise réponse 
        else: 
            print(f'Mauvaise réponse, la réponse était {randomNumber}')
            print(f'Votre score finale est de {score}')
            break
            
        


game()