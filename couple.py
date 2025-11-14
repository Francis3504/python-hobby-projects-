#Adding functions to my codes
def couple_name_combiner(option,name1,name2):
    if option.lower()=="first":
     a=name1.capitalize()[:3]
     b=name2.lower()[:3]
    else:
     a=name1.capitalize()[:3]
     b=name2.lower()[-3:]
    return a+b
while True:
  option=input("do you want to combine your partners first or last name: ")
  name1=input("Enter your first name: ")
  name2=input("Enter your partner's  name: ")
  print(f" Your combined couple name is: {couple_name_combiner(option,name1,name2)}" )