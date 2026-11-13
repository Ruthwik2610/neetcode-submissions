class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        n=len(nums)
        for i in s:
            if nums.count(i)>n//2:
                return i
            