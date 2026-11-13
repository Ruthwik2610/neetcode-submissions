class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        t=sorted(strs)
        f = t[0]
        l = t[-1]
        i=0

        while i<len(l) and  i<len(f)  and f[i]==l[i]:
            i+=1
        return f[:i]






        