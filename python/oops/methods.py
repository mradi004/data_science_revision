class students:
    def __init__(self,name,year):
        self.name=name
        self.year=year

    def greet(self):
        print("hello everyone ",self.name)    


s1=students("aditya",2025)
s1.greet()