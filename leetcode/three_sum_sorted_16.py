def three_sum_closest(nums, target):
    nums.sort()
    closest_sum=float("inf")
    n=len(nums)

    for i in range(n):
        #ignoring duplicates
        if i>0 and nums[i]==nums[i-1]:
            continue

        left=i+1
        right=n-1

        while left<right:
            current_sum=nums[i]+nums[left]+nums[right]

            if abs(current_sum-target)<abs(closest_sum-target):
                closest_sum=current_sum

            if closest_sum==target:
                return closest_sum
            
            elif closest_sum<target:
                left+=1

            else:
                right-=1

    return closest_sum


nums =[-1,2,1,-4]
target =1

print(three_sum_closest(nums,target))