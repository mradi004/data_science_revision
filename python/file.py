#for reading a data
# f=open("demo.txt","r")
# #data=f.read()
# data2=f.readline()
# print(data2)
# print(type(data2))
# f.close()

#for writing in the data
# f=open("demo.txt","w")
# f.write('this is a new line')
# f.close()

# #appending a new line
# f=open("demo.txt","a")
# f.write('hello my name is aditya')
# f.close()


f=open("Demo.txt","r+")
print(f.read())
f.readline()
f.write("hello everyone we are from 4th year")
f.close()