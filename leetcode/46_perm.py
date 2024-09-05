class Solution:
    def permute(self, nums):
        result=[]

        #base case
        if len(nums)==1:
            return [nums[:]]

        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for j in perms:
                j.append(n)
            result.extend(perms)
            nums.append(n)

        return result
    

abc=[1,2,3]
value=Solution()
print(value.permute(abc))
        