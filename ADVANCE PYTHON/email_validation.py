email=str(input('please Enter your Email:  '))
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
                    print('wrong email 5')
                    
                else:
                    print('Succesfully, you set up the correct email')
                    
            else:
                   print('wrong email 4')    
        else:
            print('wrong email 3') 
    else:
        print('wrong email 2')
        
else:
    print('wrong email 1')
                   