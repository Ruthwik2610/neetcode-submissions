from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            res[key].append(w)
        return list(res.values())



