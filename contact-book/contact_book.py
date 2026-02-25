import json
print("Contact Book App")

def store(contacts):
    with open("contacts.json","w") as file:
       store_data=json.dump(contacts,file,indent=4)
       if store_data:
          print("Data saved.")
       
           
def search():
    with open("contacts.json","r") as file:
       v=json.load(file)
       choice=input("Do you wana search by name/number/email/show(everything):").lower()
       if choice=="name":
          name=input("Enter name: ")
          for f in v:
             if f["Name"]==name:
                print("Name exists")
             else:
                print("it doesn't exist")
       elif choice=="number":
          number=input("Enter number: ")
          for f in v:
             if f["number"]==number:
                print(f"Number exists of {f["Name"]}")
             else:
                print("info not available")
       elif choice=="email":
          email=input("Enter email: ")
          for f in v:
             if f["email"]==email:
                print(f"email of {f["Name"]} exist")
             else:
                print("Email doesn't exist")
       else:
          show()
          
def delete():
    with open("contacts.json","r") as file:
       v=json.load(file)
       choice=input("Do you want to delete everything  by name/number/email/show(everything):").lower()
       if choice=="name":
          name=input("Enter name: ")
          for i,f in enumerate(v):
             if f["Name"]==name:
                del v[i]
                print(f"contact deleted")
                break
             elif f["Name"]=="":
                print("it doesn't exist")
       elif choice=="number":
          number=input("Enter number: ")
          for i, f in enumerate(v) :
             if f["number"]==number:
                del v[i]
                print("contact deleted")
             else:
                print("info not available")
       elif choice=="email":
          email=input("Enter email: ")
          for i,f in enumerate(v):
             if f["email"]==email:
                del v[i]
                print("contact deleted")
             else:
                print("Email doesn't exist")
       else:
          show()
       with open("contacts.json","w") as file:
          json.dump(v,file,indent=4)

def show():
    with open("contacts.json","r") as file:
      f= json.load(file)
      for index,info in enumerate(f,1):
         print(f"{index}.Name:{info["Name"]}")
         print(f"number:{info["number"]}")
         print(f"email:{info["email"]}")

def update():
    show()
    with open("contacts.json","r") as file:
       v=json.load(file)
       choice=input("Do you want to update name/number/email:").lower()
       if choice=="name":
          name=input("Enter old name: ").capitalize()
          for f in v:
             if f["Name"]==name:
                new=input("Enter new name: ")
                f["Name"]=new
                print("Name updated")
             else:
                print("it doesn't exist")
       elif choice=="number":
          number=input("Enter old number: ")
          for  f in v:
             if f["number"]==number:
                new=input("Enter new number: ")
                f["number"]=new
                print("Number updated")
             else:
                print("info not available")
       elif choice=="email":
          email=input("Enter old email: ")
          for f in v:
             if f["email"]==email:
                n=input("Enter new email: ")
                f["email"]=n
                print("Info updated")
             else:
                print("Email doesn't exist")
       with open("contacts.json","w") as file:
          json.dump(v,file,indent=4)

contacts=[]

while True:
    print("1.Enter contact info.")
    print("2.Save contact info.")
    print("3.Show all contacts.")
    print("4.Search for a contact info")
    print("5.Delete a contact.")
    print("6.Update/Change contact info.")
    print("7.Exit.\n")

    option=input("Enter your choice:").strip()

    if option=="1":
     name=input("Enter name: ").capitalize()
     number=input("Enter number: ")
     email=input("Enter email address: ")
     num={"Name":name,"number":number,"email":email}
     contacts.append(num)

    elif option=="2":
     store(contacts)

    elif option=="3":
     show()

    elif option=="4":
       search()

    elif option=="5":
       delete()

    elif option=="6":
       update()

    elif option=="7":
       break
    
    else:
       print("option doesn't exist")