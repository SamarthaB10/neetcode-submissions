class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        seen = {} 
        def backTrack(i): 
            if i >= len(cost): 
                return 0 
            

            if i in seen: 
                return seen[i]
            

            one_step = backTrack(i+1)
            two_steps = backTrack(i+2)

            seen[i] = cost[i] + min(one_step,two_steps)
            return seen[i]
        return min(backTrack(0),backTrack(1))
            