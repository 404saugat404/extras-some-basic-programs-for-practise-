class solutions:
    def single_no(self,nums):
        result=0

        for i in nums:
            result=result^i

        return result
    

value=solutions()
print(value.single_no([1,1,8,3,4,4,3,5,5]))