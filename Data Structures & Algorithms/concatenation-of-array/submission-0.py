class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        ans[0:len(nums)] = nums[:]
        ans[len(nums):] = nums[:]
    
        return ans


'''
answer = [0,0,0,0,0,0]


'''