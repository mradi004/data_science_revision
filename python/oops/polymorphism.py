#same name of the methods bt different work accourding to the type of object

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"+",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img 
        return complex(newReal,newImg)

n1=complex(2,4)
n1.showNumber()
n2=complex(3,6)

n2.showNumber()

n3=n1+n2
n3.showNumber()

