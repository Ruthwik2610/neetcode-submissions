class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        sett= { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in sett:
                if stack and stack[-1]== sett[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
