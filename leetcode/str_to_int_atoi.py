def atoi(s:str):


    #first lets remove the whitespaces
    s=s.strip()

    if not s:
        return 0  #just in case if string is empty 

    #now lets assign sign and result

    sign=1
    result=0

    if s[0]=="-" or s[0]=="+":
        if s[0]=="-":
            sign=-1
        s=s[1:]  #removing the sign present at begining

    for i in s:
        if not i.isdigit():
            break

        result=result*10+int(i)

    result=sign*result



    #now lets just write if else statement for conditions

    if result>=2**31-1:
        return 2**31-1

    elif result<=-2**31:
        return -2**31

    return result

# Input= "42"
# print(atoi(Input))

#output: 42

# Input= " -042"
# print(atoi(Input))

# output: 42


# Input=  "1337c0d3"
# print(atoi(Input))

# output: 1337
