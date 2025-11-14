while True:
    option=input("Do you want to check if a whole number is even,yes or no: ").lower()
    if option=="yes":
        numbers=int(input("How many numbers do you want to check?."))   
        for _ in range(numbers):
            try:
             num=int(input("Enter a whole number: "))
             print(f"{num} is an even number") if num%2==0 else print(f"{num} is an odd number")
            except ValueError:
               print("invalid input")
    elif option=="no":
       print("Thank you for your time.")
       break
    else:
       print("Invalid choice")
    

        