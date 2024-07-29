print("welcome to the quitz game:")

player=input("Are you ready? " )
score = 0

if player.lower() != "yes":
    quit()
else:
    print("lets begain")

answer = input("1.what is the capital city of Nepal? ")
if answer.lower() == "kathmandu":
    print("You are correct!")
    score += 1
else:
    print("Incorret answer!")

answer = input("2.what is CPU  stand for ?" )
if answer.lower()=="central processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorret answer!")

answer = input("3.what is ALU stand for ?" )
if answer.lower()=="Arithmetic and logical unit":
    print("You are correct!")
    score += 1
else:
    print("Incorret answer!")

print("You got "+ str(score) + " question correct")
print("You got "+ str((score/3)*100)+" question correct")



