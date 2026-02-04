import random,time
from logic import find_winner
options=["rock","paper","scissors"]
def show_menu():
    print("""
          Press the numbers to play 
          1.rock  
          2.paper
          3.scissors
         """)
def get_computer_choice():
    return random.choice(options)

def play_game():
    opt={
         "1":"rock",
         "2":"paper",
         "3":"scissors"
       }
    show_menu()
    while True:
       try:
         rounds=int(input("How many rounds do you want to play?.Enter whole number: "))
         if rounds <0:
            print("Enter positive number")
            continue
         break
       except ValueError:
            print("Enter valid answer.")
    for _ in range(rounds):
      for i,n in enumerate(options):
        if i==0:
            print(n)
            time.sleep(0.5)
        print(n)
        time.sleep(0.5)
      while True:
        number=input("play: ")
        option=opt.get(number)
        if option:
            break
        else:
            print("invalid choice") 
      comp=get_computer_choice()
      time.sleep(1)
      print(f"You:{option}")
      print(f"Me:{comp}")
      find_winner(comp,option)