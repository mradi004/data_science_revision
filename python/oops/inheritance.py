class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started....")

class toyotacar(car):
    
    def brand(self):
        print("brand is toyota...")
        super.__init__(type)

s1=toyotacar("electric")
print(s1.type)