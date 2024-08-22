def add_bin(a,b):
#     a=int(a,2)
#     b=int(b,2)
#     sum=a+b
#     return bin(sum)[2:]

# a="1010"
# b="1111"
# print(add_bin(a,b))
    """
    this way is okey but its easy so lets do a harder way"""

    a=a[::-1]

    b=b[::-1]
    
    result=""
    carry=0
    for i in range(max(len(a),len(b))):
        digit_a=int(a[i]) if i<len(a) else 0

        digit_b=int(b[i]) if i<len(b) else 0

        sum=digit_a+digit_b+carry

        char=str(sum%2)
        result=result+char

        carry=sum//2

    if carry:
        result="1"+result

    return result

a="1010"
b="1111"
print(add_bin(a,b))