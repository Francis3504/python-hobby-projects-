import csv
print("Student grade tracker app.\n")
def save(students):
  try:
    data=write(students)
    if not data:
      print("Data not saved ")
    else:
      print("Data  saved")
  except FileNotFoundError:
    print("file doesn't exist")

def write(students):
   try:
    with open("Grade.csv", "w",newline="") as file:
     csv.DictWriter(file,fieldnames=["Name","score","Grade"]).writeheader()
     csv.DictWriter(file,fieldnames=["Name","score","Grade"]).writerows(students)
     return True
   except FileNotFoundError:
     print("File doesn't exist")

def grade():
  data=read()
  grades=[(86,"A+"),(80,"A"),(70,"B+"),(60,"B"),(55,"C+"),(50,"C"),(40,"D+"),(0,"D")]
  for index,info in enumerate(data,1):
    score=float(info["score"])
    info["Grade"]=next(grade for mark,grade in grades if score>=mark)
    print(f"{index}.{info["Name"]}:{info["score"]}:{info["Grade"]}")
  write(data)

def show():
  reader=read()
  for i,get in enumerate(reader,1):
    print(f"{i}.{get["Name"]} : {get["score"]}")

def average():
  reader=read()
  scores=[float(r["score"]) for r in reader]
  average=round(sum(scores)/len(scores))
  print(f"Average mark is {average}")
  
def highest():
  reader=read()
  a=[float(mark["score"]) for mark in reader]
  mark=max(a)
  for  info in reader:
    if float(info["score"])==mark:
      print(f"highest is { info["Name"]} with {mark}%")
      break

def read():
  try:
   with open("Grade.csv","r") as file: 
    reader= csv.DictReader(file)
    return list(reader)
  except FileNotFoundError:
    return []

def details():
   while True:
      try:
       number=int(input("Enter number of students: "))
       for _ in range(number):
          try:
            student=input("Enter student's name: ").capitalize()
            while True:
             score=float(input("Enter score:  "))
             if not 0<=score<=100:
               print("Score must be between 0 and 100")
               continue
             break
          except ValueError:
            print("Invalid input")
          grade={"Name":student, "score":score}
          students.append(grade)
       save(students)
       return
      except ValueError:
        print("invalid input")
  
def moderate(mark):
  reader=read()
  for row in reader:row["score"]=min(float(row["score"])+mark,100)
  write(reader)

def mark():
  while True:
   try:
    mark=float(input("Enter marks to moderate."))
    if mark<0:
      print("Enter positive number: ")
      continue
    else:
      return mark
   except ValueError:
    print("Enter number")
commands={
    "1":details,
    "2"  : show,
    "3" : average,
    "4" : highest,
    "5" :grade,
    "6":lambda:moderate(mark())
}

students=[]
def main():
 while True:
  print("1.Enter details.")
  print("2.Show the recorded data.")
  print("3.Show average score.")
  print("4.Show the highest student(s).")
  print("5.Show grades.")
  print("6.Moderate results.")
  print("7.Exit.\n")
  choice=input("Enter your choice: ").strip()

  a=commands.get(choice)
  if choice=="7":
   break
  elif a:
    a()
  else:
    print("Command doesn't exit ")

if __name__=="__main__":
   main()