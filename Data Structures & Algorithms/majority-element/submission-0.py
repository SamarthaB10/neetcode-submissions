class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = sorted(nums)

        return x[len(nums)//2]
'''
'''


        