def rem(list,val):
    x=0
    for i in range(0,len(list)):
        if list[i]!=val:
            list[x]=list[i]
            x=x+1

    return x

nums = [3,2,2,3]
val = 3

print(rem(nums,val))