class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for i in self.marks:
            sum+=i

        print("hii ",self.name,"your average marks is",sum/3)    

s1=students("aditya",[45,65,76])
s1.average()