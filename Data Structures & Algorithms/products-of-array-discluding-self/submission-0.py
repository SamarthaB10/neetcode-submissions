class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        count = 0
        while(count < len(nums)): 
            mult = 1
            x = nums[:count] + nums[count+1:]
            for num in x: 
                mult *= num
            res.append(mult)
            count +=1

        return res




