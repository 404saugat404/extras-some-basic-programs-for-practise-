def no_repeat(s):
    dictionary={}
    left=0
    length=0

    for right in range(len(s)):
        char=s[right]
        
        if char in dictionary and dictionary[char]>=left:
            left=dictionary[char]+1

        else:
            length=max(length,right-left+1)







        dictionary[char]=right
    return length
