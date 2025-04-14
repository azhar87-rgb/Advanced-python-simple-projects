class HUMAN():
    # def __init__(self,Name,gender):
    #     self.n=Name
    #     self.age=age
    #     self.g=gender
    def greetings(self,Name=None):
        if Name is not None:
            return f'Good Morning, {Name}'
        else:
            return 'Good Morning'
    def setdetail(self,newage):
        self.age=newage
    def getdetail(self):
        return self.age
    def Gender(self,gender=None):
        if gender is 'M':
            return 'HII you are male'
        elif gender is 'F':
            return 'HII you are female'
        else:
            return 'HII you are special'
H=HUMAN()
a=H.greetings('ALI')
b=H.Gender('M')
H.setdetail(32)
print(a)
print(b)
print(f'your age is : {H.getdetail()}')

        