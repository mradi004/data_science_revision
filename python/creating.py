with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("gorakhpur","Noida")
print(new_data)

with open("practice.txt","w") as f:
    data=f.write(new_data)

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")    

def check_for_line():
    word="Noida"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no+=1    


check_for_line()            