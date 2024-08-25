def longest_common_prefix(strs:list[str]):

    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            if i==len(strs[j]) or strs[0][i]!=strs[j][i]:
                return strs[j][:i]
            
    
    return strs[0]

# strs = ["flower","flow","flight"]

# print(longest_common_prefix(strs))

# output:fl


strs = ["dog","racecar","car"]

print(longest_common_prefix(strs))

# output:empty
