def length_of_last_word(s):
    l=0
    i=len(s)-1

    while s[i]==" ":
        i=i-1
    
    while i>=0 and s[i]!=" ":
        l=l+1
        i=i-1
    
    return l

s = "Hello World"
print(length_of_last_word(s))

s = "   fly me   to   the moon  "
print(length_of_last_word(s))

s = "luffy is still joyboy"
print(length_of_last_word(s))