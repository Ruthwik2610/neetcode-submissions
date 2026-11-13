class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s=strs[0]

        for c,l in enumerate(s):
            for t in range (1,len(strs)):
                p=strs[t]
                if c >= len(p) or l!=p[c]:
                    return s[:c]
        return s
                






        