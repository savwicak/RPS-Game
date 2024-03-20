.import time
import random 

time.sleep(0.5)
print("Hello, Welcome to the Rock Paper scissors Game!")
time.sleep(0.5)
print("Please input Rock or paper or Sisors if you want to stop input stop :D")
time.sleep(0.5)
print("There is score! type score if you want to see it!")
time.sleep(2)
 
rps = ["rock", "paper", "scissors"]
player = input("Please input your answer: ")
score = 0

while player != "stop":
    computer = random.choice(rps)
    if player != "score":
        print("Player answer: ", player, "computer answer: ",computer)
        
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "papper":
            print("Computer Win")
        else:
            print ("Player Win")
            score += 1
    elif player == "scissors" :
        if computer == "rock":
            print("computer win!")
        else:
            print("player win!")
            score += 1
    elif player == "paper" :
        if computer == "scissors":
            print("computer win!")
        else:
            print("player win!")
            score += 1
    elif player == "score":
        print("your score: ", score)
    else:
        print("Please type the right answer")

    player = input("Please input your answer: ")

print("Thank you for playing")
print("your final score: ", score)
