class Solution:
    def climbStairs(self, n: int) -> int: 

        store = [-1] * n 


        def dfs(val): 
            if val > n:
                return 0 
            if val == n:
                return 1

            if store[val] != -1:
                return store[val]
            
            store[val] = dfs(val+1) + dfs(val+2)
            return store[val]
        
        return dfs(0)