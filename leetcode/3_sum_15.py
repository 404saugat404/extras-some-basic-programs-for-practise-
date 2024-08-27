def three_sum(list):
    h={}
    n=len(list)
    s=set()

    for i , num in enumerate(list):
        h[num]=i

    for i in range(n):
        for j in range(i+1, n):
            #list[a]+list[b]+list[c]=0
            #or list[c]=-list[a]-list[b]

            desired=-list[i]-list[j]

            if desired in h and h[desired]!=i and h[desired]!=j:
                s.add(tuple(sorted([list[i],list[j],desired])))


    return s

nums = [-1,0,1,2,-1,-4]

print(three_sum(nums))