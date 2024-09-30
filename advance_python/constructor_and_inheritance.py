#what if we create constructor in both child and parent class?which constructor will be called when we created the child object?
#ans is simple, the childs constructor will replace the parents construcotor.
#lets see an example

# class father:
#     def __init__(self) -> None:
#         self.money=1000
#         print("fathers constructor: ", self.money)
    
#     def show(self):
#         print("show money :", self.money)




# class son(father):
#     def son_show(self):
#         print("son output")

# s=son()
#Output:fathers constructor: 1000
#here since only one constructor there is , so child is showing fathers constructor


# class father:
#     def __init__(self) -> None:
#         self.money=1000
#         print("fathers constructor: ", self.money)
    
#     def show(self):
#         print("show money :", self.money)


# class son(father):
#     def __init__(self) -> None:
#         self.money=5000
#         print("sons constructor: ", self.money)


#     def son_show(self):
#         print("son output")

# s=son()
#output:sons constructor:  5000



#what if we want to define constructors at both child and father and still wanna access both constructor?
#can we do it?ans is yes, we can.
#for this we need to use another method called "super"

class father:
    def __init__(self) -> None:
        self.money=1000
        print("fathers constructor: ", self.money)
    
    def show(self):
        print("show money :", self.money)


class son(father):
    def __init__(self):
        super().__init__()
        self.money=5000
        print("sons constructor: ", self.money)


    def son_show(self):
        print("son output")

s=son()
 #output:
# fathers constructor:  1000
# sons constructor:  5000

