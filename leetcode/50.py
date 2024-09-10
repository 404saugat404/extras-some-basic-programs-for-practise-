def solution(x,n):
    #defining a helper function

    def help(x,n):
        if x==0: return 0
        if n==0: return 1

        result=help(x,n//2)
        result=result*result

        return x*result if n%2 else result
    
    result=help(x,abs(n))
    
    return result if n>=0 else 1/result

