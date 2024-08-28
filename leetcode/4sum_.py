def four_sum(nums,target):
    nums.sort()
    n=len(nums)
    result=[]

    for i in range(n):
        if i>0 and nums[i]==nums[i-1]:
            continue

        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue

            l=j+1
            r=n-1
            while l<r:
                current_sum=nums[i]+nums[j]+nums[l]+nums[r]

                if current_sum==target:
                    result.append([nums[i],nums[j],nums[l],nums[r]])

                    l=l+1
                    r=r-1

                    while l<r and nums[l]==nums[l-1]:
                        l=l+1

                    while l<r and nums[r]==nums[r+1]:
                        r=r-1

                elif current_sum<target:
                    l=l+1

                else:
                    r=r-1


    return result


nums = [1,0,-1,0,-2,2]
target = 0

print(four_sum(nums,target))