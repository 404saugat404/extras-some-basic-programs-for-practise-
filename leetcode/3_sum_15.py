# def three_sum(list):
#     h={}
#     n=len(list)
#     s=set()

#     for i , num in enumerate(list):
#         h[num]=i

#     for i in range(n):
#         for j in range(i+1, n):
#             #list[a]+list[b]+list[c]=0
#             #or list[c]=-list[a]-list[b]

#             desired=-list[i]-list[j]

#             if desired in h and h[desired]!=i and h[desired]!=j:
#                 s.add(tuple(sorted([list[i],list[j],desired])))


#     return s

# nums = [-1,0,1,2,-1,-4]

# print(three_sum(nums))


#the above code is the best solution but you can perform the same operaton using sorted verson too


def three_sum(list):
    list.sort()
    res=[]

    for i in range(len(list)-2):
        if i>0 and list[i]==list[i-1]:
            continue

        left,right=i+1,len(list)-1

        while left<right:

            total=list[i]+list[left]+list[right]

            if total==0:
                res.append([list[i],list[left],list[right]])

                while left<right and list[left]==list[left+1]:
                    left+=1
                while left<right and list[right]==list[right-1]:
                    right-=1

                left+=1
                right-=1



            elif total<0:
                left+=1



            else:
                right-=1


    return res


nums = [-1,0,1,2,-1,-4]

print(three_sum(nums))

