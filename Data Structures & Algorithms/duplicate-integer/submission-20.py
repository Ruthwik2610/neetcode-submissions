class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        t=bool

        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
            
        
            
            

