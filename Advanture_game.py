name = input("What is your name? ")
print("Welcome", name , "to advanture game.")

option = ["death","run"]

while True:
 choice = input("You are in the middle of the jungle and you encounter with bear. What will you do ? Act like death or run.(death/run)").lower()

 if choice not in option:
    continue
 
 elif choice == "death":
    print("Congraluation, You are alive.")

    print("Bear went away from you and walk for a while. You found a river and you have to cross the river. How will you cross the river?")
    choice = input("By swimming or by board or return to the original place(swim/board/original)").lower()

    if choice == "board":
        print("Congraluation, You are cross the river.")

        print("After crossing the you found the house . will you enter the house:")
        choice = input("if you enter house type yes otherwise no(yes/no) ").lower()

        if choice == "yes":
           print("congraluation! You found your mummy and daddy")
           break

        else:
           break
    
    elif choice=="swim":
        print("You lose! You are eatten by crocodile")
        break
        
    elif choice=="original":
        print("You lose! You are eatten by bear:")
        break
    
 else:
    print("You lose! You are eaten by bear")
    break

print("Thank you for playing.")
