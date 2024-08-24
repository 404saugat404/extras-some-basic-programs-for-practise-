def rev(integer_to_be_reversed):
    if integer_to_be_reversed>0:
        val=int(str(integer_to_be_reversed)[::-1])

    else:
        val=-(int(str(abs(integer_to_be_reversed))[::-1]))

    if val<-2**31 or val>2**31-1:
        return 0
    
    else:
        return val
    

value=1245

print(rev(value))

