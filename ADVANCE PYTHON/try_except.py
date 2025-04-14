# try:
#     num=int(input('Enter a number: '))
#     result=1/num
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print('you entered Zero which is not possible to divide')
    
# except ValueError as e:
#     print(e)
#     print('Enter valid value')
   
# print('thank u fo using this code') 
def add(a,b):
    try:
        return a+b
        
    except:
        raise ValueError('please re_enter the value')  
d=add(1,'h')
print(d)