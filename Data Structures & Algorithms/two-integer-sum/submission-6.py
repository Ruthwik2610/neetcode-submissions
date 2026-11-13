class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,j in enumerate(nums):
            d=target -j
            if d in s:
                return [s[d],i]
            s[j]=i
            