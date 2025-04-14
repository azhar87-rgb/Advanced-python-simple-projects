from time import *
import random as r
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
while True:
    ck=input("ready to go Y/N : ")
    if ck=="Y":
        test=["The quick brown fox jumps over the lazy dog."," Books are indeed never failing friends of man."]
        test_1=r.choice(test)
        print("*****Typing Test*****")
        print()
        print()
        print(test_1)
        time_1=time()
        test_2=input("Enter:  ")
        time_2=time()
        print(f'speed: {speed(time_1,time_2,test_2)} w/sec')
        print(f'Error: {Errors(test_1,test_2)}')
    elif ck=="N":
        print("thank u")
        break
    else:
        print("wrong typing")
