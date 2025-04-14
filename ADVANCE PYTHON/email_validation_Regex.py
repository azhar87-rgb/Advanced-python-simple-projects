import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{3}$"
user_input=input('Enter email: ')
if re.search(email_condition,user_input):
    print('Right Email')
else:
    print('Wrong Email')