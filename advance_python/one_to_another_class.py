#here we will learn how to pass the method and parameters of one class to another class

class ClassA:
    def __init__(self,m,n):
        self.name=m
        self.roll=n

    def disp(self):
        print("name: ", self.name)
        print("roll:",self.roll)


#now lets pass the component of classA to another class

class user:
    @staticmethod

    def show(s):
        print("user name:",s.name)  #here name of s.name came from name and roll defined as self.name and self.roll

        print("user roll:",s.roll)
        



objA=ClassA("saugat","39")

user.show(objA)


