print("Welocme ")
master_pws = input("what is  your password? ")

def add():
 name = input("User name: ")
 psw=input("password: ")

 with open ("password.txt", "a") as f:
  f.write(name + "|" + psw +'\n')

def view():
 with open("password.txt","r") as f:
  for line in f.readline():
    data= print(line.rstrip)
    user, passw = data.split('|')
    print("User:" , user,"|","Password:" ,passw)


while 1: 
 mode = input("would you like to  add new  password or view a password(add/view) and type q to quit: ").lower()

 if mode=='q':
  break
 
 if mode == "add":
  add()
 
 elif mode =="view":
  view()
 
 else:
  print("Invalid mode")
  continue