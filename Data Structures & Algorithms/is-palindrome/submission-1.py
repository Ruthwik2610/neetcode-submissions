import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[^a-zA-Z0-9]"
        p=re.sub(pattern, "",s.lower())
        print(p)
        return p==p[::-1]
        