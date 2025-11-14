import random
def get_number():
  while True:
        try:
          number=int(input("Guess the number am thinking about between 1 and 10: "))
          if number<0:
            print("Enter postive number.")
            continue
          return number
        except ValueError:
          print("Invalid input")

def play():
  correct_number=random.randint(1,10)
  won=False
  for _ in range(3): #3 is the number of attempts of the player
      number=get_number()
      if number==correct_number:
       won=True
       print("You've won!")
       return
      elif number<correct_number:
       print("Too low")
      else:
       print("Too high")
      if not won:
       print(f"You're out of guesses,the correct number is {correct_number}")

def main():
 while True:
  answer=input("do you want to play guessing game, yes or no: ").lower()
  if answer=="yes":
   play()
  elif answer=="no":
   print("Thank you for your time.Goodbye!")
   break
  else:
   print("Enter valid answer!")

if __name__=="__main__":
  main()
   
