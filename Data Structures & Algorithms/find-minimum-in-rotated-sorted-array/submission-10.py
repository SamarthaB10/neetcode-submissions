class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = (0,len(nums)-1)
        res = nums[0]
        while l < r : 
            middle = (l+r) //2
            

            if nums[middle] > nums[r]: 
                l = middle+1
            
            elif nums[middle] < nums[r]: 
                r =middle

        return nums[l]
'''
561234

56 1234

'''