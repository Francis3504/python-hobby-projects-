try:
 with open("count.txt","r") as file:
    a=file.readlines()
    try:
     c=[v for v in a]
     for i,x in enumerate(c):
        print(f"There is/are {x} {c.count(c[i])} word(s)")
    except IndexError as e:
      print(e)
except FileNotFoundError:
   print("File doesn't exist")