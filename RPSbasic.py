import random
import time
import sys

def RPS_intro():
    print("Hello and welcome to rock, paper, scissors! \n In this game you will be playing against the system")
    time.sleep(1)
    print("You will be given a chance to input your choice and the computer will play its own choice")
    time.sleep(1)
    print("Good lucks!!")


# For the algo, the variable cpu_choice value given by randrange we will have the following values stand for the following choice
# 0 = Rock
# 1 = Paper
# 2 = scissors

def RPS_main():
    cpu_choice = random.randrange(0,3)
    play_choice = input("What is your choice? ")

    if (play_choice[0] == "r" or play_choice[0] == "R") and cpu_choice == 0:
        print(f"The computer chose rock, and you chose {play_choice}, you are both tied! ")

    elif (play_choice[0] == "p" or play_choice[0] == "P") and cpu_choice == 1:
        print(f"The computer chose Paper, and you chose {play_choice}, you are both tied! ")

    elif (play_choice[0] == "s" or play_choice[0] == "S") and cpu_choice == 2:
        print(f"The computer chose scissors, and you chose {play_choice}, you are both tied! ")

    # ALL OF THESE ARE THE TIES ^^^^^^^^^^^^^^^^^^^^^^

    elif (play_choice[0] == "p" or play_choice[0] == "P") and cpu_choice == 0:
        print(f"The computer chose rock, and you chose {play_choice}, you WIN!!! ")

    elif (play_choice[0] == "s" or play_choice[0] == "S") and cpu_choice == 1:
        print(f"The computer chose scissors, and you chose {play_choice}, you WIN!!! ")
   
    elif (play_choice[0] == "r" or play_choice[0] == "R") and cpu_choice == 2:
        print(f"The computer chose paper, and you chose {play_choice}, you WIN!!! ")


    # all of these you win ^^^^^^^^^^^


    elif (play_choice[0] == "p" or play_choice[0] == "P") and cpu_choice == 2:
        print(f"The computer chose scissors, and you chose {play_choice}, system WIN!!! ")

    elif (play_choice[0] == "r" or play_choice[0] == "R") and cpu_choice == 1:
        print(f"The computer chose paper, and you chose {play_choice}, system WIN!!! ")
   
    elif (play_choice[0] == "s" or play_choice[0] == "S") and cpu_choice == 0:
        print(f"The computer chose rock and you chose {play_choice}, system WIN!!! ")

    # All of these the system wins 
    

    else:
        print("Your choice is wrong!")

RPS_intro()
RPS_main()

