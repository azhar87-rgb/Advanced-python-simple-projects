from tkinter import *
import speedtest
sp=Tk()
def checker():
    spt = speedtest.Speedtest()
    spt.get_servers()
    down=str(round(spt.download()/(10**6),2))+"Mbps"
    up=str(round(spt.upload()/(10**6),2))+"Mbps"
    label_down.config(text=down)
    label_up.config(text=up)
    
sp.title("Internet speed checker")
sp.geometry("500x650")
sp.config(bg="black")
label=Label(sp,text="Internet speed checker",font=("callibri light",20,"bold"),bg="black",fg="white")
label.place(x=80,y=40,height=60,width=350)

label=Label(sp,text="Downloading..",font=("callibri light",20,"bold"))
label.place(x=80,y=120,height=60,width=350)

label_down=Label(sp,text="00",font=("callibri light",20,"bold"))
label_down.place(x=80,y=200,height=60,width=350)

label=Label(sp,text="Uploading..",font=("callibri light",20,"bold"))
label.place(x=80,y=280,height=60,width=350)

label_up=Label(sp,text="00",font=("callibri light",20,"bold"))
label_up.place(x=80,y=360,height=60,width=350)

button=Button(sp,text="Speed Checker",font=("callibri light",20,"bold"),bg="blue",command=checker)
button.place(x=150,y=440,height=100,width=200)


sp.mainloop()