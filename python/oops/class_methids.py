# class Student:
#     school = "Old School"  # shared by all

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school = new_name


# s1=Student()
# s1.change_school("ddugu")
# print(s1.school)
# print(Student.school)

class person:
    name="anonymous"
    
    # def change_name(self,name):
    #     self.__class__.name=name -- first method
    @classmethod
    def change_name(cls,name):
       cls.name=name
p1=person()
print(p1.name)
p1.change_name("aadi")
print(p1.name)

p2=person()
print(p2.name)
p2.change_name("shivaay")
print(p2.name)
print(p1.name)
print(person.name)