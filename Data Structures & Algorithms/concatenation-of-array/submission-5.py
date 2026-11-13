class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        t=(len(nums))
        n=[0]*(2*t)

        for i in range (t):
            n[i]=nums[i]
            n[t+i] = nums[i]
        return n
