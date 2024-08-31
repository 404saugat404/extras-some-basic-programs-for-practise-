def dev(dividant,divisor):
    a=abs(dividant)
    b=abs(divisor)

    negative=(dividant>0 and divisor<0) or (dividant<0 and divisor>0)
    output=0
    while a>=b:
        counter=1
        decrement=b

        while a>=decrement:
            a-=decrement
            output+=counter
            counter+=counter
            decrement+=decrement


    output=output if not negative else -output

    return min(max(-2147483648,output),2147483647)




dividend = 7
divisor = -3
print(dev(dividend,divisor))