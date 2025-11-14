import tkinter as tk
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,width=23,font=("Arial,18"),borderwidth=3,relief="ridge",justify="right")
entry.grid(row=0,column=0,columnspan=4,pady=5)
def click(symbol):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+str(symbol))

def clear():
    entry.delete(0,tk.END)

def evaluate():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

buttons=[("7",1,0),("8",1,1),("9",1,2),("/",1,3),
          ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
          ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
          ("0",4,0),(".",4,1),("+",4,2) ,("=",4,3),]
for (text,r,c) in buttons:
    if text=="=":
        tk.Button(root,text=text,width=5,height=5,command=evaluate).grid(row=r,column=c)
    else:
        tk.Button(root,text=text,width=5,height=5,command=lambda t=text:click(t)).grid(row=r,column=c)
tk.Button(root,text="C",width=22,height=2,command=clear).grid(row=5,column=0,columnspan=4)
root.mainloop()