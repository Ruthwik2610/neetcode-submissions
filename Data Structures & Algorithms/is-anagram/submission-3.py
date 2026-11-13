class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        j,k= {}, {}
        for i in range(len(s)):
            j[s[i]]=1+j.get(s[i],0)
            k[t[i]]=1+k.get(t[i],0)
        return j==k