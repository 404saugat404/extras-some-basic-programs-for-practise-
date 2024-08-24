# def rev(integer_to_be_reversed):
#     if integer_to_be_reversed>0:
#         val=int(str(integer_to_be_reversed)[::-1])

#     else:
#         val=-(int(str(abs(integer_to_be_reversed))[::-1]))

#     if val<-2**31 or val>2**31-1:
#         return 0
    
#     else:
#         return val
    

# value=1245

# print(rev(value))

#this way is accepted, but in interview, you may need to do it without converting it to string,soo lets do manual way

def rev(x):
    is_neg=x<0
    x=abs(x)

    reversed_num=0
    while(x>0):
        reversed_num=reversed_num*10+x%10
        x=x//10
    
    if is_neg:
        reversed_num=-reversed_num

    
    if reversed_num>-2*31 or reversed_num<2**31-1:
        return 0
    
    else:
        return reversed_num