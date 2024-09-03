class solutions:
    def stairs(self,n:int)->int:
        if n==1:
            return 1
        elif n==2:
            return 2
        
        else:
            return self.stairs(n-2)+self.stairs(n-1)
        
value=solutions()
print(value.stairs(3))
         
this is the easiest way, but tc is O(2**n)

