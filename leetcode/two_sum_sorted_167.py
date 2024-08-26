def number(list, target):
    left=0
    right=len(list)-1

    while left<right:
        current_sum=list[left]+list[right]

        if current_sum>target:
            right=right-1

        elif current_sum<target:
            left=left-1

        else:
            return [left+1,right+1]
        

numbers = [2,7,11,15]
target = 9

print(number(numbers,target))

 