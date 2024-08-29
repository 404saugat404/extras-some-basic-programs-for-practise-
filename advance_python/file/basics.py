f=open("student.txt","w")
f.write("hello world")
f.close()
print("writting successful ")

f=open("student.txt","r")
data=f.read()
print(data)
f.close()