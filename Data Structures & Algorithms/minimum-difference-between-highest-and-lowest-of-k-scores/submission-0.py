class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort() 
        
        l = 0
        minDif = float("inf")

        for r in range(len(nums)): 
            window = r-l + 1 


            if window == k: 
                curDif = nums[r] - nums[l]
                minDif = min(minDif,curDif)
                l+=1
        
        return minDif












'''
[1,2,3,3,5,6]

[1,4,7,9]


'''