def zigzag(s:str,number_of_rows:int):

    if number_of_rows==1:
        return s
    
    i=0
    d=1

    rows=[[] for _ in range(number_of_rows)]

    for char in s:
        rows[i].append(char)

        if i==0:
            d=1
        
        elif i==number_of_rows-1:
            d=-1

        i=d+1

    
    ret=""
    for i in range(number_of_rows):
        ret=ret+''.join(rows[i])

    return ret

s = "PAYPALISHIRING"
numRows = 3
    
print(zigzag(s,numRows))

#the time complexity for this problem is O(n* number_of_rows)
#the space complexity is O(n+number_of_rows)