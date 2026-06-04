class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [1] * len(nums) 

        leftVal = 1
        for i in range(l):
            output[i] = leftVal
            leftVal *= nums[i]
        rval = 1
        for r in range(l-1,-1,-1): 
            output[r] *= rval
            rval *= nums[r]
        
        return output