# def two_sum_problem(numbers,target):
#     dict={}
#     for i, number in enumerate(numbers):
#         value=target-number
#         dict[number]=i
#         if value in dict:
#             print("the numbers are: ",dict[value],i)
    
# two_sum_problem([1,2,3,4,5],6)


def two_sum(list,target):
    dict={}
    for i , j in enumerate(list):
        s=target-j
        dict[j]=i
        if s in dict:
            print(f"{dict[s],i}") 
        
        
l=[1,2,3,4]
two_sum(l,6)