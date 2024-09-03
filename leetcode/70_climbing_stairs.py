# class solutions:
#     def stairs(self,n:int)->int:
#         if n==1:
#             return 1
#         elif n==2:
#             return 2
        
#         else:
#             return self.stairs(n-2)+self.stairs(n-1)
        
# value=solutions()
# print(value.stairs(3))
         
# this is the easiest way, but tc is O(2**n)
#sc is O(n)

class solutions:
    def stairs(self,n):
        dict={
            1:1,
            2:2
        }

        def f(n):
            if n in dict:
                return dict[n]
            
            else:
                dict[n]=f(n-2)+f(n-1)
                return dict[n]

        return f(n)
    

value=solutions()
print(value.stairs(5))

#the tc for this soln in O(n)
#sc is O(n)