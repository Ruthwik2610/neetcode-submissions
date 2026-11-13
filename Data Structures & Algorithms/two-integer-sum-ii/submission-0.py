class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s,d =0,len(numbers)-1
        while s<d:
            t=numbers[s]+numbers[d]
            if t==target:
                return [s+1,d+1]
            elif t>target:
                d-=1
            else:
                s+=1
        