class student:

    #default constructors
    def __init__(self):
       pass
    #parametrized constructors
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks



s1=student("Aditya Gupta",67)
print(s1.marks)

class university():
    university_name="DDUGU"

    def __init__(self,Name,course,year):
        self.Name=Name
        self.course=course
        self.year=year

s5=university("Aditya","btech",2022)
print(s5.Name)
print(s5.year)
print(s5.course)
print(s5.university_name)        


s6=university("saTYAM","BTECH",2022)
print(s6.university_name)
print(s6.Name)