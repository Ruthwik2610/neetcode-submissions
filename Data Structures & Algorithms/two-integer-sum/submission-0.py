class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in j:
                return [j[complement], i]
            j[nums[i]] = i
                