class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = [] 
        subs = [] 



        def dfs(cur,subs): 

            if len(subs) == k: 
                res.append(subs.copy())
                return 
            

            for i in range(cur,n+1): 

                subs.append(i)
                dfs(i+1,subs)

                subs.pop() 
            







        dfs(1,[])
        return res 