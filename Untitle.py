print("Calculator app")

def divide(a,b):
    if b==0:
        print("can't divide by zero")
        return
    else:
        return a/b
    
commands={
    "+" : lambda a,b:a+b,
    "-" : lambda a,b:a-b,
     "*" :lambda a,b:a*b,
     "^":lambda a,b:a**b,
     "/":lambda a,b:divide(a,b),
}

while True:

    while True:
        try:
            num1=float(input("Enter number: "))
            break
        except ValueError:
            print("invalid input")

    while True:
            operator=input("+/-/*/^/ /: ")
            if operator in commands:
                break
            else:
                print("Enter valid operator")
                
    while True:
        try:
            num2=float(input("Enter number: "))
            result= commands[operator](num1,num2)
            print("Answer=",result)
            break
        except ValueError:
            print("invalid input")
   

  