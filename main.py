import random
import os



def  clear():
     os.system('clear')

user_name=input("Please enter your name :")

user_win_times=0

computer_win_times =0



choice =['rock','paper','scissor']

menu='''Welcom to our game choose beteween 
1:Rock 
2:Paper 
3:Scissor 
4:Quit the game as Q or q
'''





def Quit_game():

    user_winnning=(f"The final winner is{ user_name} with total wins : {user_win_times}")
    com_winning=(f"The final winner is Computer with total wins : {computer_win_times}")

    user_wins= (user_win_times>computer_win_times)

    com_wins= (user_win_times<computer_win_times)

    if user_wins:
          print(user_winnning)

    elif com_wins:
        print( com_winning)
    
    else:
          print(f"Drow")



def Random_py_comp():

     return random.choice(choice)


def Logic(user_choice,comp_choice):
     global user_win_times,computer_win_times


     if user_choice =="rock" and comp_choice=="scissor":
          user_win_times+=1
          print ("User wins")
     

     elif user_choice =="paper" and comp_choice=="rock":
          user_win_times+=1
          print ("User wins")
     

     elif user_choice =="scissor" and comp_choice=="paper":
          user_win_times+=1
          print ("User wins")
     

     elif user_choice ==comp_choice:
          print ('Drow')
     

     else:
          
          computer_win_times+=1
          print ("Computer wins")
     

     



while True:

    print(f'\nUser total wins = {user_win_times}')
    print(f'\nComputer total wins = {computer_win_times}')
    
    user_choice= input("Enter your choice ").lower()

    if user_choice=="q":
        Quit_game()
        break

    

    if user_choice in choice:
        comp_choice=Random_py_comp()
        Logic(user_choice,comp_choice)
               
              
            

    clear()
              


