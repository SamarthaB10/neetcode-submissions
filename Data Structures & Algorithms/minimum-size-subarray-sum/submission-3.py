class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        minL = len(nums) + 1  
        Sums = 0 
        for r in range(len(nums)): 
            Sums+=nums[r]
            while Sums >= target: 
                Sums -= nums[l]
                
                minL = min(r-l+ 1, minL)
                l+=1
            
        
        return 0 if minL == len(nums)+1 else minL

'''
[2,1,5,1,5,3]



'''