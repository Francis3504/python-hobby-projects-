print("A couple name combiner.")
print("You can take turns entering the name.\n")

while True:
  print("1.Play game.")
  print("2.Exit.\n")
  choice=input("Enter your choice: ").strip()
  if choice=="1":
    name1=input("Enter your name(boy or girl's first or laste name):").capitalize().strip()
    name2=input("Enter your name(boy or girl's first or last name):").lower().strip()
    slice1=name1[:3]
    slice2=name2[-3:]
    print("Your combined couple  name is",slice1+slice2)
  elif choice=="2":
    print("Thank you for playing.")
    break
  else:
    print("Invalid choice .")


