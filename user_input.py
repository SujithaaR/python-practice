#user input

# a=input("print the input: \n")
# print(a)
# print(type(a))

#Rock,Paper,Scissor
import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3

# print(RPS(2))
# print(RPS(1))
# print(RPS(3))

# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

print("")
playerchoice=input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissor\n\n")
# print(playerchoice)
# print(type(playerchoice))

player=int(playerchoice)
if player<1 or player>3:
    sys.exit("You must enter 1,2 or 3")

computerchoice=random.choice("123")

computer=int(computerchoice)

print("")

print("your choice : "+str(RPS(player)).replace('RPS.','')+".")
print("computer choice : "+str(RPS(computer)).replace('RPS.','')+".")

if player==1 and computer==3:
    print("🔥🔥you win🔥🔥")
elif player==2 and computer==1:
    print("🔥🔥you win🔥🔥")
elif player==1 and computer==2:
    print("🔥🔥you win🔥🔥")
elif player==computer:
    print("Game tie")
else:
    print("python wins")
    
    
    
