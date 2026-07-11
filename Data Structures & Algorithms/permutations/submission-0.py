class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        subs = [] 

        
        left = set(nums)
        def dfs(): 

            if len(subs) == len(nums): 
                res.append(subs.copy())
                return
            
            for num in nums:
                
                if num in left: 
                    subs.append(num)
                    left.remove(num)
                    dfs()

                    subs.pop()
                    left.add(num)
        
        dfs()
        return res

            
            
