def med(list1,list2):
    a,b=list1,list2

    if len(a)>len(b):
        a,b=b,a

    l=0
    r=len(a)-1

    total=len(a)+len(b)
    half=total//2

    while True:
        i=(l+r)//2 #a
        j=half-i-2 #b

        a_left=a[i] if i>=0 else float("-inf")
        a_right=a[i+1] if i<len(a) else float("inf")
        
        b_left=b[j] if j>=0 else float("-inf")
        b_right=b[j+1] if j<len(b) else float("inf")



        if a_left<=b_right and b_left<=a_right:
            #odd
            if total%2:
                return min(a_right,b_right)
            
            return (max(a_left,b_left)+min(a_right,b_right))/2
        
        elif a_left>b_right:
            r=i-1

        else:
            r=i+1



nums1 =[1,3]
nums2 =[2]

print(med(nums1,nums2))
