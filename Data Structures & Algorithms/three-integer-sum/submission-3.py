class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = [] 

        for i,v in enumerate(nums) :
    
            if i > 0 and v == nums[i-1]: 
                continue 
            
            l, r = (i+1, len(nums)-1)
            while (l < r): 
                var = nums[l] + nums[r] + v 
                if var > 0: 
                    r-=1
                elif var < 0: 
                    l +=1
                else: 
                    store.append([nums[l],nums[r],v])  
                    l+=1
                    r -=1
                    while nums[l]== nums[l-1] and l < r:
                        l+=1               
        return store





'''
 nums = [-1,0,1,2,-1,-4]
sorted = [-4,-1,-1,0,1,2]

[-2,-2,0,0,2,2]

-1,-1,2
while l < r and 
0,-4
1,-1
2,-1
3,0
4,1
5,2

triplets = []
[-4, ] 




'''