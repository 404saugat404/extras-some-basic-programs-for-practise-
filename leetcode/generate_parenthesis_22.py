def gen_par(number:int):
    result=[]

    def backtrack(s='',left=0,right=0):
        if len(s)==2*number:
            result.append(s)
            return
        
        if left<number:
            backtrack(s+'(',left+1,right)

        if right<left:
            backtrack(s+')',left,right+1)

    
    backtrack()
    return result


number=2
print(gen_par(number))
            