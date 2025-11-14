#I coded this on my own ....i'm proud of myself..job well done😊💖
import os
import csv
from difflib import get_close_matches

FIlE="expenses.csv"
fields=["Expenses","prices","bought","salary"]
def set_up_csv():
    if not os.path.exists(FIlE):
        with open(FIlE,"w",newline="") as file:
            write=csv.DictWriter(file,fieldnames=fields)
            write.writeheader()

def load_data():
    with open(FIlE,"r") as file:
        read=csv.DictReader(file)
        return list(read)
    
def add_expenses(data):
    with open(FIlE,"w",newline="") as file:
        fg=csv.DictWriter(file,fieldnames=fields)
        fg.writeheader()
        fg.writerows(data)

def write_expenses(data):
   with open(FIlE,"w",newline="") as file:
      n=csv.DictWriter(file,fieldnames=fields)
      n.writeheader()
      n.writerows(data)
      return True

def options():
    print("Enter number to perform any of the actions")
    option=["1.show_expenses","2.check_balance","3.mark_bought_items",
            "4.update_expenses","5.remove_expenses","6.Show_marked_items",
            "7.To exit"]
    for op in option:
       print(op)

def show_expenses(data):
    for i,e in enumerate(data[1:],1):
        print(f"{i}.{e["Expenses"]}-k{e["prices"]}")

def show_marked_items(data):
   for i,v in enumerate(data[1:],1):
      print(f"{i}.{v["Expenses"]}--k{v["prices"]}:{v["bought"]}")

def check_balance(data):
    amount=data[0].get("salary")
    total=[float(e["prices"].strip()) for e in data[1:]]
    if sum(total)>=float(amount):
       print("No money left")
    else:
     balance=float(amount)-sum(total)
     print(f"balance from amount of {amount} is :k{balance}")
   
def mark_bought_items(data): 
    #a proper searching algorithm was devised
    expense=input("Enter expense to mark: ")
    for v in data[1:]:
       if expense.strip()==v["Expenses"].strip():
        if v["bought"]=="[]":
           v["bought"]="[x]"
           print("item marked")
           write_expenses(data)
        else:
           print("item already bought.")
        return
       
    match=get_close_matches(expense,[c["Expenses"] for c in data[1:]],cutoff=0.2)
    choice=input(f"Did you mean {match[0]} ? yes/no:").lower().strip()
    if choice=="yes":   
       for n in data[1:]:
          if n["Expenses"].strip()==match[0].strip():
             if n["bought"]=="[]":
                n["bought"]="[x]"
                print("item marked.")
                write_expenses(data)
             else:
                print("item marked already.")
             return
    else:
       print("It doesn't exist.")
       return
      
def update_expenses(data):
    print("press 1 for expense and 2 for item.")
    choice=input("Do you want to update expense or item? ")
    found=False
    if choice=="1":
       old=input("Enter old expense: ").lower()
       new=input("Enter new expense: ").lower()
       for n in data[1:]:
          if n["Expenses"].strip().lower()==old:
             n["Expenses"]=new
             found=True
             entered=write_expenses(data)
             print("expense updated") if entered else print("not updated")
             return
       if not found:
        match=get_close_matches(new,[v["Expenses"].strip().lower() for v in data[1:]],cutoff=0.12)
        confirm=input(f"Did you mean {match[0]}? yes or no: ").strip().lower()
        if confirm=="yes":
           for n in data[1:]:
              if n["Expenses"].strip().lower()==match.strip():
                 n["Expenses"]=new
                 print("Updated")
                 write_expenses(data)
                 return
        else:
           print("Expense doesn't exist")
           return
    else:
       old=input("Enter old price: ")
       new=input("Enter new price: ")
       for n in data[1:]:
          if n["prices"].strip()==old.strip():
             n["prices"]=new
             found=True
             entered=write_expenses(data)
             print("price updated") if entered else print("not updated")
             return
       if not found:
        match=get_close_matches(new,[v["prices"].strip().lower() for v in data[1:]],cutoff=0)
        confirm=input(f"Did you mean {match[0]}? yes or no: ").strip().lower()
        if confirm=="yes":
           for n in data[1:]:
              if n["prices"].strip()==match[0].strip():
                 n["prices"]=new
                 print("Updated")
                 write_expenses(data)
                 return
        else:
           print("price doesn't exist")
           return
        
def remove_expenses(data):
    expense=input("Enter expense to mark: ")
    for i,v in enumerate(data[1:]):
       if expense.strip()==v["Expenses"].strip():
           del data[i]
           print("Expense deleted")
           write_expenses(data)
           return
       
    match=get_close_matches(expense,[c["Expenses"] for c in data[1:]],cutoff=0.2)
    choice=input(f"Did you mean {match[0]} ? yes/no:").lower().strip()
    if choice=="yes":   
       for n in data[1:]:
          if n["Expenses"].strip()==match[0].strip():
                del data[i]
                print("Expense deleted.")
                write_expenses(data)
                return
    else:
       print("Expense doesn't exist")

commands={"1":lambda:show_expenses(load_data()),
          "2":lambda:check_balance(load_data()),
          "3":lambda:mark_bought_items(load_data()),
          "4":lambda:update_expenses(load_data()),
          "5":lambda:remove_expenses(load_data()),
          "6":lambda:show_marked_items(load_data())
          }

def main():
  set_up_csv()
  data=load_data()
  salary=input("Enter salary or income: ")
  data.append({"salary":salary})
  print("Press 1 when you're done:")
  while True:
     enter=input(": ").strip()
     if enter=="1":
        answer=input("Are you done with recording expenses? yes or no?").strip().lower()
        if answer=="yes":
           break
        else:
           continue
     else:
        expense=input("enter expense: ").strip().lower()
        price=input("enter amount: ")
        budget={"Expenses":expense, "prices": price,"bought":"[]"}
        data.append(budget)
        add_expenses(data)
        
  while True:
    options()
    choices=input(">")
    choice=commands.get(choices)
    if choice:
     choice()
    elif choice=="7":
      print("Thank you for using our app")
    else:
      print("Enter valid choice")

if __name__=="__main__":
   main()