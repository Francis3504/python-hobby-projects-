print("To do list app.\n")
def read_tasks():
   try:
    with open("Chores.txt", "r") as file:
      task=file.readlines()
      file.seek(0)
      return [t.strip() for t in task]
   except FileNotFoundError:
      return []

def write_tasks(task):
   with open("Chores.txt","w") as file:
         for lin in task:
            file.write(lin+"\n")
def add():
   task=input("Enter task: ")
   try:
     with open("Chores.txt","a") as file:
        tasks=file.write(task+ "\n")
        if not tasks:
           print("task not added: ")
        else:
           print("Task has been added:")
   except FileNotFoundError:
      print("file doesn't exist for chores: ")

def show_task():
      tasks=read_tasks()
      for i,task in enumerate(tasks,1):
         print(f"{i}. {task}")

def remove():
   show_task()
   num=int(input("Enter number: "))
   line=read_tasks()
   remove=line.pop(num-1)
   print(f"removed: {remove}")
   write_tasks(line)
      
def update():
      show_task()
      num,task=num_task(choice.lower())
      line=read_tasks()
      del line[num-1]
      line.insert(num-1,task)
      write_tasks(line)
      print(f"Task has been updated to {task}")

def mark():
      show_task()
      num,task=num_task(choice.lower())
      line=read_tasks()
      lm=[j.strip() for j in line]
      if num<=len(lm):
         for index,lin in enumerate(lm):
          if index==num-1:
            if not lin.endswith(":done"):
               line[index]=task+":done"
               write_tasks(line)
               print("Task has been marked.")
               break
            else:
               print("task already marked")
      else:
       print("Exceeded the number of tasks")

def num_task(action):
   num=int(input(f"Enter the number to {action}:"))
   task=input( f"Enter task to {action}: ")
   return num,task  

commands={
   "1":add,
   "2":show_task,
   "3"  : mark,
   "4" : update,
   "5" : remove}

while True:
   print("1.Add task.")
   print("2.Show added task(s).")
   print("3.Tick a completed task.")
   print("4.Update/Change a task.")
   print("5.Remove a task.")
   print("6.Exit.\n")
   
   choice=input("Enter your choice: ").strip()
   if choice=="6":
      print("Thank you for using the app!")
      break
   action=commands.get(choice)
   if action:
      action()
   else:
      print("Invalid choice")