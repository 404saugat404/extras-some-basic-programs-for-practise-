class solution(object):
    def is_valid(self,s):
        stack=[]
        hm={
            ")":"(",

            "}":"{",

            "]":"["
        }

        for i in s:
            if i in hm:
                if stack and stack[-1]==hm[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if not stack:
            return True 
        
        else:
            return False