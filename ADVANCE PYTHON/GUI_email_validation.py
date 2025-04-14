from tkinter import *
import webbrowser  
# Add a URL of JavaTpoint to open it in a browser  
   
# Using urlopen() function with url in it  
 
root=Tk()

def Work():
    email=entry.get()
    a=0
    s=0
    c=0
    if len(email)>=6:
        if email[0].isalpha():
            if "@" in email and (email.count('@')==1):
                if email[-4]=='.':
                    for i in email:
                        if i.isspace():
                            s=1
                        elif i.isalpha():
                          if i==i.upper():
                            a=1
                        elif i.isdigit():
                            continue
                        elif i=='-' or i=='.' or i=='@':
                            continue
                        else:
                            c=1
                    if s==1 or a==1 or c==1:
                        label7=Label(root, text="Your Email has Invalid characters",font=60)
                        label7.pack()
                        
                    else:
                       label6=Label(root, text="SUCCESFULLY YOU ENTER THE EMAIL",font=60)
                       label6.pack()
                       url= 'https://www.javatpoint.com/python-tutorial'
                        
                else:
                    label5=Label(root, text="Email must have '.' before 'com'",font=60)
                    label5.pack()    
            else:
                label4=Label(root, text="Email must have at least one '@' character",font=60)
                label4.pack() 
        else:
            label3=Label(root, text="Email must not have uppercase letter",font=60)
            label3.pack()
            
    else:
        label2=Label(root, text="The Email length is too short",font=60)
        label2.pack()

   
label=Label(root, text="please enter your Email!",font=60)
label1=Label(root, text="  ")
label.pack()
label1.pack()
mybutton = Button(root, text="Enter", padx=20, pady=20, command=Work,fg="Blue", bg="RED")
mybutton.pack()
entry=Entry()
entry.config(font=('Ink black',20))
entry.config(bg='white')
entry.config(fg='black')
entry.pack()
root.mainloop()