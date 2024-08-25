#advantage: it makes the code reusuable , ie: you dont need to write same code again and again

class father:
    money=5000

    def show(self):
        print("parent class instance method")

    @classmethod

    def showmoney(cls):
        print("parent class class method", cls.money)

class son(father):
    def disp(self):
        print("child class instance method")

s=son()

# s.disp()
#output: child class instance method

#now lets use child to access fathers method/function

s.show()
#output: parent class instance method

s.showmoney()
#output:parent class class method 5000