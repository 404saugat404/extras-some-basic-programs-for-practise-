def position(nums,target):

    nums.append(float("inf")) #this adds infinity ie largeee value at the end of list
    left=0
    right=len(nums)-1


    while left<right:
        mid_value=(left+right)//2
        if target<=nums[mid_value]:
            right=mid_value
        
        else:
            left=mid_value+1

    return left


# nums = [1,3,5,6]
# target = 5

nums = [1,3,5,6]
target = 7

print(position(nums,target))