while True:
  
  try:
   num1=float(input("Enter number: "))
   operator=input('Enter an operator: ')
   num2=float(input("Enter number: "))

   if operator=="+":
    print(num1+num2)
   elif operator=="-":
    print(num1-num2)
   elif operator=="*":
    print(num1*num2)
   elif operator=="/":
    if round(num2)==0:
     print("math error")
    else:
       print(num1/num2)
   elif operator=="^":
      print(num1**num2)
   else: 
      print("enter the basic math operators")
      
  except ValueError:
   print("enter valid input")
   
  