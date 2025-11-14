"""My first attempt at trying to search through a list....searching can be tricky and using if statements is very
tricky ...one has to careful on how they seach through a list.."""
expense=input("Enter expense to mark: ")
data=["there was a dictionary with three keys"]
for v in data[1:]:
       if expense.strip()==v["Expenses"].strip():
        if v["bought"]=="[]":
           v["bought"]="[x]"
           break
        else:
           print("item already bought.")
           break
       else:
          match=get_close_matches(expense,[c["Expenses"] for c in data[1:]],cutoff=0.2)
          answer=input(f"Did you mean {match[0]}? yes or no?:").lower().strip()
          if answer=="yes":
             for v in data[1:]:
               if v["Expenses"]==match:
                   print(v["Expenses"])
                   if v["bought"]=="[]":
                      v["bought"]="[x]" 
                      print("Item marked")
                      break
                   else:
                      print("item already bought.")

