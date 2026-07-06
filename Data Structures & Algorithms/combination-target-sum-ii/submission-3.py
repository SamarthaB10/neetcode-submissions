class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subs = [] 



        def dfs(i,cur):
            
            if cur == target:
                res.append(subs[:])
                return 
            
            if i == len(candidates) or cur > target:
                return 
            

            subs.append(candidates[i])
            dfs(i+1,cur+candidates[i])

            subs.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1
            
            dfs(i+1,cur)
        

        dfs(0,0)
        return res




            
            