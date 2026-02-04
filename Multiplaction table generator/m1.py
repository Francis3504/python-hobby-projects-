print("Multiplication table generator.")
number=int(input("Enter a number: "))
if number <0:
    print("you have entered a negative number.\nPlease enter a positive number.")
else:
    for i in range(1,1000):
        print(f"{number} x {i}={number*i}")
