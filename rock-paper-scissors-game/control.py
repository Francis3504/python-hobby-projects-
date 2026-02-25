from base import intialize_csv
from interface import play_game
from logic import dispay_points
def main():
    intialize_csv()   
    while True:
        print("""Type the letters to 
             a.Play game
             b.Exit game
             c.show scores""")
        
        choice=input(": ").strip().lower()
        if choice=="a":
           play_game()
        elif choice=="b":
            print("Thank you for playing!")
            break
        elif choice=="c":
            comp,play=dispay_points()
            print(f"You have {play} wins ")
            print(f"I have {comp} wins ")
        else:
            print("invalid answer")

if __name__=="__main__":
    main()