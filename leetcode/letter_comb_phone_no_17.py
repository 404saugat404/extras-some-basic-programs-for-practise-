def combination(number:str):
    phone_dict={
             "2": "abc",
             "3": "def", 
             "4": "ghi", 
             "5": "jkl",
             "6": "mno", 
             "7": "pqrs", 
             "8": "tuv", 
             "9": "wxyz"
    }
    
    result=[]

    #backtracking
    def backtrack(i,current_string): #i is for phone_dict string access and current string is for strng addition
        if len(current_string)==len(number):
            result.append(current_string)
            return
        
        for char in phone_dict[number[i]]:
            backtrack(i+1,current_string+char)

    
    if number:
        backtrack(0,"")

    return result


number="23"
print(combination(number))