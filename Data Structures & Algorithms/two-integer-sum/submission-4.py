class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} 

        for i,v in enumerate(nums): 
            val = target - v

            if val in prev: 
                return [prev[val],i]
            
            prev[v] = i