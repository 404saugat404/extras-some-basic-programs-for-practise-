#26. Remove Duplicates from Sorted Array
def duplicate(list):
    j=0
    for i in range(1,len(list)):
        if list[i]!=list[j]:
            j=j+1
            list[j]=list[i]
            
    return j+1



# list=[1,1,2]
# print(duplicate(list))


# list=[0,0,1,1,1,2,2,3,3,4]
# print(duplicate(list))