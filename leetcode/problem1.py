def two_sum_problem(numbers,target):
    dict={}
    for i, number in enumerate(numbers):
        value=target-number
        dict[number]=i
        if value in dict:
            print("the numbers are: ",dict[value],i)
    
two_sum_problem([1,2,3,4,5],6)

#this need to be solved more
