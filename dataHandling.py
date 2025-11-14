print("To do list app")
def add(task):
   try:
     with open("Chores.txt","a") as file:
        tasks=file.write(task+ "\n")
        if not task:
           print("task not added: ")
        else:
           print("Task has been added:")
   except FileNotFoundError:
      print("file doesn't exist for chores: ")

def show_task():
   with open("Chores.txt", "r") as file:
      task=file.readlines()
      tasks=[t.strip() for t in task]
      for i,task in enumerate(tasks,1):
         print(f"{i}. {task}")

def remove(num):
   with open("Chores.txt","r") as file:
      tasks=file.readlines()
      line=[line.strip() for line in tasks]
      remove=line.pop(num-1)
      print(f"remove: {remove}")
      with open("Chores.txt","w") as file:
         for lin in line:
            file.write(lin+"\n")
def update(num,task):
   with open("Chores.txt","r") as file:
      tasks=file.readlines()
      line=[line.strip() for line in tasks]
      del line[num-1]
      line.insert(num-1,task)
      with open("Chores.txt","w") as file:
         for lin in line:
            file.write(lin+"\n")  
def mark(num,task):
    with open("Chores.txt","r") as file:
      tasks=file.readlines()
      line=[line.strip() for line in tasks]
      for index,lin in enumerate(line):
         if index==num-1:
            if not(lin.endswith(":done")):
               line[index]=task+":done"
               with open("Chores.txt","w") as file:
                  for l in line:
                     file.write(l+"\n")
                  break
            else:
               print("task already marked")
while True:
   choice=input("add/show/mark/update/remove/exit :")
   if choice.lower()=="add":
      task=input("Enter task: ")
      add(task)
   elif choice.lower()=="show":
      show_task()
   elif choice.lower()=="mark":
      show_task()
      num=int(input("enter numer of task: "))
      task=input("Enter the task to be marked: ").lower()
      mark(num,task)
   elif choice.lower()=="update":
      show_task()
      num=int(input("Enter number: "))
      task=input("Enter task to update: ").lower()
      update(num,task)
   elif choice.lower()=="remove":
      show_task()
      num=int(input("Enter number: "))
      remove(num)
   elif choice.lower()=="exit":
      print("Thank for using the app: !")
      break
   else:
      print("Invalid choice")