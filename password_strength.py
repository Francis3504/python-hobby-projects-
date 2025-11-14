import re
#i tried my best😊❤
print("Welcome members")
def store(password):
    with open("password.txt","w") as file:
         file.write(password+"\n")

def confirm(password):
    with open("password.txt","r") as file:
        a=file.readlines()
        l=[l.strip() for l in a]                                                                                                        
        if password.strip() in l:
          print("Correct password")
        else:
          print("wrong password")
          conf=input("Re-enter password: ")
          confirm(conf)

def login(n):
    with open("password.txt","r") as file:
        a=file.readlines()
        l=[l.strip() for l in a]                                                                                                        
        if n.strip() in l:
          print("logging in  success")
        else:
          print("Wrong password, re-enter")
          conf=input("Re-enter password: ")
          login(conf)

def check(password):
    with open("password.txt","r") as file:
        a=file.readlines()
        l=[l.strip() for l in a]                                                                                                        
        if password.strip() in l:
          print("password already exists")
          pas=input("Enter password:")
          check(pas)
        else:
          alpha=bool(re.search(r"[a-zA-z]",password))
          numeric=bool(re.search(r"\d",password))
          special=bool(re.search(r"[!~@#$&]",password))
          strength=sum([alpha,numeric,special])
          score=3 #strong password
          if strength==score:
             print("Strong password")
          elif strength==score-1:
             print("weak password")
          else: 
             print("Very weak password")
          
          choice=input("DO you want to store or enter a new one?(yes or no.)").lower()
          if choice=="yes":
              get=input("Enter password:")
              gain(get)
          else:
             store(password)

def gain(get):
  while True:
    if len(get)<=8:
      print("Short length")
      get=input("Enter password:")
      continue
    else: 
      check(get)
      break

while True:
  status=input("Are you new or old: ").lower()
  if status=="new":
    print("must atleast have 8 characters with numbers/letters/speacial characters")
    get=input("Enter password:")
    gain(get)
    conf=input("Re-enter password: ")
    confirm(conf)
    break
  elif status=="old":
    new=input("Enter password to login: ")
    login(new)
    break
  else:
     print("Do you want to be a member?")