print("Welcome to Game")
import random

user_wins =0
computer_wins = 0

option = ["rock","scissor","papper"]
while True:
 user = input("rock or scissor or papper or q for quit:" ).lower()

 if user == "q":
    break

 if user not in option:
   continue
 
 random_number = random.randint(0,1)
 computer = option[random_number]
 print("computer picked.."  +   computer  + " . ")

 if user == "rock" and computer == "scissor":
  print("You won!")
  user_wins += 1

 elif user == "scissor" and computer=="papper":
  print("You won!")
  user_wins += 1

 elif user == "papper" and computer=="rock":
  print("You won!")
  user_wins += 1

 elif user == computer:
   print("Draw")

 else:
   print("You loose")

 computer_wins += 1

print("You won", user_wins , "times")
print("computer won" , computer_wins , "times")

print("Bye Bye see you next time".upper())