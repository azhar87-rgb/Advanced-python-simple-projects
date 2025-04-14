from tkinter import *
from numpy import *
root=Tk()
result=0

def addition():
    a=int(num1.get())
    b=int(num2.get())
    result=Label(root,text=f'{add(a,b)}')
    result.place(x=100,y=100,height=50,width=50)  
    
def sub():
    a=int(num1.get())
    b=int(num2.get())
    result=Label(root,text=f'{subtract(a,b)}')
    result.place(x=100,y=100,height=50,width=50)
def mul():
    a=int(num1.get())
    b=int(num2.get())
    result=Label(root,text=f'{multiply(a,b)}')
    result.place(x=100,y=100,height=50,width=50)
def insert_num1(no):
    num1.insert(INSERT,no)
def enter():
    def insert_num2(no):
      num2.insert(INSERT,no)  
root.title("SIMPLE CALCULATOR")
root.geometry("500x500")
root.config(bg="blue")
num1=Entry(root,font=('callibri',10))
num2=Entry(root,font=('callibri',10))
num1.place(x=50,y=120,height=50,width=300)
# num2.place(x=50,y=180,height=50,width=300)

sum=Button(root,text="+",bg="white",fg="black",relief=RAISED,command=addition)
sum.place(x=300,y=250,height=30,width=60)

diff=Button(root,text="-",bg="white",fg="black",relief=RAISED,command=sub)
diff.place(x=300,y=280,height=30,width=60)

prod=Button(root,text="x",bg="white",fg="black",relief=RAISED,command=mul)
prod.place(x=300,y=310,height=30,width=60)

one=Button(root,text="1",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(1))
one.place(x=50,y=250,height=30,width=60)
two=Button(root,text="2",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(2))
two.place(x=110,y=250,height=30,width=60)
three=Button(root,text="3",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(3))
three.place(x=170,y=250,height=30,width=60)
four=Button(root,text="4",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(4))
four.place(x=230,y=250,height=30,width=60)
five=Button(root,text="5",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(5))
five.place(x=50,y=280,height=30,width=60)
six=Button(root,text="6",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(6))
six.place(x=110,y=280,height=30,width=60)
seven=Button(root,text="7",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(7))
seven.place(x=170,y=280,height=30,width=60)
eight=Button(root,text="8",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(8))
eight.place(x=230,y=280,height=30,width=60)
nine=Button(root,text="9",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(9))
nine.place(x=50,y=310,height=30,width=60)
zero=Button(root,text="0",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1(0))
zero.place(x=110,y=310,height=30,width=60)
hash=Button(root,text="#",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1('#'))
hash.place(x=170,y=310,height=30,width=60)
star=Button(root,text="*",bg="white",fg="black",relief=RAISED,command=lambda:insert_num1('*'))
star.place(x=230,y=310,height=30,width=60)


root.mainloop()