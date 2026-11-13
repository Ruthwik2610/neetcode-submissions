class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack=[]
        for i in s:
            stack.append(i)
        c=0
        while stack:
            s[c]=stack.pop()
            c+=1


        