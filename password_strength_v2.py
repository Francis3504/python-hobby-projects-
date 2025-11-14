import re
import os
import hashlib
import json
File="info.json"
def check_strength(password):
   alpha=bool(re.search(r"[a-zA-Z]",password))
   numeric=bool(re.search(r"\d",password))
   special=bool(re.search(r"[~!@#$%^&]",password))
   length=len(password)>=8
   strength=sum([alpha,numeric,special,length])
   if strength==4:
      print("strong")
   elif strength==3:
      print("weak")
   else:
      print("very Weak")
def check(a,b):
   if os.path.exists(File):
    try:
      with open(File,"r") as file:
         e=json.load(file)
    except json.JSONDecodeError:
      e=[]
   else:
       e=[]

   for i in e:
     if i["username"]==a:
      print("username exists")
      return
     if i["password"]==b:
      print("password exist")
      return
   check_strength(b)
   salt=os.urandom(16).hex()
   p=hashlib.sha256((salt+b).encode()).hexdigest()
   save(a,p,e)

def save(a,p,e):
   inf={"username":a,"password":p}
   e.append(inf)
   with open(File,"w") as file:
      json.dump(e,file,indent=4)
      print("saved")

print("Press 1 to sign up or 2 login")
choice=input("sign up or login?:  ")
if choice=="1":
    name=input("Enter username: ")
    password=input("Enter password: ")
    check(name,password)
