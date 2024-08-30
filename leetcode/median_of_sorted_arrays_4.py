def med(nums1: list[int], nums2: list[int]) -> float:
        a,b=nums1,nums2
        if len(b)<len(a):
            a,b=b,a
        total=len(a)+len(b)
        half=total//2
        

        l=0
        r=len(a)-1

        while True:
            i=(l+r)//2 #a
            j=half-i-2 #b

            a_left=a[i] if i>=0 else float("-inf")
            a_right=a[i+1] if (i+1)<len(a) else float("inf")
            b_left=b[j] if j>=0 else float("-inf")
            b_right=b[j+1] if (j+1)<len(b) else float("inf")

            if a_left<=b_right and b_left<=a_right:
                #for odd
                if total%2:
                    return min(a_right,b_right)

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left>b_right:
                r=i-1

            else:
                l=i+1



nums1 =[1,2]
nums2 =[3,4]

print(med(nums1,nums2))
