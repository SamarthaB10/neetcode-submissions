class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 


        subs = []
        def dfs(i,cur): 
            

            if cur == target: 
                res.append(subs[:])
                return 
            
            if i == len(nums) or cur > target:
                    return 


            subs.append(nums[i])
            dfs(i,cur + nums[i])



            subs.pop()
            dfs(i+1,cur)
        
        dfs(0,0)

        return res
        
            

            