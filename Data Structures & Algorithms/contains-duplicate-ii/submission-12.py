class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        l = 0 

        seen = set()
        for r in range(len(nums)): 
            w = abs(r-l)
            if w > k: 
                seen.remove(nums[l])
                l+=1
            
            if nums[r] in seen:
                return True 
            seen.add(nums[r])

        return False 







'''
[1,2,3,1], k = 3




'''