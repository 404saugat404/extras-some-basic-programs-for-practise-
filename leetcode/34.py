class solutions:
    def first_and_last(self,nums:list[int],target:int):

        left=self.bin_search(nums,target,True)

        right=self.bin_search(nums,target,False)

        return [left,right]



    def bin_search(self,nums,target,left_bias):
        #normal bin search
        l=0
        r=len(nums)-1
        i=-1

        while l<=r:
            m=(l+r)//2
            if target<nums[m]:
                r=m-1
            
            elif target>nums[m]:
                l=m+1

            else:
                i=m

                #modified bin search

                if left_bias:
                    r=m-1

                else:
                    l=m+1

        return i
    
nums = [5,7,7,8,8,10]
target = 8
value=solutions()


print(value.first_and_last(nums,target))