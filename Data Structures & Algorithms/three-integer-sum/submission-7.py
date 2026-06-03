class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= [] 
        for i,v in enumerate(nums): 
            if i > 0 and v == nums[i-1]: 
                continue 
            
            l,r = (i+1,len(nums)-1)
            while l < r: 
                cur = nums[l] + nums[r] + v

                if cur < 0: 
                    l+=1
                elif cur > 0 : 
                    r-=1
                else: 
                    res.append([nums[l],nums[r],v])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]: 
                        l+=1
        return res 

'''
[-1,0,1,2,-1,-4]

isolate 1 number, v, find the others to add to x
nums = [-4, -1, -1, 0, 1, 2]
[-4]
[-1]
l = -1,r = 2 2+-1+-2 = 0, [-1,2,-1]
l =0,r = 1 -1+0+1 = 0, [0,1,-1]
[-4]
l = -1, r = 2
-1+2+-4 != 0 
l = -1, r= 1 
l = 0,r=. 
'''