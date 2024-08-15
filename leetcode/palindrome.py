class solution(object):
    def pal(self,x):
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False
        
number=int(input("enter the number :"))
sol=solution()
print(sol.pal(number))