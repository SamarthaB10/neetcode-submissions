from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        l = r = 0 
        q = deque()

        while r < len(nums):
            
            
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r)

            if l > q[0]: 
                q.popleft()

            if r - l + 1 == k: 
                res.append(nums[q[0]]) 
                l+=1
            
            r+=1
        
        
        
        return res 


















'''
nums = [1,2,1,0,4,2,6]

maxVal Arr = [] 
- loop through window 
add to maxVal iff val > 0 
-pop at end at each phase 

maxVal = [1]
[1,2,1]
maxVal = [2]
res = [2]
maxVal = [] 
[2,1,0]
maxVal = [2]
res = [2,2]
[1,0,4]
maxVal = [1,0,4]
res = [2,2,4]

'''
