print("Multiplication table generator.")
while True:
   try:
    number=int((input("Enter a number: ")))
    if number <0 :
     print("Enter positive number.")
    else:
       for i in range(1,13):
        print(number,"x ",i,"=",number*i)
   except ValueError:
    print("Enter a whole number.")

