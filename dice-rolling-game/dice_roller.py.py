import random,time
def get_dice_number():
    number=random.randint(1,6)
    print("rolling...")
    time.sleep(2)
    print(f"You have rolled:{number}")

while True:
    number=input("press 1 to roll/2 to exit:  ")
    if number=="1":
        get_dice_number()
    elif number=="2":
        print("Thank you using the app")
        break
    else:
        print("invalid choice")

 