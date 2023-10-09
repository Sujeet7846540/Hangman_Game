import random
from hangman_words import word_list
from hangman_stages import stages
from hangman_stages import logo
import os

lives=6
print(logo)
# word_list=["ardvark","baboon","camel"]

chosen_word=random.choice(word_list)
blankl=[]
for i in range(len(chosen_word)):
    blankl.append("_")
print(blankl)
# print(chosen_word)
end_game=False

while end_game==False:
    # print("Lives Left: ",lives)
    inp=input("Enter a Letter to guess the Word: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]==inp:

            blankl[i]=chosen_word[i]
        # else:
            # print("Wrong Guess (-_-)")
        
    if inp not in chosen_word:
        lives=lives-1
        print("You Guessed a worng Word, You Loose a Life (-_-)")
    
    print(blankl)
    if "_" not in blankl:
        end_game=True
        print("You Won")
        print(chosen_word)
        # os.clear()
    if lives==0:
        end_game=True
        print("You Loose (-_-)")
        print(chosen_word)
        # os.clear()
    print(stages[lives])
    
    



        # print("Right")
    # else:
    #     print("Wrong") 


a=input()