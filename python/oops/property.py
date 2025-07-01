class Students:
    def __init__(self,name,phy,che,math):
        self.name=name
        self.phy=phy
        self.che=che
        self.math=math

    @property
    def percentage(self):
        return (self.phy+self.che+self.math)/3

        
s1=Students("aadi",56,78,45) 
print(s1.percentage)       

s1.phy=99
print(s1.percentage)
        