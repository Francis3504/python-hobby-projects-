import random
correct_number=random.randint(1,10)
won=False
while True:
 answer=input("do you want to play a guessing game, yes or no: ").lower()
 if answer=="yes":
   for _ in range(3): #3 is the number of attempts of the player
      while True:
        try:
          number=int(input("Guess the number am thinking about between 1 and 10: "))
          if number<0:
            print("Enter postive number.")
            continue
          break
        except ValueError:
          print("Invalid input")
      if number==correct_number:
       won=True
       print("You've won!")
       break
      elif number<correct_number:
       print("Too low")
      else:
       print("Too high")

   if not won:
    print(f"You're out of guesses,the correct number is {correct_number}")

 elif answer=="no":
  print("Thank you for your time.Goodbye!")
  break
 else:
   print("Enter valid answer!")
   
