class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums) 

        for i in range(len(nums)): 
            newArr = nums[:i] + nums[i+1:]
            ct = 1
            for val in newArr: 
                ct *= val
            
            output[i] = ct
        return output