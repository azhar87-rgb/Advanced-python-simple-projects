from tkinter import *
import os
power=Tk()
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")
    
power.title("POWER APP")
power.geometry('400x400')
power.config(bg="black")
R_button=Button(power,text="Restart",font=("callibri",20,"bold"),relief=RAISED,cursor="plus",command=restart)
R_button.place(x=120,y=40,height=50,width=150)

RT_button=Button(power,text="Restart Time",font=("callibri",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
RT_button.place(x=120,y=140,height=50,width=165)

lg_button=Button(power,text="Log-Out",font=("callibri",20,"bold"),relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=120,y=240,height=50,width=150)

st_button=Button(power,text="ShutDown",font=("callibri",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=120,y=340,height=50,width=150)

power.mainloop()