class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        l,r = 0,len(nums)-1

        while(l < r): 
            curS = nums[l] + nums[r]
            if curS == target: 
                return [l+1,r+1]
            elif curS > target: 
                r-=1
            else:
                l+=1 
        return []
        