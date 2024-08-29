f=open("student.txt","w")
f.write("hello world")
f.close()
print("writting successful ")

f=open("student.txt","r")
print(f.readable())
data=f.read()
print(data)
f.close()

#f.readable()  to check if file can be read or not
#f.writable()  to check if file can be written or not
#f.closed      to check if the file is closed or not
#f.mode        to know the mode of file (read or write)
#f.name        to know the name of the file 