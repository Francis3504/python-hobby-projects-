CORRECT_NUMBER=5
attempts=3
for _ in range(attempts):
    number=int(input("Guess the number am thinking about between 1 and 10: "))
    if number==CORRECT_NUMBER:
        print("you've guessed correctly, you win.")
        break
    else:
        print("wrong guess.")
        
