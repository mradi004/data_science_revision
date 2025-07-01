class car:
    def __init__(self):
        self.clutch=False
        self.brk=False

    def car_start(self):
        self.clutch=True
        self.brk=True
        print("car started successfully")


s1=car()
s1.car_start()        
