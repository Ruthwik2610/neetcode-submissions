class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k={}
        for i,j in enumerate(nums):
            d=target -j
            if d in k:
                return[k[d],i]
            k[j]=i
