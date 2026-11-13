class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p,q={},{}
        for i in s:
            if i not in p:
                p[i]=0
            p[i]+=1
        for i in t :
            if i not in q:
                q[i]=0
            q[i]+=1
        return p==q

        

        
        


        