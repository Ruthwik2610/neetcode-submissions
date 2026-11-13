class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=set()
        for i in nums:
            if i in c:
                return True
                break
            else:
                c.add(i)
                print(c)
        return False
        