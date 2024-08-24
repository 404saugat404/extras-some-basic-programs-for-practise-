class OuterClass:
    def __init__(self) -> None:
        self.name="saugat"
        self.gn=self.Gun()  #creating class within class
    
    def show(self):
        print("name :", self.name)

    
    class Gun:
        def __init__(self) -> None:
            self.name="ak"
            self.round=42
            self.mag=2

        def disp(self):
            print("gun name:",self.name)
            print("gun round: ",self.round)
            print("mag: ",self.mag)



#now lets try accessing inner class

#first lets define an obj for main class

obj=OuterClass()
print(obj.name)

#output:saugat

#now lets acces 2nd class

print(obj.gn.name)

#saugat
#ak

#writing outer_class.inner_class.var is kinda annoying, so lets create another obj for easier

obj2=obj.gn

print(obj2.name)

#ak