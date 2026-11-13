class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s=[0]*2*len(nums)
        s=nums+nums
        return s