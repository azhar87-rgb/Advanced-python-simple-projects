from tkinter import *
from time import *
import random as r
root=Tk()
def type() : 
    root.title("Typing Test")
    root.geometry("300x300")
    root.config(bg="black")
    label=Label(root,text="***Welcome to Typing Testing App***",font=("roman new style",20,"bold"),fg="white",bg="green")
    label.place(x=100,y=50)
    test=["The quick brown fox jumps over the lazy dog."," Books are indeed never failing friends of man."]
    test_1=r.choice(test)
    space=Label(root)
    space.pack()
        
    label_test=Label(root,text=test_1,font=("roman new style",20),fg="white",bg="blue")
    label_test.pack()
    space_3=Label(root)
    space_3.pack()
    time_1=time()
    entry=Entry()
    entry.config(font=('Ink black',40))
    entry.config(bg='white')
    entry.config(fg='black')
    entry.pack()

    def work():
        
        def Errors(testpara,inputpara):
            error=0
            for i in range(len(testpara)):
                try:
                    if testpara[i]!=inputpara[i]:
                        error=error+1
                except:
                    error=error+1
            return error
        def speed(start,end,inputpara):
            time_delay=end-start
            total_time=round(time_delay,2)
            speed=len(inputpara)/total_time
            return round(speed)
        time_2=time()
        test_2=entry.get()
        speed=Label(root,text=f'speed: {speed(time_1,time_2,test_2)} w/sec',font=("roman new style",20))
        speed.pack()
        space_1=Label(root)
        space_1.pack()
        error=Label(root,text=f'Error: {Errors(test_1,test_2)}',font=("roman new style",20),bg="red")
        error.pack() 
    mybutton = Button(root, text="Enter", padx=20, pady=20,relief=RAISED, command=work,fg="black", bg="blue")
    mybutton.pack()
def goodbye():
    space_7=Label(root)
    space_7.pack()
    thanks=Label(root,text='THANK YOU FOR USING THIS CODE',font=("roman new style",20),bg="green")
    thanks.pack()
Asking=Label(root,text="Ae you Ready? Press Y OR N",font=("roman new style",20),bg="green")
Asking.pack()
yes=Button(root, text="Y", padx=20, pady=20,relief=RAISED, command=type,fg="black", bg="blue")
yes.pack()
no=Button(root,text="N",padx=20, pady=20,relief=RAISED, command=goodbye,fg="black", bg="blue")
no.pack()
root.mainloop()