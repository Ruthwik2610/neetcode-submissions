import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[^a-zA-Z0-9]"
        t=s.replace(" ","")
        p=re.sub(pattern, "",t.lower())
        print(p)
        return p==p[::-1]
        