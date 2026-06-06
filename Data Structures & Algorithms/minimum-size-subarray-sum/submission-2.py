class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums) + 1
        l= 0
        window_sum = 0
        for r in range(len(nums)):
            
            window_sum +=nums[r]
            while window_sum >= target: 
                minLen = min((r-l +1), minLen)
                window_sum -= nums[l]
                l+=1
            
        
        
        return minLen if minLen != len(nums) +1 else 0


            


'''
2,1,


'''