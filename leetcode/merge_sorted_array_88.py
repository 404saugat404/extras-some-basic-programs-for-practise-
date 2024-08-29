def sort_array(l1,m, l2,n):

    last=m+n-1

    while m>0 and n>0:

        if l1[m-1]>l2[n-1]:
            l1[last]=l1[m-1]
            m=m-1

        else:
            l1[last]=l2[n-1]
            n=n-1
            
        last=last-1

    while n>0:
        l1[last]=l2[n-1]
        last=last-1
        n=n-1

    


    return l1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(sort_array(nums1,m,nums2,n))